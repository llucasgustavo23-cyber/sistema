from __future__ import annotations
from typing import Optional

from PySide6.QtWidgets import (
    QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QFrame, QPushButton, QSpacerItem, QSizePolicy,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QAbstractScrollArea, QAbstractItemView, QMessageBox,
)
from PySide6.QtCore import Qt

from app.database import Database

COL_ID      = 0
COL_CHASSI  = 1
COL_MODELO  = 2
COL_ANO     = 3
COL_FORMA   = 4
COL_OFICIAL = 5
COL_RESERVA = 6

COLUNAS = ["ID", "Chassi", "Modelo", "Ano", "Forma de aquisição", "Oficial", "Reserva"]


class ListarDadosDialog(QDialog):

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setWindowTitle("Ambulâncias Cadastradas")
        self.resize(980, 680)
        self._db = Database()
        self._build_ui()
        self._setup_table()
        self.carregar_dados_do_banco()

    def _build_ui(self) -> None:
        self.setStyleSheet("""
            QDialog {
                background: #f3f4f6;
                font-family: "Segoe UI", Arial;
                color: #1f2937;
                font-size: 14px;
            }
            QFrame#cardTabela {
                background: #ffffff;
                border-radius: 14px;
                border: 1px solid #e5e7eb;
                padding: 14px;
            }
            QTableWidget {
                background: #ffffff;
                border-radius: 12px;
                border: 1px solid #d1d5db;
                gridline-color: #e5e7eb;
                selection-background-color: #4f46e5;
                selection-color: white;
                alternate-background-color: #f9fafb;
            }
            QHeaderView::section {
                background: #f1f5f9;
                color: #1f2937;
                padding: 10px;
                border: none;
                font-weight: bold;
                font-size: 14px;
            }
            QTableWidget::item:hover {
                background: #e0e7ff;
                color: #1e1b4b;
            }
            QPushButton#btnVoltar {
                background-color: #6b7280;
                color: white;
                padding: 10px 18px;
                border-radius: 10px;
                font-weight: 600;
                border: none;
            }
            QPushButton#btnVoltar:hover { background-color: #4b5563; }
            QPushButton#btnVoltar:pressed { background-color: #374151; }
        """)

        root = QVBoxLayout(self)
        root.setSpacing(12)
        root.setContentsMargins(16, 16, 16, 16)

        self.tituloPagina = QLabel("Ambulâncias cadastradas")
        self.tituloPagina.setStyleSheet("font-size: 26px; font-weight: 700; color: #111827; padding: 6px 4px 12px 4px;")
        root.addWidget(self.tituloPagina)

        card = QFrame()
        card.setObjectName("cardTabela")
        card.setFrameShape(QFrame.StyledPanel)
        vbox = QVBoxLayout(card)
        vbox.setSpacing(10)
        vbox.setContentsMargins(12, 12, 12, 12)

        self.tabelaAmbulancias = QTableWidget(0, len(COLUNAS))
        self.tabelaAmbulancias.setHorizontalHeaderLabels(COLUNAS)
        self.tabelaAmbulancias.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabelaAmbulancias.setAlternatingRowColors(True)
        self.tabelaAmbulancias.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabelaAmbulancias.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabelaAmbulancias.setShowGrid(True)
        self.tabelaAmbulancias.setSortingEnabled(True)
        self.tabelaAmbulancias.setCornerButtonEnabled(False)
        vbox.addWidget(self.tabelaAmbulancias)

        hbox = QHBoxLayout()
        hbox.setSpacing(10)
        hbox.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.btnVoltar = QPushButton("Voltar")
        self.btnVoltar.setObjectName("btnVoltar")
        self.btnVoltar.clicked.connect(self.reject)
        hbox.addWidget(self.btnVoltar)
        vbox.addLayout(hbox)

        root.addWidget(card)

    def _setup_table(self) -> None:
        t = self.tabelaAmbulancias
        header = t.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(COL_RESERVA, QHeaderView.Stretch)
        t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        t.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        t.setTextElideMode(Qt.ElideNone)
        t.setWordWrap(True)
        t.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        t.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

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

    def showEvent(self, event):
        super().showEvent(event)
        self.carregar_dados_do_banco()