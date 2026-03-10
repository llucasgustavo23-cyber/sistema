# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (QAbstractButton, QComboBox, QDateEdit,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

_STYLESHEET = u"""
QWidget {
    background-color: #f0f4f8;
    font-family: "Segoe UI", sans-serif;
    font-size: 13px;
    color: #1e293b;
}

QFrame#card {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
}

QLabel {
    background: transparent;
    color: #475569;
    font-size: 13px;
    font-weight: 500;
}

QLabel#title {
    background: transparent;
    color: #1e293b;
    font-size: 22px;
    font-weight: 700;
    padding-bottom: 4px;
}

QLineEdit, QComboBox, QDateEdit, QSpinBox {
    background-color: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 13px;
    color: #1e293b;
    min-height: 20px;
}

QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QSpinBox:focus {
    border-color: #dc2626;
    background-color: #ffffff;
}

QComboBox::drop-down { border: none; width: 24px; }

QComboBox QAbstractItemView {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    selection-background-color: #fee2e2;
    selection-color: #1e293b;
}

QDateEdit::drop-down { border: none; width: 24px; }
QSpinBox::up-button, QSpinBox::down-button { border: none; width: 18px; }

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

QPushButton#pushButton {
    background-color: #f1f5f9;
    color: #475569;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: 600;
    min-height: 36px;
}

QPushButton#pushButton:hover {
    background-color: #e2e8f0;
    color: #334155;
}

QDialogButtonBox QPushButton {
    border-radius: 8px;
    padding: 10px 24px;
    font-size: 13px;
    font-weight: 600;
    min-height: 36px;
    min-width: 90px;
}

QDialogButtonBox QPushButton[text="OK"],
QDialogButtonBox QPushButton[text="&OK"] {
    background-color: #dc2626;
    color: white;
    border: none;
}

QDialogButtonBox QPushButton[text="OK"]:hover,
QDialogButtonBox QPushButton[text="&OK"]:hover {
    background-color: #b91c1c;
}

QDialogButtonBox QPushButton[text="Cancel"],
QDialogButtonBox QPushButton[text="&Cancel"],
QDialogButtonBox QPushButton[text="Cancelar"] {
    background-color: #ffffff;
    color: #64748b;
    border: 1.5px solid #e2e8f0;
}

QDialogButtonBox QPushButton[text="Cancel"]:hover,
QDialogButtonBox QPushButton[text="&Cancel"]:hover,
QDialogButtonBox QPushButton[text="Cancelar"]:hover {
    background-color: #f8fafc;
    color: #334155;
    border-color: #cbd5e1;
}
"""


