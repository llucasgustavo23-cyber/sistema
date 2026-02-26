# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TELADEMODIFICA.UI'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_modificar(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 581)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")

        self.verticalLayout.addWidget(self.title)

        self.card = QFrame(Form)
        self.card.setObjectName(u"card")
        self.card.setFrameShape(QFrame.StyledPanel)
        self.grid = QGridLayout(self.card)
        self.grid.setObjectName(u"grid")
        self.grid.setHorizontalSpacing(24)
        self.grid.setVerticalSpacing(14)
        self.grid.setContentsMargins(12, 12, 12, 12)
        self.lbl_modelo = QLabel(self.card)
        self.lbl_modelo.setObjectName(u"lbl_modelo")

        self.grid.addWidget(self.lbl_modelo, 0, 0, 1, 1)

        self.modelo = QLineEdit(self.card)
        self.modelo.setObjectName(u"modelo")

        self.grid.addWidget(self.modelo, 1, 0, 1, 2)

        self.lbl_placa = QLabel(self.card)
        self.lbl_placa.setObjectName(u"lbl_placa")

        self.grid.addWidget(self.lbl_placa, 2, 0, 1, 1)

        self.placa = QLineEdit(self.card)
        self.placa.setObjectName(u"placa")

        self.grid.addWidget(self.placa, 3, 0, 1, 1)

        self.lbl_chassi = QLabel(self.card)
        self.lbl_chassi.setObjectName(u"lbl_chassi")

        self.grid.addWidget(self.lbl_chassi, 2, 1, 1, 1)

        self.chassi = QLineEdit(self.card)
        self.chassi.setObjectName(u"chassi")

        self.grid.addWidget(self.chassi, 3, 1, 1, 1)

        self.lbl_data = QLabel(self.card)
        self.lbl_data.setObjectName(u"lbl_data")

        self.grid.addWidget(self.lbl_data, 4, 0, 1, 1)

        self.data = QDateEdit(self.card)
        self.data.setObjectName(u"data")
        self.data.setCalendarPopup(True)

        self.grid.addWidget(self.data, 5, 0, 1, 1)

        self.lbl_tipo = QLabel(self.card)
        self.lbl_tipo.setObjectName(u"lbl_tipo")

        self.grid.addWidget(self.lbl_tipo, 4, 1, 1, 1)

        self.tipo = QComboBox(self.card)
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.setObjectName(u"tipo")

        self.grid.addWidget(self.tipo, 5, 1, 1, 1)

        self.lbl_ano = QLabel(self.card)
        self.lbl_ano.setObjectName(u"lbl_ano")

        self.grid.addWidget(self.lbl_ano, 6, 0, 1, 1)

        self.ano = QSpinBox(self.card)
        self.ano.setObjectName(u"ano")
        self.ano.setMinimum(1950)
        self.ano.setMaximum(2100)
        self.ano.setValue(2024)

        self.grid.addWidget(self.ano, 7, 0, 1, 1)

        self.lbl_cnes = QLabel(self.card)
        self.lbl_cnes.setObjectName(u"lbl_cnes")

        self.grid.addWidget(self.lbl_cnes, 6, 1, 1, 1)

        self.cnes = QLineEdit(self.card)
        self.cnes.setObjectName(u"cnes")

        self.grid.addWidget(self.cnes, 7, 1, 1, 1)

        self.lbl_denominacao = QLabel(self.card)
        self.lbl_denominacao.setObjectName(u"lbl_denominacao")

        self.grid.addWidget(self.lbl_denominacao, 8, 0, 1, 1)

        self.denominacao = QLineEdit(self.card)
        self.denominacao.setObjectName(u"denominacao")

        self.grid.addWidget(self.denominacao, 9, 0, 1, 2)


        self.verticalLayout.addWidget(self.card)

        self.btnrow = QHBoxLayout()
        self.btnrow.setObjectName(u"btnrow")
        self.btnrow.setContentsMargins(0, 0, 0, 0)
        self.hs = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btnrow.addItem(self.hs)

        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.btnrow.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.btnrow)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setStyleSheet(QCoreApplication.translate("Form", u"font:700 22pt \"Segoe UI\"; padding-bottom:4px;", None))
        self.title.setText(QCoreApplication.translate("Form", u"MODIFICAR DADOS", None))
        self.card.setStyleSheet(QCoreApplication.translate("Form", u"#card{background:#ffffff;border-radius:12px;padding:20px;border:1px solid #dddddd;}\n"
"QLabel.formLabel{font:600 10pt 'Segoe UI'; color:#444; margin-bottom:4px;}\n"
"QLineEdit,QComboBox,QDateEdit,QSpinBox{background:#f7f7f7;border:1px solid #cfcfcf;border-radius:6px;padding:8px 10px; font:10pt 'Segoe UI';}", None))
        self.lbl_modelo.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_modelo.setText(QCoreApplication.translate("Form", u"Modelo", None))
        self.modelo.setPlaceholderText(QCoreApplication.translate("Form", u"Insira aqui", None))
        self.lbl_placa.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_placa.setText(QCoreApplication.translate("Form", u"Placa", None))
        self.placa.setPlaceholderText(QCoreApplication.translate("Form", u"Insira aqui", None))
        self.lbl_chassi.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_chassi.setText(QCoreApplication.translate("Form", u"Chassi", None))
        self.chassi.setPlaceholderText(QCoreApplication.translate("Form", u"Insira aqui", None))
        self.lbl_data.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_data.setText(QCoreApplication.translate("Form", u"Data de aquisi\u00e7\u00e3o", None))
        self.data.setDisplayFormat(QCoreApplication.translate("Form", u"dd/MM/yyyy", None))
        self.lbl_tipo.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_tipo.setText(QCoreApplication.translate("Form", u"Tipo de aquisi\u00e7\u00e3o", None))
        self.tipo.setItemText(0, QCoreApplication.translate("Form", u"Compra", None))
        self.tipo.setItemText(1, QCoreApplication.translate("Form", u"Doa\u00e7\u00e3o", None))
        self.tipo.setItemText(2, QCoreApplication.translate("Form", u"Loca\u00e7\u00e3o", None))

        self.lbl_ano.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_ano.setText(QCoreApplication.translate("Form", u"Ano", None))
        self.lbl_cnes.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_cnes.setText(QCoreApplication.translate("Form", u"CNES", None))
        self.cnes.setPlaceholderText(QCoreApplication.translate("Form", u"Insira aqui", None))
        self.lbl_denominacao.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_denominacao.setText(QCoreApplication.translate("Form", u"Denomina\u00e7\u00e3o", None))
        self.denominacao.setPlaceholderText(QCoreApplication.translate("Form", u"Insira aqui", None))
    # retranslateUi

