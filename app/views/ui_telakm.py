# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TELAKM.UI'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFormLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_telakm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(703, 423)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupDados = QGroupBox(Form)
        self.groupDados.setObjectName(u"groupDados")
        self.formLayout = QFormLayout(self.groupDados)
        self.formLayout.setObjectName(u"formLayout")
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


        self.verticalLayout.addWidget(self.groupDados)

        self.groupKm = QGroupBox(Form)
        self.groupKm.setObjectName(u"groupKm")
        self.verticalLayout_km = QVBoxLayout(self.groupKm)
        self.verticalLayout_km.setObjectName(u"verticalLayout_km")
        self.horizontalLayout_top = QHBoxLayout()
        self.horizontalLayout_top.setObjectName(u"horizontalLayout_top")
        self.labelAno = QLabel(self.groupKm)
        self.labelAno.setObjectName(u"labelAno")

        self.horizontalLayout_top.addWidget(self.labelAno)

        self.comboAno = QComboBox(self.groupKm)
        self.comboAno.setObjectName(u"comboAno")

        self.horizontalLayout_top.addWidget(self.comboAno)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_top.addItem(self.horizontalSpacer)

        self.btnPreencherAno = QPushButton(self.groupKm)
        self.btnPreencherAno.setObjectName(u"btnPreencherAno")

        self.horizontalLayout_top.addWidget(self.btnPreencherAno)

        self.btnAddMes = QPushButton(self.groupKm)
        self.btnAddMes.setObjectName(u"btnAddMes")

        self.horizontalLayout_top.addWidget(self.btnAddMes)

        self.btnRemoverLinha = QPushButton(self.groupKm)
        self.btnRemoverLinha.setObjectName(u"btnRemoverLinha")

        self.horizontalLayout_top.addWidget(self.btnRemoverLinha)


        self.verticalLayout_km.addLayout(self.horizontalLayout_top)

        self.tableKm = QTableWidget(self.groupKm)
        if (self.tableKm.columnCount() < 3):
            self.tableKm.setColumnCount(3)
        self.tableKm.setObjectName(u"tableKm")
        self.tableKm.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableKm.setAlternatingRowColors(True)
        self.tableKm.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableKm.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableKm.setRowCount(0)
        self.tableKm.setColumnCount(3)

        self.verticalLayout_km.addWidget(self.tableKm)

        self.horizontalLayout_total = QHBoxLayout()
        self.horizontalLayout_total.setObjectName(u"horizontalLayout_total")
        self.horizontalSpacer2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_total.addItem(self.horizontalSpacer2)

        self.labelTotalTxt = QLabel(self.groupKm)
        self.labelTotalTxt.setObjectName(u"labelTotalTxt")

        self.horizontalLayout_total.addWidget(self.labelTotalTxt)

        self.labelTotalValor = QLabel(self.groupKm)
        self.labelTotalValor.setObjectName(u"labelTotalValor")
        self.labelTotalValor.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout_total.addWidget(self.labelTotalValor)


        self.verticalLayout_km.addLayout(self.horizontalLayout_total)


        self.verticalLayout.addWidget(self.groupKm)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.horizontalSpacer3 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_buttons.addItem(self.horizontalSpacer3)

        self.btnSalvar = QPushButton(Form)
        self.btnSalvar.setObjectName(u"btnSalvar")

        self.horizontalLayout_buttons.addWidget(self.btnSalvar)

        self.btnLimpar = QPushButton(Form)
        self.btnLimpar.setObjectName(u"btnLimpar")

        self.horizontalLayout_buttons.addWidget(self.btnLimpar)

        self.btnFechar = QPushButton(Form)
        self.btnFechar.setObjectName(u"btnFechar")

        self.horizontalLayout_buttons.addWidget(self.btnFechar)


        self.verticalLayout.addLayout(self.horizontalLayout_buttons)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupDados.setTitle(QCoreApplication.translate("Form", u"Dados do registro", None))
        self.labelPlaca.setText(QCoreApplication.translate("Form", u"Placa:", None))
        self.linePlaca.setPlaceholderText(QCoreApplication.translate("Form", u"Ex.: ABC1D23 ou ABC-1234", None))
        self.labelDataRegistro.setText(QCoreApplication.translate("Form", u"Data do registro:", None))
        self.dateRegistro.setDisplayFormat(QCoreApplication.translate("Form", u"dd/MM/yyyy", None))
        self.groupKm.setTitle(QCoreApplication.translate("Form", u"Quilometragem por m\u00eas", None))
        self.labelAno.setText(QCoreApplication.translate("Form", u"Ano:", None))
        self.btnPreencherAno.setText(QCoreApplication.translate("Form", u"Preencher meses do ano", None))
        self.btnAddMes.setText(QCoreApplication.translate("Form", u"Adicionar m\u00eas", None))
        self.btnRemoverLinha.setText(QCoreApplication.translate("Form", u"Remover", None))
        self.labelTotalTxt.setText(QCoreApplication.translate("Form", u"Total no ano (km):", None))
        self.labelTotalValor.setText(QCoreApplication.translate("Form", u"0", None))
        self.btnSalvar.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.btnLimpar.setText(QCoreApplication.translate("Form", u"Limpar", None))
        self.btnFechar.setText(QCoreApplication.translate("Form", u"Fechar", None))
    # retranslateUi

