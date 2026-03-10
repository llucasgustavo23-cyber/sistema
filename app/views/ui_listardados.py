# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (QAbstractItemView, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

_STYLESHEET = u"""
QWidget {
    background-color: #f0f4f8;
    font-family: "Segoe UI", sans-serif;
    font-size: 13px;
    color: #1e293b;
}

QLabel#tituloPagina {
    font-size: 22px;
    font-weight: 700;
    color: #1e293b;
    padding: 4px 0 10px 0;
}

QFrame#cardTabela {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
}

QTableWidget {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    gridline-color: #f1f5f9;
    font-size: 13px;
    selection-background-color: #fee2e2;
    selection-color: #1e293b;
    alternate-background-color: #f8fafc;
}

QTableWidget::item {
    padding: 8px 12px;
    border-bottom: 1px solid #f1f5f9;
}

QTableWidget::item:hover {
    background-color: #fff1f2;
}

QHeaderView::section {
    background-color: #f8fafc;
    color: #64748b;
    font-weight: 700;
    font-size: 11px;
    letter-spacing: 0.5px;
    padding: 10px 12px;
    border: none;
    border-bottom: 2px solid #e2e8f0;
}

QPushButton#btnModificar {
    background-color: #0284c7;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: 600;
    min-height: 36px;
}

QPushButton#btnModificar:hover   { background-color: #0369a1; }
QPushButton#btnModificar:pressed { background-color: #075985; }

QPushButton#btnExcluir {
    background-color: #dc2626;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: 600;
    min-height: 36px;
}

QPushButton#btnExcluir:hover   { background-color: #b91c1c; }
QPushButton#btnExcluir:pressed { background-color: #991b1b; }

QPushButton#btnSalvar {
    background-color: #16a34a;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: 600;
    min-height: 36px;
}

QPushButton#btnSalvar:hover   { background-color: #15803d; }
QPushButton#btnSalvar:pressed { background-color: #166534; }
"""


class Ui_ListarAmbulancias(object):
    def setupUi(self, ListarAmbulancias):
        if not ListarAmbulancias.objectName():
            ListarAmbulancias.setObjectName(u"ListarAmbulancias")
        ListarAmbulancias.resize(980, 680)
        ListarAmbulancias.setStyleSheet(_STYLESHEET)

        self.verticalLayout = QVBoxLayout(ListarAmbulancias)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)

        self.tituloPagina = QLabel(ListarAmbulancias)
        self.tituloPagina.setObjectName(u"tituloPagina")
        self.tituloPagina.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.tituloPagina)

        self.cardTabela = QFrame(ListarAmbulancias)
        self.cardTabela.setObjectName(u"cardTabela")
        self.cardTabela.setFrameShape(QFrame.NoFrame)
        self.vboxCard = QVBoxLayout(self.cardTabela)
        self.vboxCard.setSpacing(10)
        self.vboxCard.setContentsMargins(16, 16, 16, 16)

        self.tabelaAmbulancias = QTableWidget(self.cardTabela)
        self.tabelaAmbulancias.setColumnCount(8)
        for i in range(8):
            self.tabelaAmbulancias.setHorizontalHeaderItem(i, QTableWidgetItem())
        self.tabelaAmbulancias.setObjectName(u"tabelaAmbulancias")
        self.tabelaAmbulancias.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabelaAmbulancias.setAlternatingRowColors(True)
        self.tabelaAmbulancias.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tabelaAmbulancias.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabelaAmbulancias.setSortingEnabled(True)
        self.tabelaAmbulancias.setRowCount(0)
        self.vboxCard.addWidget(self.tabelaAmbulancias)

        self.hboxButtons = QHBoxLayout()
        self.hboxButtons.setSpacing(10)

        self.btnModificar = QPushButton(self.cardTabela)
        self.btnModificar.setObjectName(u"btnModificar")
        self.hboxButtons.addWidget(self.btnModificar)

        self.hboxButtons.addItem(
            QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        )

        self.btnExcluir = QPushButton(self.cardTabela)
        self.btnExcluir.setObjectName(u"btnExcluir")
        self.hboxButtons.addWidget(self.btnExcluir)

        self.btnSalvar = QPushButton(self.cardTabela)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.hboxButtons.addWidget(self.btnSalvar)

        self.vboxCard.addLayout(self.hboxButtons)
        self.verticalLayout.addWidget(self.cardTabela)

        self.retranslateUi(ListarAmbulancias)
        QMetaObject.connectSlotsByName(ListarAmbulancias)

    def retranslateUi(self, ListarAmbulancias):
        ListarAmbulancias.setWindowTitle(QCoreApplication.translate("ListarAmbulancias", u"Ambulâncias Cadastradas", None))
        self.tituloPagina.setText("Ambulâncias cadastradas")
        headers = ["ID", "Chassi", "Modelo", "Ano", "Forma de aquisição", "Tipo de aquisição", "Oficial", "Reserva"]
        for i, txt in enumerate(headers):
            self.tabelaAmbulancias.horizontalHeaderItem(i).setText(txt)
        self.btnModificar.setText("Modificar")
        self.btnExcluir.setText("Excluir")
        self.btnSalvar.setText("Salvar")