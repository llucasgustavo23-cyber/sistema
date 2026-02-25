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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_telakm(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 472)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_root = QVBoxLayout(self.centralwidget)
        self.verticalLayout_root.setObjectName(u"verticalLayout_root")
        self.groupDados = QGroupBox(self.centralwidget)
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


        self.verticalLayout_root.addWidget(self.groupDados)

        self.groupKm = QGroupBox(self.centralwidget)
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


        self.verticalLayout_root.addWidget(self.groupKm)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.horizontalSpacer3 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_buttons.addItem(self.horizontalSpacer3)

        self.btnSalvar = QPushButton(self.centralwidget)
        self.btnSalvar.setObjectName(u"btnSalvar")

        self.horizontalLayout_buttons.addWidget(self.btnSalvar)

        self.btnLimpar = QPushButton(self.centralwidget)
        self.btnLimpar.setObjectName(u"btnLimpar")

        self.horizontalLayout_buttons.addWidget(self.btnLimpar)

        self.btnFechar = QPushButton(self.centralwidget)
        self.btnFechar.setObjectName(u"btnFechar")

        self.horizontalLayout_buttons.addWidget(self.btnFechar)


        self.verticalLayout_root.addLayout(self.horizontalLayout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Controle de Quilometragem de Ambul\u00e2ncia", None))
        self.groupDados.setTitle(QCoreApplication.translate("MainWindow", u"Dados do registro", None))
        self.labelPlaca.setText(QCoreApplication.translate("MainWindow", u"Placa:", None))
        self.linePlaca.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex.: ABC1D23 ou ABC-1234", None))
        self.labelDataRegistro.setText(QCoreApplication.translate("MainWindow", u"Data do registro:", None))
        self.dateRegistro.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.groupKm.setTitle(QCoreApplication.translate("MainWindow", u"Quilometragem por m\u00eas", None))
        self.labelAno.setText(QCoreApplication.translate("MainWindow", u"Ano:", None))
        self.btnPreencherAno.setText(QCoreApplication.translate("MainWindow", u"Preencher meses do ano", None))
        self.btnAddMes.setText(QCoreApplication.translate("MainWindow", u"Adicionar m\u00eas", None))
        self.btnRemoverLinha.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.labelTotalTxt.setText(QCoreApplication.translate("MainWindow", u"Total no ano (km):", None))
        self.labelTotalValor.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btnLimpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btnFechar.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
    # retranslateUi

