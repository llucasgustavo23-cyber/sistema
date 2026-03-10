# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (QAbstractItemView, QDateEdit, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

_STYLESHEET = u"""
QWidget {
    background-color: #f0f4f8;
    font-family: "Segoe UI", sans-serif;
    font-size: 13px;
    color: #1e293b;
}

QGroupBox {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    margin-top: 14px;
    padding: 12px 16px 16px 16px;
    font-weight: 600;
    font-size: 13px;
    color: #334155;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 14px;
    top: 2px;
    padding: 0 6px;
    background-color: #ffffff;
    color: #dc2626;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

QGroupBox#groupDados_3 {
    border: none;
    background: transparent;
    margin-top: 0px;
    padding: 0px;
}

QGroupBox#groupDados_3::title { color: #64748b; }

QLineEdit {
    background-color: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 13px;
    color: #1e293b;
    min-height: 20px;
    selection-background-color: #dc2626;
}

QLineEdit:focus {
    border-color: #dc2626;
    background-color: #ffffff;
}

QLineEdit:disabled {
    background-color: #f1f5f9;
    color: #94a3b8;
    border-color: #e2e8f0;
}

QDateEdit {
    background-color: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 13px;
    color: #1e293b;
    min-height: 20px;
}

QDateEdit:focus {
    border-color: #dc2626;
    background-color: #ffffff;
}

QDateEdit::drop-down { border: none; width: 24px; }

QLabel {
    background: transparent;
    color: #475569;
    font-size: 13px;
    font-weight: 500;
}

QRadioButton {
    background: transparent;
    color: #475569;
    font-size: 13px;
    spacing: 6px;
}

QRadioButton::indicator {
    width: 16px;
    height: 16px;
    border-radius: 8px;
    border: 2px solid #cbd5e1;
    background: #ffffff;
}

QRadioButton::indicator:checked {
    border-color: #dc2626;
    background-color: #dc2626;
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

QPushButton#btnSalvar {
    background-color: #dc2626;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 28px;
    font-size: 13px;
    font-weight: 600;
    min-width: 100px;
    min-height: 36px;
}

QPushButton#btnSalvar:hover   { background-color: #b91c1c; }
QPushButton#btnSalvar:pressed { background-color: #991b1b; }

QPushButton#btnLimpar {
    background-color: #f1f5f9;
    color: #475569;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 28px;
    font-size: 13px;
    font-weight: 600;
    min-width: 100px;
    min-height: 36px;
}

QPushButton#btnLimpar:hover {
    background-color: #e2e8f0;
    color: #334155;
}

QPushButton#btnFechar {
    background-color: #ffffff;
    color: #64748b;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 28px;
    font-size: 13px;
    font-weight: 600;
    min-width: 100px;
    min-height: 36px;
}

QPushButton#btnFechar:hover {
    background-color: #f8fafc;
    color: #334155;
    border-color: #cbd5e1;
}

QScrollBar:vertical {
    background: #f8fafc;
    width: 8px;
    border-radius: 4px;
}

QScrollBar::handle:vertical {
    background: #cbd5e1;
    border-radius: 4px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover { background: #94a3b8; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0px; }
"""


