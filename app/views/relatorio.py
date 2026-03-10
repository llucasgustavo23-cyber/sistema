# app/views/relatorio.py
from PySide6.QtCore import Signal, QDate, Qt
from .ui_relatorio import Ui_relatorio
from app.database import Database
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QHeaderView, QListWidgetItem, QAbstractItemView

class Relatorio(QWidget, Ui_relatorio):
    gotomenu = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._db = Database()

        self._wire()
        self._carregar_ambulancias()
        self._setup_table()

    # ----------------------------------------------------------------
    # Conexões
    # ----------------------------------------------------------------
    def _wire(self):
        self.dateEdit.setDate(QDate.currentDate())

        if hasattr(self, "btnVoltar"):
            self.btnVoltar.clicked.connect(self.gotomenu.emit)
        if hasattr(self, "btnGerar"):
            self.btnGerar.clicked.connect(self._carregar)

    # ----------------------------------------------------------------
    # Setup
    # ----------------------------------------------------------------
    def _setup_table(self):
        header = self.tableDiario.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableDiario.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def _carregar_ambulancias(self):
        """Preenche o combo de ambulâncias com placa."""
        self.comboAmbulancia.clear()
        self.comboAmbulancia.addItem("— Selecione —", None)
        try:
            rows = self._db.listar_ambulancias()
            for row in rows:
                label = f"{row.get('placa', '')}"
                self.comboAmbulancia.addItem(label, row)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível carregar ambulâncias:\n{e}")

    # ----------------------------------------------------------------
    # Gerar relatório
    # ----------------------------------------------------------------
    def _carregar(self):
        amb = self.comboAmbulancia.currentData()

        # ✅ VALIDAÇÃO: bloqueia se nenhuma ambulância foi selecionada
        if amb is None:
            # Destaca o combo visualmente
            self.comboAmbulancia.setStyleSheet(
                "border: 2px solid #dc2626; border-radius: 8px; padding: 7px 12px;"
                "background-color: #fff1f2;"
            )
            self.labelAmb.setStyleSheet("color: #dc2626; font-weight: 700;")
            QMessageBox.warning(
                self,
                "Ambulância não selecionada",
                "Selecione uma ambulância antes de gerar o relatório."
            )
            return

        # Limpa o destaque após seleção válida
        self.comboAmbulancia.setStyleSheet("")
        self.labelAmb.setStyleSheet("")

        data_filtro = self.dateEdit.date()
        mes = data_filtro.month()
        ano = data_filtro.year()

        self._preencher_info_ambulancia(amb)

        id_ambulancia = int(amb["id_ambulancia"]) if amb else None

        try:
            registros = self._db.listar_registros_uso(
                mes=mes,
                ano=ano,
                id_ambulancia=id_ambulancia,
            )
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível carregar registros:\n{e}")
            return

        self._preencher_tabela(registros)
        self._preencher_resumo(registros)

    # ----------------------------------------------------------------
    # Preenche info da ambulância selecionada
    # ----------------------------------------------------------------
    def _preencher_info_ambulancia(self, amb: dict):
        if not amb:
            self.lblChassi.setText("-")
            self.lblPlaca.setText("-")
            self.lblAno.setText("-")
            self.lblData.setText("-")
            self.lblForma.setText("-")
            self.lblUnidade.setText("-")
            return

        self.lblChassi.setText(str(amb.get("chassi") or "-"))
        self.lblPlaca.setText(str(amb.get("placa") or "-"))
        self.lblAno.setText(str(amb.get("ano") or "-"))
        self.lblData.setText(str(amb.get("data_aquisicao") or "-"))
        self.lblForma.setText(str(amb.get("forma_nome") or "-"))
        self.lblUnidade.setText(str(amb.get("cnes") or "-"))

    # ----------------------------------------------------------------
    # Preenche tabela diária
    # ----------------------------------------------------------------
    def _preencher_tabela(self, registros: list):
        t = self.tableDiario
        t.setRowCount(0)

        for rec in registros:
            r = t.rowCount()
            t.insertRow(r)

            data_val = rec.get("data")
            if data_val is None:
                data_str = "-"
            elif hasattr(data_val, "strftime"):
                data_str = data_val.strftime("%d/%m/%Y")
            else:
                data_str = str(data_val)

            total_km = rec.get("total_km") or 0
            rodou    = str(rec.get("rodou") or "-")
            motivo   = str(rec.get("motivo") or "")

            valores = [
                data_str,
                "-",
                "-",
                str(total_km),
                rodou,
                motivo,
            ]

            for c, val in enumerate(valores):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignCenter)
                t.setItem(r, c, item)

    # ----------------------------------------------------------------
    # Preenche resumo
    # ----------------------------------------------------------------
    def _preencher_resumo(self, registros: list):
        if not registros:
            self.lblKmTotal.setText("0 km")
            self.lblDiasRodados.setText("0")
            self.lblDiasParados.setText("0")
            self.lblMediaDiaria.setText("0 km")
            self.lblMaiorDia.setText("0 km")
            self.listMotivos.clear()
            return

        total_km     = sum(int(r.get("total_km") or 0) for r in registros)
        dias_rodados = sum(1 for r in registros if str(r.get("rodou", "")).lower() == "sim")
        dias_parados = sum(1 for r in registros if str(r.get("rodou", "")).lower() == "não")
        maior_dia    = max((int(r.get("total_km") or 0) for r in registros), default=0)
        media        = round(total_km / dias_rodados, 1) if dias_rodados > 0 else 0

        self.lblKmTotal.setText(f"{total_km} km")
        self.lblDiasRodados.setText(str(dias_rodados))
        self.lblDiasParados.setText(str(dias_parados))
        self.lblMediaDiaria.setText(f"{media} km")
        self.lblMaiorDia.setText(f"{maior_dia} km")

        # Motivos de parada
        self.listMotivos.clear()
        motivos: dict = {}
        for r in registros:
            m = (r.get("motivo") or "").strip()
            if m:
                motivos[m] = motivos.get(m, 0) + 1

        for motivo, contagem in sorted(motivos.items(), key=lambda x: -x[1]):
            self.listMotivos.addItem(QListWidgetItem(f"{motivo} ({contagem}x)"))

    # ----------------------------------------------------------------
    # Recarrega ao exibir
    # ----------------------------------------------------------------
    def showEvent(self, event):
        super().showEvent(event)
        self._carregar_ambulancias()