class Ui_cadastro(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1113, 720)
        Form.setStyleSheet(_STYLESHEET)

        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)

        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.verticalLayout.addWidget(self.title)

        self.card = QFrame(Form)
        self.card.setObjectName(u"card")
        self.card.setFrameShape(QFrame.StyledPanel)
        self.card.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding))

        self.grid = QGridLayout(self.card)
        self.grid.setHorizontalSpacing(24)
        self.grid.setVerticalSpacing(14)
        self.grid.setContentsMargins(20, 20, 20, 20)

        self.radioButton_2 = QRadioButton(self.card)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.grid.addWidget(self.radioButton_2, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.card)
        self.radioButton.setObjectName(u"radioButton")
        self.grid.addWidget(self.radioButton, 1, 0, 1, 1)

        self.lbl_modelo = QLabel(self.card)
        self.lbl_modelo.setObjectName(u"lbl_modelo")
        self.grid.addWidget(self.lbl_modelo, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.card)
        self.lineEdit.setObjectName(u"lineEdit")
        self.grid.addWidget(self.lineEdit, 3, 0, 1, 3)

        self.lbl_placa = QLabel(self.card)
        self.lbl_placa.setObjectName(u"lbl_placa")
        self.grid.addWidget(self.lbl_placa, 4, 0, 1, 1)

        self.comboBox = QComboBox(self.card)
        self.comboBox.addItems(["Ford", "Fiat", "Honda", "Toyota", "Mercedez"])
        self.comboBox.setObjectName(u"comboBox")
        self.grid.addWidget(self.comboBox, 5, 0, 1, 1)

        self.lbl_chassi = QLabel(self.card)
        self.lbl_chassi.setObjectName(u"lbl_chassi")
        self.grid.addWidget(self.lbl_chassi, 4, 2, 1, 1)

        self.chassi = QLineEdit(self.card)
        self.chassi.setObjectName(u"chassi")
        self.grid.addWidget(self.chassi, 5, 2, 1, 1)

        self.lbl_data = QLabel(self.card)
        self.lbl_data.setObjectName(u"lbl_data")
        self.grid.addWidget(self.lbl_data, 6, 0, 1, 1)

        self.lbl_tipo = QLabel(self.card)
        self.lbl_tipo.setObjectName(u"lbl_tipo")
        self.grid.addWidget(self.lbl_tipo, 6, 2, 1, 1)

        self.data = QDateEdit(self.card)
        self.data.setObjectName(u"data")
        self.data.setCalendarPopup(True)
        self.grid.addWidget(self.data, 7, 0, 1, 1)

        self.tipo = QComboBox(self.card)
        self.tipo.addItems(["Doação", "Compra", "Emenda parlamentar"])
        self.tipo.setObjectName(u"tipo")
        self.grid.addWidget(self.tipo, 7, 2, 1, 1)

        self.lbl_ano = QLabel(self.card)
        self.lbl_ano.setObjectName(u"lbl_ano")
        self.grid.addWidget(self.lbl_ano, 8, 0, 1, 1)

        self.lbl_cnes = QLabel(self.card)
        self.lbl_cnes.setObjectName(u"lbl_cnes")
        self.grid.addWidget(self.lbl_cnes, 8, 2, 1, 1)

        self.ano = QSpinBox(self.card)
        self.ano.setObjectName(u"ano")
        self.ano.setMinimum(1950)
        self.ano.setMaximum(2100)
        self.ano.setValue(2024)
        self.grid.addWidget(self.ano, 9, 0, 1, 1)

        self.cnes = QLineEdit(self.card)
        self.cnes.setObjectName(u"cnes")
        self.grid.addWidget(self.cnes, 9, 2, 1, 1)

        self.lbl_denominacao = QLabel(self.card)
        self.lbl_denominacao.setObjectName(u"lbl_denominacao")
        self.grid.addWidget(self.lbl_denominacao, 10, 0, 1, 1)

        self.denominacao = QLineEdit(self.card)
        self.denominacao.setObjectName(u"denominacao")
        self.grid.addWidget(self.denominacao, 11, 0, 1, 3)

        self.verticalLayout.addWidget(self.card)

        # ── Botões ─────────────────────────────────────────────────
        self.btnrow = QHBoxLayout()
        self.btnrow.setSpacing(10)
        self.btnrow.addItem(
            QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        )

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.btnrow.addWidget(self.pushButton)

        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.btnrow.addWidget(self.buttonBox)

        self.verticalLayout.addLayout(self.btnrow)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Cadastro de Ambulância", None))
        self.title.setText("CADASTRO AMBULÂNCIAS")
        self.radioButton_2.setText("Oficial")
        self.radioButton.setText("Reserva")
        self.lbl_modelo.setText("Placa")
        self.lineEdit.setPlaceholderText("Insira aqui")
        self.lbl_placa.setText("Modelo")
        self.lbl_chassi.setText("Chassi")
        self.chassi.setPlaceholderText("Insira aqui")
        self.lbl_data.setText("Data de aquisição")
        self.lbl_tipo.setText("Tipo de aquisição")
        self.data.setDisplayFormat("dd/MM/yyyy")
        self.lbl_ano.setText("Ano")
        self.lbl_cnes.setText("CNES")
        self.cnes.setPlaceholderText("Insira aqui")
        self.lbl_denominacao.setText("Denominação")
        self.denominacao.setPlaceholderText("Insira aqui")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Ambulâncias Cadastradas", None))