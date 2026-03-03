# app/views/telakm.py
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Signal, QDate

from .ui_telakm import Ui_telakm


class telakm(QWidget, Ui_telakm):
    gotomenu = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._meses_no_ano = []  
        self._bloqueado_item_changed = False
        self._setup_defaults()
        self._setup_table()
        self._wire()

    # ---------------------------- Setup ----------------------------

    def _setup_defaults(self):
        # Data do registro → hoje
        if hasattr(self, "dateRegistro"):
            self.dateRegistro.setDate(QDate.currentDate())

        if hasattr(self, "comboAno"):
            self.comboAno.clear()
            ano_atual = QDate.currentDate().year()
            anos = [str(a) for a in range(ano_atual - 5, ano_atual + 3)]
            self.comboAno.addItems(anos)
            idx = self.comboAno.findText(str(ano_atual))
            if idx >= 0:
                self.comboAno.setCurrentIndex(idx)

        if hasattr(self, "linePlaca"):
            self.linePlaca.setText("")
        if hasattr(self, "linePlaca_2"):
            self.linePlaca_2.setText("")

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
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        # Recalcular total quando editar célula
        self.tableKm.itemChanged.connect(self._on_item_changed)

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

    # ---------------------------- Handlers ----------------------------

    def _on_change_ano(self, *_):
        """Quando muda o ano no combo, apenas limpa a lista interna de meses (opcional)."""
        self._meses_no_ano.clear()
        # Se quiser, pode limpar a tabela ao trocar o ano:
        # self.tableKm.setRowCount(0)
        # self._recalcular_total_ano()

    def _on_item_changed(self, item):
        """Recalcula o total do ano quando usuário edita km inicial/final."""
        if self._bloqueado_item_changed:
            return
        self._recalcular_total_ano()

    # ---------------------------- Ações UI ----------------------------

    def _preencher_meses_do_ano(self):
        """Preenche a tabela com meses 01..12 do ano selecionado (não duplica existentes)."""
        if not hasattr(self, "tableKm") or not hasattr(self, "comboAno"):
            return

        ano = self.comboAno.currentText().strip() if self.comboAno else ""
        if not ano.isdigit():
            QMessageBox.warning(self, "Ano inválido", "Selecione um ano válido.")
            return

        # Evita disparar itemChanged em lote
        self._bloqueado_item_changed = True

        meses = [f"{m:02d}/{ano}" for m in range(1, 13)]
        # Garante que _meses_no_ano está sincronizado com a tabela
        existentes = set(self._listar_meses_da_tabela())
        for mes in meses:
            if mes in existentes:
                continue
            self._inserir_linha(mes, "", "")

        self._bloqueado_item_changed = False
        self._recalcular_total_ano()

    def _adicionar_mes(self):
        """Adiciona o próximo mês faltante do ano selecionado (01..12/AAAA)."""
        if not hasattr(self, "tableKm") or not hasattr(self, "comboAno"):
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
        """Remove a linha selecionada na tabela."""
        if not hasattr(self, "tableKm"):
            return
        linha = self.tableKm.currentRow()
        if linha < 0:
            QMessageBox.information(self, "Remover", "Selecione uma linha para remover.")
            return
        self.tableKm.removeRow(linha)
        self._recalcular_total_ano()

    
    def _limpar_tudo(self):
        """Confirma e limpa campos e tabela."""
        resposta = QMessageBox.question(
            self,
            "Confirmar limpeza",
            "Tem certeza de que deseja limpar todos os campos e a tabela?\n"
            "Esta ação não pode ser desfeita.",
            QMessageBox.yes | QMessageBox.No,
            QMessageBox.No
        )

        if resposta != QMessageBox.Yes:
            return  # usuário cancelou

        if hasattr(self, "linePlaca"):
            self.linePlaca.clear()
        if hasattr(self, "linePlaca_2"):
            self.linePlaca_2.clear()
        if hasattr(self, "dateRegistro"):
            self.dateRegistro.setDate(QDate.currentDate())
        if hasattr(self, "tableKm"):
            self.tableKm.setRowCount(0)
        if hasattr(self, "labelTotalValor"):
            self.labelTotalValor.setText("0")


    def _salvar(self):
        """
        Placeholder de salvar.
        Aqui você:
          - lê placa, data, linhas da tabela
          - valida
          - persiste no MySQL
        """
        placa = self.linePlaca.text().strip() if hasattr(self, "linePlaca") else ""
        if not placa:
            QMessageBox.warning(self, "Validação", "Informe a placa.")
            return

        # Coletar linhas
        registros = []
        for i in range(self.tableKm.rowCount()):
            mes = self._texto_item(i, 0)
            km_ini = self._to_int(self._texto_item(i, 1))
            km_fim = self._to_int(self._texto_item(i, 2))
            if not mes:
                continue
            registros.append({"mes": mes, "km_ini": km_ini, "km_fim": km_fim})

        # TODO: Salvar no banco (use seu Database/pymysql aqui)
        # Exemplo:
        # db = Database()
        # for r in registros:
        #     db.salvar_km_mensal(placa, r["mes"], r["km_ini"], r["km_fim"])

        QMessageBox.information(self, "Salvar", "Registro(s) salvo(s) com sucesso!")

    # ---------------------------- Helpers tabela/total ----------------------------

    def _listar_meses_da_tabela(self):
        meses = []
        for i in range(self.tableKm.rowCount()):
            meses.append(self._texto_item(i, 0))
        return meses

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
