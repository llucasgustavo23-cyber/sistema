# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_modernizada_labels_acima.ui'
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
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_cadastro(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1113, 720)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.title)

        self.card = QFrame(Form)
        self.card.setObjectName(u"card")
        sizePolicy.setHeightForWidth(self.card.sizePolicy().hasHeightForWidth())
        self.card.setSizePolicy(sizePolicy)
        self.card.setFrameShape(QFrame.StyledPanel)
        self.grid = QGridLayout(self.card)
        self.grid.setObjectName(u"grid")
        self.grid.setHorizontalSpacing(24)
        self.grid.setVerticalSpacing(14)
        self.grid.setContentsMargins(12, 12, 12, 12)
        self.denominacao = QLineEdit(self.card)
        self.denominacao.setObjectName(u"denominacao")

        self.grid.addWidget(self.denominacao, 11, 0, 1, 3)

        self.comboBox = QComboBox(self.card)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.grid.addWidget(self.comboBox, 5, 0, 1, 1)

        self.tipo = QComboBox(self.card)
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.setObjectName(u"tipo")

        self.grid.addWidget(self.tipo, 7, 2, 1, 1)

        self.lbl_cnes = QLabel(self.card)
        self.lbl_cnes.setObjectName(u"lbl_cnes")

        self.grid.addWidget(self.lbl_cnes, 8, 2, 1, 1)

        self.lbl_data = QLabel(self.card)
        self.lbl_data.setObjectName(u"lbl_data")

        self.grid.addWidget(self.lbl_data, 6, 0, 1, 1)

        self.radioButton = QRadioButton(self.card)
        self.radioButton.setObjectName(u"radioButton")

        self.grid.addWidget(self.radioButton, 1, 0, 1, 1)

        self.lbl_placa = QLabel(self.card)
        self.lbl_placa.setObjectName(u"lbl_placa")

        self.grid.addWidget(self.lbl_placa, 4, 0, 1, 1)

        self.cnes = QLineEdit(self.card)
        self.cnes.setObjectName(u"cnes")

        self.grid.addWidget(self.cnes, 9, 2, 1, 1)

        self.lbl_chassi = QLabel(self.card)
        self.lbl_chassi.setObjectName(u"lbl_chassi")

        self.grid.addWidget(self.lbl_chassi, 4, 2, 1, 1)

        self.lineEdit = QLineEdit(self.card)
        self.lineEdit.setObjectName(u"lineEdit")

        self.grid.addWidget(self.lineEdit, 3, 0, 1, 3)

        self.lbl_tipo = QLabel(self.card)
        self.lbl_tipo.setObjectName(u"lbl_tipo")

        self.grid.addWidget(self.lbl_tipo, 6, 2, 1, 1)

        self.data = QDateEdit(self.card)
        self.data.setObjectName(u"data")
        self.data.setCalendarPopup(True)

        self.grid.addWidget(self.data, 7, 0, 1, 1)

        self.chassi = QLineEdit(self.card)
        self.chassi.setObjectName(u"chassi")
        self.chassi.setDragEnabled(False)
        self.chassi.setReadOnly(False)
        self.chassi.setClearButtonEnabled(False)

        self.grid.addWidget(self.chassi, 5, 2, 1, 1)

        self.lbl_denominacao = QLabel(self.card)
        self.lbl_denominacao.setObjectName(u"lbl_denominacao")

        self.grid.addWidget(self.lbl_denominacao, 10, 0, 1, 1)

        self.ano = QSpinBox(self.card)
        self.ano.setObjectName(u"ano")
        self.ano.setMinimum(1950)
        self.ano.setMaximum(2100)
        self.ano.setValue(2024)

        self.grid.addWidget(self.ano, 9, 0, 1, 1)

        self.lbl_ano = QLabel(self.card)
        self.lbl_ano.setObjectName(u"lbl_ano")

        self.grid.addWidget(self.lbl_ano, 8, 0, 1, 1)

        self.lbl_modelo = QLabel(self.card)
        self.lbl_modelo.setObjectName(u"lbl_modelo")

        self.grid.addWidget(self.lbl_modelo, 2, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.card)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.grid.addWidget(self.radioButton_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.card)

        self.btnrow = QHBoxLayout()
        self.btnrow.setObjectName(u"btnrow")
        self.btnrow.setContentsMargins(0, 0, 0, 0)
        self.hs = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btnrow.addItem(self.hs)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btnrow.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btnrow.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btnrow.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btnrow.addItem(self.horizontalSpacer_4)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.btnrow.addWidget(self.pushButton)

        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.btnrow.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.btnrow)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setStyleSheet(QCoreApplication.translate("Form", u"font:700 22pt \"Segoe UI\"; padding-bottom:4px;", None))
        self.title.setText(QCoreApplication.translate("Form", u"CADASTRO AMBUL\u00c2NCIAS", None))
        self.card.setStyleSheet(QCoreApplication.translate("Form", u"#card{background:#ffffff;border-radius:12px;padding:20px;border:1px solid #dddddd;}\n"
"QLabel.formLabel{font:600 10pt 'Segoe UI'; color:#444; margin-bottom:4px;}\n"
"QLineEdit,QComboBox,QDateEdit,QSpinBox{background:#f7f7f7;border:1px solid #cfcfcf;border-radius:6px;padding:8px 10px; font:10pt 'Segoe UI';}", None))
        self.denominacao.setPlaceholderText(QCoreApplication.translate("Form", u"Insira aqui", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"5", None))

        self.tipo.setItemText(0, QCoreApplication.translate("Form", u"Compra", None))
        self.tipo.setItemText(1, QCoreApplication.translate("Form", u"Doa\u00e7\u00e3o", None))
        self.tipo.setItemText(2, QCoreApplication.translate("Form", u"Loca\u00e7\u00e3o", None))

        self.lbl_cnes.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_cnes.setText(QCoreApplication.translate("Form", u"CNES", None))
        self.lbl_data.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_data.setText(QCoreApplication.translate("Form", u"Data de aquisi\u00e7\u00e3o", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Reserva", None))
        self.lbl_placa.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_placa.setText(QCoreApplication.translate("Form", u"Modelo", None))
        self.cnes.setPlaceholderText(QCoreApplication.translate("Form", u"Insira aqui", None))
        self.lbl_chassi.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_chassi.setText(QCoreApplication.translate("Form", u"Chassi", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insira aqui", None))
        self.lbl_tipo.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_tipo.setText(QCoreApplication.translate("Form", u"Tipo de aquisi\u00e7\u00e3o", None))
        self.data.setDisplayFormat(QCoreApplication.translate("Form", u"dd/MM/yyyy", None))
        self.chassi.setPlaceholderText(QCoreApplication.translate("Form", u"Insira aqui", None))
        self.lbl_denominacao.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_denominacao.setText(QCoreApplication.translate("Form", u"Denomina\u00e7\u00e3o", None))
        self.lbl_ano.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_ano.setText(QCoreApplication.translate("Form", u"Ano", None))
        self.lbl_modelo.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { font:600 10pt \"Segoe UI\"; color:#444; margin-bottom:4px; }", None))
        self.lbl_modelo.setText(QCoreApplication.translate("Form", u"Placa", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Oficial", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Amcul\u00e2ncias Cadastradas", None))
    # retranslateUi

