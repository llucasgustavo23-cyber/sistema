# app/views/telakm.py
from datetime import date
import re

from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QHeaderView,
    QCompleter
)
from PySide6.QtCore import Signal, QDate, Qt, QStringListModel

from .ui_telakm import Ui_telakm
from app.database import Database


class telakm(QWidget, Ui_telakm):
    gotomenu = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._db = Database()

        self._meses_no_ano = []
        self._bloqueado_item_changed = False

        # modelos para autocomplete
        self._model_placas = QStringListModel([], self)

        self._setup_defaults()
        self._setup_table()
        self._setup_autocomplete_placa()
        self._wire()
        self._atualizar_estado_funcionamento()  # deixa a UI consistente no início

    # ---------------------------- Setup ----------------------------

    def _setup_defaults(self):
        # Data do registro → hoje
        if hasattr(self, "dateRegistro"):
            self.dateRegistro.setDate(QDate.currentDate())

        # Inicializa combo de anos
        if hasattr(self, "comboAno"):
            self.comboAno.clear()
            ano_atual = QDate.currentDate().year()
            anos = [str(a) for a in range(ano_atual - 5, ano_atual + 3)]
            self.comboAno.addItems(anos)
            idx = self.comboAno.findText(str(ano_atual))
            if idx >= 0:
                self.comboAno.setCurrentIndex(idx)

        # Campos
        if hasattr(self, "linePlaca"):
            self.linePlaca.setText("")
        if hasattr(self, "linePlaca_2"):
            # Campo "KM" (mensal / do mês do dateRegistro)
            self.linePlaca_2.setText("")

        # Funcionamento (Rodou?): padrão = Sim
        if hasattr(self, "radioButton") and hasattr(self, "radioButton_2"):
            if not (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
                self.radioButton.setChecked(True)  # Sim

        # Motivo (lineEdit dentro de groupDados_3)
        if hasattr(self, "lineEdit"):
            self.lineEdit.setText("")

        # Total do ano
        if hasattr(self, "labelTotalValor"):
            self.labelTotalValor.setText("0")

    def _setup_table(self):
        if not hasattr(self, "tableKm"):
            return

        self.tableKm.clear()
        self.tableKm.setRowCount(0)
        self.tableKm.setColumnCount(3)
        self.tableKm.setHorizontalHeaderLabels(["Mês", "Km Inicial", "Km Final"])

        # Redimensionamento amigável
        header = self.tableKm.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        # Recalcular total quando editar célula
        self.tableKm.itemChanged.connect(self._on_item_changed)

    def _setup_autocomplete_placa(self):
        """Liga o campo Placa ao banco usando autocomplete."""
        try:
            placas = self._db.listar_placas()
            self._model_placas.setStringList(placas)
        except Exception as e:
            print("[telakm] Aviso: não consegui carregar placas do BD:", e)
            self._model_placas.setStringList([])

        comp = QCompleter(self._model_placas, self)
        comp.setCaseSensitivity(Qt.CaseInsensitive)
        comp.setFilterMode(Qt.MatchContains)
        comp.setCompletionMode(QCompleter.PopupCompletion)
        self.linePlaca.setCompleter(comp)

    def _wire(self):
        if hasattr(self, "btnFechar"):
            self.btnFechar.clicked.connect(self.gotomenu.emit)

        if hasattr(self, "btnLimpar"):
            self.btnLimpar.clicked.connect(self._limpar_tudo)

        if hasattr(self, "btnSalvar"):
            self.btnSalvar.clicked.connect(self._salvar)

        if hasattr(self, "btnPreencherAno"):
            self.btnPreencherAno.clicked.connect(self._preencher_meses_do_ano)

        if hasattr(self, "btnAddMes"):
            self.btnAddMes.clicked.connect(self._adicionar_mes)

        if hasattr(self, "btnRemoverLinha"):
            self.btnRemoverLinha.clicked.connect(self._remover_linha_selecionada)

        if hasattr(self, "comboAno"):
            self.comboAno.currentIndexChanged.connect(self._on_change_ano)

        # Quando terminar de digitar o KM (mensal), aplica na tabela do mês correspondente
        if hasattr(self, "linePlaca_2"):
            self.linePlaca_2.editingFinished.connect(self._aplicar_km_mensal_input)

        # Rodou? Sim/Não -> ajusta UI e validação
        if hasattr(self, "radioButton") and hasattr(self, "radioButton_2"):
            self.radioButton.toggled.connect(self._atualizar_estado_funcionamento)   # Sim
            self.radioButton_2.toggled.connect(self._atualizar_estado_funcionamento) # Não

    # ---------------------------- Estado “Rodou” ----------------------------

    def _atualizar_estado_funcionamento(self):
        """Se 'Não' rodou: bloqueia edição de KM/tabela e obriga Motivo."""
        rodou = self.radioButton.isChecked() if hasattr(self, "radioButton") else True
        # Habilita/Desabilita campos relacionados a KM
        enable_km = bool(rodou)

        for wname in ("linePlaca_2", "tableKm", "btnPreencherAno", "btnAddMes", "btnRemoverLinha"):
            if hasattr(self, wname):
                widget = getattr(self, wname)
                widget.setEnabled(enable_km)

        # Se NÃO rodou, zera total e limpa tabela
        if not enable_km:
            if hasattr(self, "labelTotalValor"):
                self.labelTotalValor.setText("0")
            if hasattr(self, "tableKm"):
                self.tableKm.setRowCount(0)

        # Motivo: obrigatório se NÃO rodou
        if hasattr(self, "lineEdit"):
            self.lineEdit.setEnabled(True)  # sempre pode digitar motivo
            # Sinaliza visualmente se obrigatório
            if not enable_km:
                # destaque leve
                self.lineEdit.setPlaceholderText("Obrigatório: informe o motivo de NÃO ter rodado")
            else:
                self.lineEdit.setPlaceholderText("Motivo (opcional)")

    # ---------------------------- Handlers ----------------------------

    def _on_change_ano(self, *_):
        self._meses_no_ano.clear()

    def _on_item_changed(self, item):
        if self._bloqueado_item_changed:
            return
        self._recalcular_total_ano()

    # ---------------------------- Ações UI ----------------------------

    def _preencher_meses_do_ano(self):
        if not hasattr(self, "tableKm") or not hasattr(self, "comboAno"):
            return

        # Bloqueio se NÃO rodou
        if hasattr(self, "radioButton_2") and self.radioButton_2.isChecked():
            QMessageBox.information(self, "Funcionamento", "Como a viatura NÃO rodou, não é possível preencher meses.")
            return

        ano = self.comboAno.currentText().strip() if self.comboAno else ""
        if not ano.isdigit():
            QMessageBox.warning(self, "Ano inválido", "Selecione um ano válido.")
            return

        self._bloqueado_item_changed = True

        meses = [f"{m:02d}/{ano}" for m in range(1, 13)]
        existentes = set(self._listar_meses_da_tabela())
        for mes in meses:
            if mes in existentes:
                continue
            self._inserir_linha(mes, "", "")

        self._bloqueado_item_changed = False
        self._recalcular_total_ano()

    def _adicionar_mes(self):
        if not hasattr(self, "tableKm") or not hasattr(self, "comboAno"):
            return

        # Bloqueio se NÃO rodou
        if hasattr(self, "radioButton_2") and self.radioButton_2.isChecked():
            QMessageBox.information(self, "Funcionamento", "Como a viatura NÃO rodou, não é possível adicionar mês.")
            return

        ano = self.comboAno.currentText().strip()
        if not ano.isdigit():
            QMessageBox.warning(self, "Ano inválido", "Selecione um ano válido.")
            return

        existentes = set(self._listar_meses_da_tabela())
        for m in range(1, 13):
            mes = f"{m:02d}/{ano}"
            if mes not in existentes:
                self._inserir_linha(mes, "", "")
                self._recalcular_total_ano()
                return

        QMessageBox.information(self, "Meses completos", "Todos os meses deste ano já foram adicionados.")

    def _remover_linha_selecionada(self):
        if not hasattr(self, "tableKm"):
            return
        linha = self.tableKm.currentRow()
        if linha < 0:
            QMessageBox.information(self, "Remover", "Selecione uma linha para remover.")
            return
        self.tableKm.removeRow(linha)
        self._recalcular_total_ano()

    def _limpar_tudo(self):
        resposta = QMessageBox.question(
            self,
            "Confirmar limpeza",
            "Tem certeza de que deseja limpar todos os campos e a tabela?\n"
            "Esta ação não pode ser desfeita.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if resposta != QMessageBox.Yes:
            return

        if hasattr(self, "linePlaca"):
            self.linePlaca.clear()
        if hasattr(self, "linePlaca_2"):
            self.linePlaca_2.clear()
        if hasattr(self, "lineEdit"):
            self.lineEdit.clear()  # motivo
        if hasattr(self, "dateRegistro"):
            self.dateRegistro.setDate(QDate.currentDate())
        if hasattr(self, "tableKm"):
            self.tableKm.setRowCount(0)
        if hasattr(self, "labelTotalValor"):
            self.labelTotalValor.setText("0")

    # ---------------------------- Lógica: KM mensal -> Tabela ----------------------------

    def _aplicar_km_mensal_input(self):
        """Aplica o valor do campo 'KM' na linha do mês da data selecionada."""
        # Bloqueio se NÃO rodou
        if hasattr(self, "radioButton_2") and self.radioButton_2.isChecked():
            return

        if not hasattr(self, "linePlaca_2"):
            return

        km_txt = (self.linePlaca_2.text() or "").strip()
        km_val = self._parse_km(km_txt)
        if km_val is None:
            return

        # Mês/ano da data do registro
        d = self.dateRegistro.date() if hasattr(self, "dateRegistro") else QDate.currentDate()
        mes_str = f"{d.month():02d}/{d.year()}"

        # Insere/atualiza a linha do mês
        self._upsert_mes(mes_str, km_val)
        self._recalcular_total_ano()

    def _parse_km(self, txt: str) -> int | None:
        if not txt:
            return None
        # aceita "100", "100km", "100 KM" etc.
        digs = re.sub(r"\D+", "", txt)
        if not digs:
            return None
        try:
            return int(digs)
        except Exception:
            return None

    def _upsert_mes(self, mes: str, km_final: int):
        self._bloqueado_item_changed = True

        row = self._find_row_by_mes(mes)
        if row is None:
            self._inserir_linha(mes, "0", str(km_final))
        else:
            ini_txt = self._texto_item(row, 1) or "0"
            self.tableKm.setItem(row, 1, QTableWidgetItem(str(ini_txt)))
            self.tableKm.setItem(row, 2, QTableWidgetItem(str(km_final)))

        self._bloqueado_item_changed = False

    def _find_row_by_mes(self, mes: str) -> int | None:
        for i in range(self.tableKm.rowCount()):
            if self._texto_item(i, 0) == mes:
                return i
        return None

    # ---------------------------- Salvar ----------------------------

    def _salvar(self):
        """
        Salva em 'registro_uso' (total_km, motivo, data).
        Regras:
          - Se 'Não' rodou: exige motivo, salva total_km=0, bloqueia edição de meses.
          - Se 'Sim' rodou: motivo opcional, total_km vem do campo KM se preenchido; senão, do somatório da tabela.
        """
        # Validação da placa apenas se quiser manter como referência na UI (não grava no BD)
        placa = self.linePlaca.text().strip() if hasattr(self, "linePlaca") else ""

        rodou = self.radioButton.isChecked() if hasattr(self, "radioButton") else True
        motivo = (self.lineEdit.text().strip() if hasattr(self, "lineEdit") else "")

        # Data
        dqt = self.dateRegistro.date() if hasattr(self, "dateRegistro") else QDate.currentDate()
        data_py = date(dqt.year(), dqt.month(), dqt.day())

        if not rodou:
            # NÃO rodou -> motivo obrigatório, total_km = 0
            if not motivo:
                QMessageBox.warning(self, "Validação", "Informe o motivo de NÃO ter rodado.")
                if hasattr(self, "lineEdit"):
                    self.lineEdit.setFocus()
                return
            total_km = 0
        else:
            # SIM rodou -> motivo opcional/ignorado
            motivo = None

            # total do campo KM (se houver) OU soma da tabela
            km_input = self._parse_km(self.linePlaca_2.text().strip() if hasattr(self, "linePlaca_2") else "")
            if km_input is not None:
                total_km = km_input
            else:
                try:
                    total_km = int(self.labelTotalValor.text())
                except Exception:
                    total_km = 0

            # Se não tem meses e total 0, não faz sentido salvar
            if self.tableKm.rowCount() == 0 and total_km == 0:
                QMessageBox.warning(self, "Validação", "Adicione meses e quilometragem ou informe o KM do mês.")
                return

        # Persistir no BD
        try:
            new_id = self._db.inserir_registro_uso(
            total_km=int(total_km),
            motivo=motivo,
            data=data_py,
            rodou=("Sim" if rodou else "Não"),
        )
            
        except Exception as e:
            QMessageBox.critical(self, "Erro ao salvar", f"Não foi possível salvar o registro de uso:\n{e}")
            return

        QMessageBox.information(self, "Salvar", f"Registro salvo com sucesso! (ID {new_id})")

    # ---------------------------- Helpers tabela/total ----------------------------

    def _listar_meses_da_tabela(self):
        return [self._texto_item(i, 0) for i in range(self.tableKm.rowCount())]

    def _inserir_linha(self, mes: str, km_ini: str, km_fim: str):
        """Insere uma linha no final com os valores informados."""
        linha = self.tableKm.rowCount()
        self.tableKm.insertRow(linha)

        self.tableKm.setItem(linha, 0, QTableWidgetItem(mes))
        self.tableKm.setItem(linha, 1, QTableWidgetItem(str(km_ini)))
        self.tableKm.setItem(linha, 2, QTableWidgetItem(str(km_fim)))

    def _texto_item(self, row: int, col: int) -> str:
        it = self.tableKm.item(row, col)
        return it.text().strip() if it else ""

    def _to_int(self, s: str) -> int:
        try:
            return int(s)
        except Exception:
            return 0

    def _recalcular_total_ano(self):
        """Soma (km_fim - km_ini) de todas as linhas, ignorando valores inválidos."""
        total = 0
        for i in range(self.tableKm.rowCount()):
            km_ini = self._to_int(self._texto_item(i, 1))
            km_fim = self._to_int(self._texto_item(i, 2))
            if km_fim >= km_ini:
                total += (km_fim - km_ini)
        if hasattr(self, "labelTotalValor"):
            self.labelTotalValor.setText(str(total))