class Ui_telakm(object):
    def setupUi(self, telakm):
        if not telakm.objectName():
            telakm.setObjectName(u"telakm")
        telakm.resize(820, 620)
        telakm.setStyleSheet(_STYLESHEET)

        self.verticalLayout = QVBoxLayout(telakm)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)

        # ── GroupBox: Quilometragem Mensal ────────────────────────
        self.groupDados_2 = QGroupBox(telakm)
        self.groupDados_2.setObjectName(u"groupDados_2")
        self.formLayout_2 = QFormLayout(self.groupDados_2)
        self.formLayout_2.setHorizontalSpacing(16)
        self.formLayout_2.setVerticalSpacing(12)

        self.labelPlaca_2 = QLabel(self.groupDados_2)
        self.labelPlaca_2.setObjectName(u"labelPlaca_2")
        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelPlaca_2)

        self.linePlaca_2 = QLineEdit(self.groupDados_2)
        self.linePlaca_2.setObjectName(u"linePlaca_2")
        self.linePlaca_2.setMaxLength(10)
        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.linePlaca_2)

        # ── GroupBox: Dados do registro (aninhado) ────────────────
        self.groupDados = QGroupBox(self.groupDados_2)
        self.groupDados.setObjectName(u"groupDados")
        self.formLayout = QFormLayout(self.groupDados)
        self.formLayout.setHorizontalSpacing(16)
        self.formLayout.setVerticalSpacing(12)

        self.labelPlaca = QLabel(self.groupDados)
        self.labelPlaca.setObjectName(u"labelPlaca")
        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelPlaca)

        self.linePlaca = QLineEdit(self.groupDados)
        self.linePlaca.setObjectName(u"linePlaca")
        self.linePlaca.setMaxLength(8)
        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.linePlaca)

        self.labelDataRegistro = QLabel(self.groupDados)
        self.labelDataRegistro.setObjectName(u"labelDataRegistro")
        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelDataRegistro)

        self.dateRegistro = QDateEdit(self.groupDados)
        self.dateRegistro.setObjectName(u"dateRegistro")
        self.dateRegistro.setCalendarPopup(True)
        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateRegistro)

        # ── GroupBox: Funcionamento ────────────────────────────────
        self.groupDados_3 = QGroupBox(self.groupDados)
        self.groupDados_3.setObjectName(u"groupDados_3")
        self.groupDados_3.setFlat(True)
        self.horizontalLayout = QHBoxLayout(self.groupDados_3)
        self.horizontalLayout.setSpacing(16)

        self.labelPlaca_3 = QLabel(self.groupDados_3)
        self.labelPlaca_3.setObjectName(u"labelPlaca_3")
        self.horizontalLayout.addWidget(self.labelPlaca_3)

        self.radioButton = QRadioButton(self.groupDados_3)
        self.radioButton.setObjectName(u"radioButton")
        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupDados_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)

        self.labelDataRegistro_2 = QLabel(self.groupDados_3)
        self.labelDataRegistro_2.setObjectName(u"labelDataRegistro_2")
        self.horizontalLayout.addWidget(self.labelDataRegistro_2)

        self.lineEdit = QLineEdit(self.groupDados_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.groupDados_3)
        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.groupDados)
        self.verticalLayout.addWidget(self.groupDados_2)

        # ── GroupBox: Quilometragem por dia ────────────────────────
        self.groupKm = QGroupBox(telakm)
        self.groupKm.setObjectName(u"groupKm")
        self.verticalLayout_km = QVBoxLayout(self.groupKm)
        self.verticalLayout_km.setSpacing(10)

        self.tableKm = QTableWidget(self.groupKm)
        self.tableKm.setColumnCount(3)
        for i, txt in enumerate(["Data", "Km Inicial", "Km Final"]):
            self.tableKm.setHorizontalHeaderItem(i, QTableWidgetItem())
        self.tableKm.setObjectName(u"tableKm")
        self.tableKm.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableKm.setAlternatingRowColors(True)
        self.tableKm.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableKm.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableKm.setRowCount(0)
        self.verticalLayout_km.addWidget(self.tableKm)

        self.horizontalLayout_total = QHBoxLayout()
        self.horizontalLayout_total.addItem(
            QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        )
        self.labelTotalTxt = QLabel(self.groupKm)
        self.labelTotalTxt.setObjectName(u"labelTotalTxt")
        self.horizontalLayout_total.addWidget(self.labelTotalTxt)
        self.labelTotalValor = QLabel(self.groupKm)
        self.labelTotalValor.setObjectName(u"labelTotalValor")
        self.horizontalLayout_total.addWidget(self.labelTotalValor)
        self.verticalLayout_km.addLayout(self.horizontalLayout_total)
        self.verticalLayout.addWidget(self.groupKm)

        # ── Botões ─────────────────────────────────────────────────
        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setSpacing(10)
        self.horizontalLayout_buttons.addItem(
            QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        )
        self.btnSalvar = QPushButton(telakm)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.horizontalLayout_buttons.addWidget(self.btnSalvar)
        self.btnLimpar = QPushButton(telakm)
        self.btnLimpar.setObjectName(u"btnLimpar")
        self.horizontalLayout_buttons.addWidget(self.btnLimpar)
        self.btnFechar = QPushButton(telakm)
        self.btnFechar.setObjectName(u"btnFechar")
        self.horizontalLayout_buttons.addWidget(self.btnFechar)
        self.verticalLayout.addLayout(self.horizontalLayout_buttons)

        self.retranslateUi(telakm)
        QMetaObject.connectSlotsByName(telakm)

    def retranslateUi(self, telakm):
        telakm.setWindowTitle(QCoreApplication.translate("telakm", u"Registro de Quilometragem", None))
        self.groupDados_2.setTitle("Quilometragem Mensal")
        self.labelPlaca_2.setText("KM rodado no dia:")
        self.linePlaca_2.setPlaceholderText("Ex.: 150")
        self.groupDados.setTitle("Dados do registro")
        self.labelPlaca.setText("Placa:")
        self.linePlaca.setPlaceholderText("Ex.: ABC1D23 ou ABC-1234")
        self.labelDataRegistro.setText("Data do registro:")
        self.dateRegistro.setDisplayFormat("dd/MM/yyyy")
        self.groupDados_3.setTitle("Funcionamento")
        self.labelPlaca_3.setText("Rodou:")
        self.radioButton.setText("Sim")
        self.radioButton_2.setText(QCoreApplication.translate("telakm", u"Não", None))
        self.labelDataRegistro_2.setText("Motivo")
        self.lineEdit.setPlaceholderText("Motivo (opcional)")
        self.groupKm.setTitle("Quilometragem por dia")
        headers = ["Data", "Km Inicial", "Km Final"]
        for i, txt in enumerate(headers):
            self.tableKm.horizontalHeaderItem(i).setText(txt)
        self.labelTotalTxt.setStyleSheet("color: #64748b; font-size: 13px;")
        self.labelTotalTxt.setText("Total no ano (km):")
        self.labelTotalValor.setStyleSheet("font-weight: 700; font-size: 15px; color: #dc2626;")
        self.labelTotalValor.setText("0")
        self.btnSalvar.setText("Salvar")
        self.btnLimpar.setText("Limpar")
        self.btnFechar.setText("Fechar")