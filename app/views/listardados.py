# listardados.py
from __future__ import annotations
from typing import Optional

from PySide6.QtWidgets import (
    QWidget,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
    QSizePolicy,
    QAbstractScrollArea,
    QAbstractItemView,
    QPushButton,
)
from PySide6.QtCore import Signal, Qt

from ui_listardados import Ui_ListarAmbulancias
from app.database import Database
from modificar import Modificar


COL_ID      = 0
COL_CHASSI  = 1
COL_PLACA   = 2
COL_MODELO  = 3
COL_ANO     = 4
COL_FORMA   = 5
COL_OFICIAL = 6
COL_RESERVA = 7

class listardados(QWidget, Ui_ListarAmbulancias):
    gotomenu = Signal()

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setupUi(self)
        self._db = Database()

        self.btnSalvar.hide()

        self.btnVoltar = QPushButton("Voltar")
        self.btnVoltar.setObjectName("btnVoltar")
        self.btnVoltar.setStyleSheet(
            "QPushButton#btnVoltar {"
            "  background-color: #6b7280;"
            "  color: white;"
            "  padding: 10px 18px;"
            "  border-radius: 10px;"
            "  font-weight: 600;"
            "  border: none;"
            "}"
            "QPushButton#btnVoltar:hover { background-color: #4b5563; }"
            "QPushButton#btnVoltar:pressed { background-color: #374151; }"
        )
        self.hboxButtons.addWidget(self.btnVoltar)

        self._setup_table()
        self._wire()
        self.carregar_dados_do_banco()

    def _wire(self) -> None:
        self.btnVoltar.clicked.connect(self.gotomenu.emit)
        self.btnModificar.clicked.connect(self._on_modificar)
        self.btnExcluir.clicked.connect(self._on_excluir)

    def _setup_table(self) -> None:
        t = self.tabelaAmbulancias
        t.setColumnCount(8)
        t.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        t.setHorizontalHeaderItem(1, QTableWidgetItem("Chassi"))
        t.setHorizontalHeaderItem(2, QTableWidgetItem("Placa"))
        t.setHorizontalHeaderItem(3, QTableWidgetItem("Modelo"))
        t.setHorizontalHeaderItem(4, QTableWidgetItem("Ano"))
        t.setHorizontalHeaderItem(5, QTableWidgetItem("Forma de aquisição"))
        t.setHorizontalHeaderItem(6, QTableWidgetItem("Oficial"))
        t.setHorizontalHeaderItem(7, QTableWidgetItem("Reserva"))

        header = t.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(COL_RESERVA, QHeaderView.Stretch)
        t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        t.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        t.setTextElideMode(Qt.ElideNone)
        t.setWordWrap(True)
        t.setSelectionBehavior(QAbstractItemView.SelectRows)
        t.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        t.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        t.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def carregar_dados_do_banco(self) -> None:
        try:
            rows = self._db.listar_ambulancias()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível carregar os dados:\n{e}")
            return

        t = self.tabelaAmbulancias
        t.blockSignals(True)
        t.setRowCount(0)

        for rec in rows:
            r = t.rowCount()
            t.insertRow(r)
            oficial = bool(rec.get("uso_oficial"))
            valores = [
                str(rec.get("id_ambulancia") or ""),
                str(rec.get("chassi") or ""),
                str(rec.get("placa") or ""),
                str(rec.get("modelo_nome") or ""),
                str(rec.get("ano") or ""),
                str(rec.get("forma_nome") or ""),   # forma de aquisição (sem tipo duplicado)
                "SIM" if oficial else "NÃO",
                "NÃO" if oficial else "SIM",
            ]
            for c, val in enumerate(valores):
                item = QTableWidgetItem(val)
                item.setToolTip(val)
                item.setTextAlignment(Qt.AlignCenter)
                t.setItem(r, c, item)

        t.resizeRowsToContents()
        t.blockSignals(False)

    def _on_modificar(self) -> None:
        chassi = self._chassi_selecionado()
        if not chassi:
            QMessageBox.information(self, "Selecione", "Selecione uma ambulância na tabela.")
            return

        dlg = Modificar(chassi=chassi, parent=self)
        if dlg.exec() == Modificar.Accepted:
            self.carregar_dados_do_banco()

    def _on_excluir(self) -> None:
        chassi = self._chassi_selecionado()
        if not chassi:
            QMessageBox.information(self, "Selecione", "Selecione uma ambulância na tabela.")
            return

        resp = QMessageBox.question(
            self,
            "Confirmar exclusão",
            f"Deseja excluir a ambulância com chassi:\n{chassi}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if resp != QMessageBox.Yes:
            return

        try:
            ok = self._db.excluir_ambulancia_por_chassi(chassi)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível excluir:\n{e}")
            return

        if ok:
            QMessageBox.information(self, "Sucesso", "Ambulância excluída com sucesso.")
            self.carregar_dados_do_banco()
        else:
            QMessageBox.warning(self, "Aviso", "Nenhuma linha removida. Verifique o chassi.")

    def _chassi_selecionado(self) -> str:
        t = self.tabelaAmbulancias
        rows = t.selectionModel().selectedRows()
        if not rows:
            return ""
        row = rows[0].row()
        item = t.item(row, COL_CHASSI)
        return item.text().strip() if item else ""

    def showEvent(self, event):
        super().showEvent(event)
        self.carregar_dados_do_banco()