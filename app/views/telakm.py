# app/views/telakm.py
from datetime import date
import re

from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QHeaderView,
    QCompleter, QAbstractItemView
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

        self._model_placas = QStringListModel([], self)

        self._setup_defaults()
        self._setup_table()
        self._setup_autocomplete_placa()
        self._wire()
        self._atualizar_estado_funcionamento()

    # ---------------------------- Setup ----------------------------

    def _setup_defaults(self):
        if hasattr(self, "dateRegistro"):
            self.dateRegistro.setDate(QDate.currentDate())
        if hasattr(self, "linePlaca"):
            self.linePlaca.setText("")
        if hasattr(self, "linePlaca_2"):
            self.linePlaca_2.setText("")
        if hasattr(self, "radioButton") and hasattr(self, "radioButton_2"):
            if not (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
                self.radioButton.setChecked(True)
        if hasattr(self, "lineEdit"):
            self.lineEdit.setText("")
        if hasattr(self, "labelTotalValor"):
            self.labelTotalValor.setText("0")

    def _setup_table(self):
        if not hasattr(self, "tableKm"):
            return

        self.tableKm.setRowCount(0)
        self.tableKm.setColumnCount(3)
        self.tableKm.setHorizontalHeaderLabels(["Data", "Km Inicial", "Km Final"])

        header = self.tableKm.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.tableKm.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableKm.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableKm.verticalHeader().setVisible(False)

    def _setup_autocomplete_placa(self):
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
        if hasattr(self, "radioButton") and hasattr(self, "radioButton_2"):
            self.radioButton.toggled.connect(self._atualizar_estado_funcionamento)
            self.radioButton_2.toggled.connect(self._atualizar_estado_funcionamento)
        if hasattr(self, "linePlaca"):
            self.linePlaca.editingFinished.connect(self._carregar_tabela_por_placa)

    # ---------------------------- Estado "Rodou" ----------------------------

    def _atualizar_estado_funcionamento(self):
        rodou = self.radioButton.isChecked() if hasattr(self, "radioButton") else True
        enable_km = bool(rodou)

        if hasattr(self, "linePlaca_2"):
            self.linePlaca_2.setEnabled(enable_km)

        if hasattr(self, "lineEdit"):
            self.lineEdit.setEnabled(True)
            if not enable_km:
                self.lineEdit.setPlaceholderText("Obrigatório: informe o motivo de NÃO ter rodado")
            else:
                self.lineEdit.setPlaceholderText("Motivo (opcional)")

    # ---------------------------- Tabela: carregar do banco ----------------------------

    def _carregar_tabela_por_placa(self):
        placa = self.linePlaca.text().strip() if hasattr(self, "linePlaca") else ""
        if not placa:
            self.tableKm.setRowCount(0)
            if hasattr(self, "labelTotalValor"):
                self.labelTotalValor.setText("0")
            return

        try:
            registros = self._db.listar_registros_uso(placa=placa)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível carregar registros:\n{e}")
            return

        self._preencher_tabela(registros)

    def _preencher_tabela(self, registros: list):
        t = self.tableKm
        t.setRowCount(0)

        total_geral  = 0
        km_acumulado = 0  # km_inicial do primeiro dia = 0

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

            km_total = int(rec.get("total_km") or 0)
            km_ini   = km_acumulado
            km_fim   = km_ini + km_total
            km_acumulado = km_fim
            total_geral += km_total

            valores = [data_str, str(km_ini), str(km_fim)]

            for c, val in enumerate(valores):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignCenter)
                t.setItem(r, c, item)

        if hasattr(self, "labelTotalValor"):
            self.labelTotalValor.setText(str(total_geral))

    # ---------------------------- Salvar ----------------------------

    def _salvar(self):
        placa = self.linePlaca.text().strip() if hasattr(self, "linePlaca") else ""
        if not placa:
            QMessageBox.warning(self, "Validação", "Informe a placa da ambulância.")
            if hasattr(self, "linePlaca"):
                self.linePlaca.setFocus()
            return

        rodou  = self.radioButton.isChecked() if hasattr(self, "radioButton") else True
        motivo = (self.lineEdit.text().strip() if hasattr(self, "lineEdit") else "")

        dqt     = self.dateRegistro.date() if hasattr(self, "dateRegistro") else QDate.currentDate()
        data_py = date(dqt.year(), dqt.month(), dqt.day())

        if not rodou:
            if not motivo:
                QMessageBox.warning(self, "Validação", "Informe o motivo de NÃO ter rodado.")
                if hasattr(self, "lineEdit"):
                    self.lineEdit.setFocus()
                return
            km_inicial = self._obter_ultimo_km_final(placa)
            km_final   = km_inicial
            total_km   = 0
        else:
            motivo = motivo or None

            km_fim_txt = self.linePlaca_2.text().strip() if hasattr(self, "linePlaca_2") else ""
            km_rodado  = self._parse_km(km_fim_txt)

            if km_rodado is None or km_rodado == 0:
                QMessageBox.warning(self, "Validação", "Informe o KM rodado no dia.")
                if hasattr(self, "linePlaca_2"):
                    self.linePlaca_2.setFocus()
                return

            km_inicial = self._obter_ultimo_km_final(placa)
            km_final   = km_inicial + km_rodado
            total_km   = km_rodado

        try:
            new_id = self._db.inserir_registro_uso(
                total_km=int(total_km),
                motivo=motivo,
                data=data_py,
                rodou=("Sim" if rodou else "Não"),
                placa=placa,
                km_inicial=km_inicial,
                km_final=km_final,
            )
        except Exception as e:
            QMessageBox.critical(self, "Erro ao salvar", f"Não foi possível salvar o registro de uso:\n{e}")
            return

        QMessageBox.information(self, "Salvar", f"Registro salvo com sucesso! (ID {new_id})")

        if hasattr(self, "linePlaca_2"):
            self.linePlaca_2.clear()
        if hasattr(self, "lineEdit"):
            self.lineEdit.clear()
        if hasattr(self, "dateRegistro"):
            self.dateRegistro.setDate(QDate.currentDate())
        if hasattr(self, "radioButton"):
            self.radioButton.setChecked(True)

        self._carregar_tabela_por_placa()

    # ---------------------------- Helpers ----------------------------

    def _obter_ultimo_km_final(self, placa: str) -> int:
        try:
            registros = self._db.listar_registros_uso(placa=placa)
            if not registros:
                return 0
            ultimo  = registros[-1]
            km_fim  = ultimo.get("km_final")
            km_ini  = int(ultimo.get("km_inicial") or 0)
            total   = int(ultimo.get("total_km") or 0)
            if km_fim is not None:
                return int(km_fim)
            return km_ini + total
        except Exception:
            return 0

    def _parse_km(self, txt: str) -> int | None:
        if not txt:
            return None
        digs = re.sub(r"\D+", "", txt)
        if not digs:
            return None
        try:
            return int(digs)
        except Exception:
            return None

    # ---------------------------- Limpar tudo ----------------------------

    def _limpar_tudo(self):
        resposta = QMessageBox.question(
            self,
            "Confirmar limpeza",
            "Tem certeza de que deseja limpar todos os campos?\nEsta ação não pode ser desfeita.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if resposta != QMessageBox.Yes:
            return

        for wname in ("linePlaca", "linePlaca_2", "lineEdit"):
            if hasattr(self, wname):
                getattr(self, wname).clear()
        if hasattr(self, "dateRegistro"):
            self.dateRegistro.setDate(QDate.currentDate())
        if hasattr(self, "tableKm"):
            self.tableKm.setRowCount(0)
        if hasattr(self, "labelTotalValor"):
            self.labelTotalValor.setText("0")
        if hasattr(self, "radioButton"):
            self.radioButton.setChecked(True)

    def hideEvent(self, event):
        super().hideEvent(event)
        if hasattr(self, "tableKm"):
            self.tableKm.setRowCount(0)
        if hasattr(self, "labelTotalValor"):
            self.labelTotalValor.setText("0")