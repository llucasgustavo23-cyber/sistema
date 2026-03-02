# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RELATORIO.UI'
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
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_relatorio(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(814, 822)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupFiltros = QGroupBox(Form)
        self.groupFiltros.setObjectName(u"groupFiltros")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.groupFiltros.setFont(font)
        self.horizontalLayout_filtros = QHBoxLayout(self.groupFiltros)
        self.horizontalLayout_filtros.setObjectName(u"horizontalLayout_filtros")
        self.labelAmb = QLabel(self.groupFiltros)
        self.labelAmb.setObjectName(u"labelAmb")
        font1 = QFont()
        font1.setPointSize(10)
        self.labelAmb.setFont(font1)

        self.horizontalLayout_filtros.addWidget(self.labelAmb)

        self.comboAmbulancia = QComboBox(self.groupFiltros)
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.addItem("")
        self.comboAmbulancia.setObjectName(u"comboAmbulancia")
        self.comboAmbulancia.setFont(font1)

        self.horizontalLayout_filtros.addWidget(self.comboAmbulancia)

        self.labelMes = QLabel(self.groupFiltros)
        self.labelMes.setObjectName(u"labelMes")

        self.horizontalLayout_filtros.addWidget(self.labelMes)

        self.labelAno = QLabel(self.groupFiltros)
        self.labelAno.setObjectName(u"labelAno")
        self.labelAno.setFont(font1)

        self.horizontalLayout_filtros.addWidget(self.labelAno)

        self.dateEdit = QDateEdit(self.groupFiltros)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font1)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2010, 1, 1))

        self.horizontalLayout_filtros.addWidget(self.dateEdit)

        self.spacerFiltros1 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_filtros.addItem(self.spacerFiltros1)

        self.btnGerar = QPushButton(self.groupFiltros)
        self.btnGerar.setObjectName(u"btnGerar")
        self.btnGerar.setFont(font1)

        self.horizontalLayout_filtros.addWidget(self.btnGerar)


        self.verticalLayout.addWidget(self.groupFiltros)

        self.groupInfo = QGroupBox(Form)
        self.groupInfo.setObjectName(u"groupInfo")
        font2 = QFont()
        font2.setPointSize(12)
        self.groupInfo.setFont(font2)
        self.gridLayout_info = QGridLayout(self.groupInfo)
        self.gridLayout_info.setObjectName(u"gridLayout_info")
        self.lblAnoTitle = QLabel(self.groupInfo)
        self.lblAnoTitle.setObjectName(u"lblAnoTitle")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.lblAnoTitle.setFont(font3)

        self.gridLayout_info.addWidget(self.lblAnoTitle, 1, 0, 1, 1)

        self.lblAno = QLabel(self.groupInfo)
        self.lblAno.setObjectName(u"lblAno")
        self.lblAno.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_info.addWidget(self.lblAno, 1, 2, 1, 1)

        self.lblUnidade = QLabel(self.groupInfo)
        self.lblUnidade.setObjectName(u"lblUnidade")
        self.lblUnidade.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_info.addWidget(self.lblUnidade, 2, 5, 1, 1)

        self.lblPlacaTitle = QLabel(self.groupInfo)
        self.lblPlacaTitle.setObjectName(u"lblPlacaTitle")
        self.lblPlacaTitle.setFont(font3)

        self.gridLayout_info.addWidget(self.lblPlacaTitle, 0, 3, 1, 1)

        self.lblUnidadeTitle = QLabel(self.groupInfo)
        self.lblUnidadeTitle.setObjectName(u"lblUnidadeTitle")
        self.lblUnidadeTitle.setFont(font3)

        self.gridLayout_info.addWidget(self.lblUnidadeTitle, 2, 3, 1, 1)

        self.lblData = QLabel(self.groupInfo)
        self.lblData.setObjectName(u"lblData")
        self.lblData.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_info.addWidget(self.lblData, 2, 2, 1, 1)

        self.lblFormaTitle = QLabel(self.groupInfo)
        self.lblFormaTitle.setObjectName(u"lblFormaTitle")
        self.lblFormaTitle.setFont(font3)

        self.gridLayout_info.addWidget(self.lblFormaTitle, 1, 3, 1, 1)

        self.lblChassiTitle = QLabel(self.groupInfo)
        self.lblChassiTitle.setObjectName(u"lblChassiTitle")
        self.lblChassiTitle.setFont(font3)

        self.gridLayout_info.addWidget(self.lblChassiTitle, 0, 0, 1, 1)

        self.lblForma = QLabel(self.groupInfo)
        self.lblForma.setObjectName(u"lblForma")
        self.lblForma.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_info.addWidget(self.lblForma, 1, 5, 1, 1)

        self.lblChassi = QLabel(self.groupInfo)
        self.lblChassi.setObjectName(u"lblChassi")
        self.lblChassi.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_info.addWidget(self.lblChassi, 0, 2, 1, 1)

        self.lblDataTitle = QLabel(self.groupInfo)
        self.lblDataTitle.setObjectName(u"lblDataTitle")
        self.lblDataTitle.setFont(font3)

        self.gridLayout_info.addWidget(self.lblDataTitle, 2, 0, 1, 1)

        self.lblPlaca = QLabel(self.groupInfo)
        self.lblPlaca.setObjectName(u"lblPlaca")
        self.lblPlaca.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_info.addWidget(self.lblPlaca, 0, 5, 1, 1)

        self.lblTipoTitle = QLabel(self.groupInfo)
        self.lblTipoTitle.setObjectName(u"lblTipoTitle")
        self.lblTipoTitle.setFont(font3)

        self.gridLayout_info.addWidget(self.lblTipoTitle, 3, 0, 1, 1)

        self.spacerInfo = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_info.addItem(self.spacerInfo, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_info.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_info.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)


        self.verticalLayout.addWidget(self.groupInfo)

        self.groupResumo = QGroupBox(Form)
        self.groupResumo.setObjectName(u"groupResumo")
        self.groupResumo.setFont(font)
        self.gridLayout_resumo = QGridLayout(self.groupResumo)
        self.gridLayout_resumo.setObjectName(u"gridLayout_resumo")
        self.lblKmTotalTitle = QLabel(self.groupResumo)
        self.lblKmTotalTitle.setObjectName(u"lblKmTotalTitle")
        self.lblKmTotalTitle.setFont(font1)

        self.gridLayout_resumo.addWidget(self.lblKmTotalTitle, 1, 0, 1, 1)

        self.lblDiasRodados = QLabel(self.groupResumo)
        self.lblDiasRodados.setObjectName(u"lblDiasRodados")
        self.lblDiasRodados.setStyleSheet(u"font-weight: bold; color: #2e7d32;")

        self.gridLayout_resumo.addWidget(self.lblDiasRodados, 0, 1, 1, 1)

        self.lblDiasParados = QLabel(self.groupResumo)
        self.lblDiasParados.setObjectName(u"lblDiasParados")
        self.lblDiasParados.setStyleSheet(u"font-weight: bold; color: #c62828;")

        self.gridLayout_resumo.addWidget(self.lblDiasParados, 0, 3, 1, 1)

        self.lblDiasParadosTitle = QLabel(self.groupResumo)
        self.lblDiasParadosTitle.setObjectName(u"lblDiasParadosTitle")
        self.lblDiasParadosTitle.setFont(font1)

        self.gridLayout_resumo.addWidget(self.lblDiasParadosTitle, 0, 2, 1, 1)

        self.lblMediaDiariaTitle = QLabel(self.groupResumo)
        self.lblMediaDiariaTitle.setObjectName(u"lblMediaDiariaTitle")
        self.lblMediaDiariaTitle.setFont(font1)

        self.gridLayout_resumo.addWidget(self.lblMediaDiariaTitle, 1, 2, 1, 1)

        self.lblMediaDiaria = QLabel(self.groupResumo)
        self.lblMediaDiaria.setObjectName(u"lblMediaDiaria")
        self.lblMediaDiaria.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_resumo.addWidget(self.lblMediaDiaria, 1, 3, 1, 1)

        self.lblKmTotal = QLabel(self.groupResumo)
        self.lblKmTotal.setObjectName(u"lblKmTotal")
        self.lblKmTotal.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_resumo.addWidget(self.lblKmTotal, 1, 1, 1, 1)

        self.lblMaiorDiaTitle = QLabel(self.groupResumo)
        self.lblMaiorDiaTitle.setObjectName(u"lblMaiorDiaTitle")
        self.lblMaiorDiaTitle.setFont(font1)

        self.gridLayout_resumo.addWidget(self.lblMaiorDiaTitle, 2, 0, 1, 1)

        self.lblMaiorDia = QLabel(self.groupResumo)
        self.lblMaiorDia.setObjectName(u"lblMaiorDia")
        self.lblMaiorDia.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_resumo.addWidget(self.lblMaiorDia, 2, 1, 1, 1)

        self.groupMotivos = QGroupBox(self.groupResumo)
        self.groupMotivos.setObjectName(u"groupMotivos")
        self.groupMotivos.setFont(font1)
        self.verticalLayout_motivos = QVBoxLayout(self.groupMotivos)
        self.verticalLayout_motivos.setObjectName(u"verticalLayout_motivos")
        self.listMotivos = QListWidget(self.groupMotivos)
        self.listMotivos.setObjectName(u"listMotivos")

        self.verticalLayout_motivos.addWidget(self.listMotivos)


        self.gridLayout_resumo.addWidget(self.groupMotivos, 0, 4, 3, 1)

        self.lblDiasRodadosTitle = QLabel(self.groupResumo)
        self.lblDiasRodadosTitle.setObjectName(u"lblDiasRodadosTitle")
        self.lblDiasRodadosTitle.setFont(font1)

        self.gridLayout_resumo.addWidget(self.lblDiasRodadosTitle, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupResumo)

        self.groupTabela = QGroupBox(Form)
        self.groupTabela.setObjectName(u"groupTabela")
        self.verticalLayout_tabela = QVBoxLayout(self.groupTabela)
        self.verticalLayout_tabela.setObjectName(u"verticalLayout_tabela")
        self.tableDiario = QTableWidget(self.groupTabela)
        if (self.tableDiario.columnCount() < 6):
            self.tableDiario.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableDiario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableDiario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableDiario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableDiario.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableDiario.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableDiario.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableDiario.setObjectName(u"tableDiario")
        self.tableDiario.setAlternatingRowColors(True)
        self.tableDiario.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_tabela.addWidget(self.tableDiario)


        self.verticalLayout.addWidget(self.groupTabela)

        self.horizontalLayout_acoes = QHBoxLayout()
        self.horizontalLayout_acoes.setObjectName(u"horizontalLayout_acoes")
        self.btnExportarPDF = QPushButton(Form)
        self.btnExportarPDF.setObjectName(u"btnExportarPDF")

        self.horizontalLayout_acoes.addWidget(self.btnExportarPDF)

        self.btnExportarExcel = QPushButton(Form)
        self.btnExportarExcel.setObjectName(u"btnExportarExcel")

        self.horizontalLayout_acoes.addWidget(self.btnExportarExcel)

        self.btnImprimir = QPushButton(Form)
        self.btnImprimir.setObjectName(u"btnImprimir")

        self.horizontalLayout_acoes.addWidget(self.btnImprimir)

        self.spacerAcoes = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_acoes.addItem(self.spacerAcoes)

        self.btnVoltar = QPushButton(Form)
        self.btnVoltar.setObjectName(u"btnVoltar")

        self.horizontalLayout_acoes.addWidget(self.btnVoltar)


        self.verticalLayout.addLayout(self.horizontalLayout_acoes)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupFiltros.setTitle(QCoreApplication.translate("Form", u"Filtros", None))
        self.labelAmb.setText(QCoreApplication.translate("Form", u"Ambul\u00e2ncia:", None))
        self.comboAmbulancia.setItemText(0, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(1, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(2, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(3, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(4, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(5, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(6, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(7, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(8, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(9, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(10, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(11, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(12, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(13, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(14, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(15, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(16, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(17, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(18, QCoreApplication.translate("Form", u"New Item", None))
        self.comboAmbulancia.setItemText(19, QCoreApplication.translate("Form", u"New Item", None))

        self.labelMes.setText("")
        self.labelAno.setText(QCoreApplication.translate("Form", u"Data", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"M/yyyy", None))
        self.btnGerar.setText(QCoreApplication.translate("Form", u"Gerar Relat\u00f3rio", None))
        self.groupInfo.setTitle(QCoreApplication.translate("Form", u"Informa\u00e7\u00f5es da Ambul\u00e2ncia", None))
        self.lblAnoTitle.setText(QCoreApplication.translate("Form", u"Ano:", None))
        self.lblAno.setText(QCoreApplication.translate("Form", u"-", None))
        self.lblUnidade.setText(QCoreApplication.translate("Form", u"-", None))
        self.lblPlacaTitle.setText(QCoreApplication.translate("Form", u"Placa:", None))
        self.lblUnidadeTitle.setText(QCoreApplication.translate("Form", u"Unidade:", None))
        self.lblData.setText(QCoreApplication.translate("Form", u"-", None))
        self.lblFormaTitle.setText(QCoreApplication.translate("Form", u"Forma de Aquisi\u00e7\u00e3o:", None))
        self.lblChassiTitle.setText(QCoreApplication.translate("Form", u"Chassi:", None))
        self.lblForma.setText(QCoreApplication.translate("Form", u"-", None))
        self.lblChassi.setText(QCoreApplication.translate("Form", u"-", None))
        self.lblDataTitle.setText(QCoreApplication.translate("Form", u"Data de Aquisi\u00e7\u00e3o:", None))
        self.lblPlaca.setText(QCoreApplication.translate("Form", u"-", None))
        self.lblTipoTitle.setText(QCoreApplication.translate("Form", u"Tipo:", None))
        self.groupResumo.setTitle(QCoreApplication.translate("Form", u"Resumo do M\u00eas", None))
        self.lblKmTotalTitle.setText(QCoreApplication.translate("Form", u"Quilometragem total:", None))
        self.lblDiasRodados.setText(QCoreApplication.translate("Form", u"0", None))
        self.lblDiasParados.setText(QCoreApplication.translate("Form", u"0", None))
        self.lblDiasParadosTitle.setText(QCoreApplication.translate("Form", u"Dias parados:", None))
        self.lblMediaDiariaTitle.setText(QCoreApplication.translate("Form", u"M\u00e9dia por dia rodado:", None))
        self.lblMediaDiaria.setText(QCoreApplication.translate("Form", u"0 km", None))
        self.lblKmTotal.setText(QCoreApplication.translate("Form", u"0 km", None))
        self.lblMaiorDiaTitle.setText(QCoreApplication.translate("Form", u"Maior quilometragem di\u00e1ria:", None))
        self.lblMaiorDia.setText(QCoreApplication.translate("Form", u"0 km", None))
        self.groupMotivos.setTitle(QCoreApplication.translate("Form", u"Motivos de parada (contagem)", None))
        self.lblDiasRodadosTitle.setText(QCoreApplication.translate("Form", u"Dias rodados:", None))
        self.groupTabela.setTitle(QCoreApplication.translate("Form", u"Quilometragem di\u00e1ria", None))
        ___qtablewidgetitem = self.tableDiario.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Data", None));
        ___qtablewidgetitem1 = self.tableDiario.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Km Inicial", None));
        ___qtablewidgetitem2 = self.tableDiario.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Km Final", None));
        ___qtablewidgetitem3 = self.tableDiario.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Total do Dia", None));
        ___qtablewidgetitem4 = self.tableDiario.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Rodou?", None));
        ___qtablewidgetitem5 = self.tableDiario.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Motivo", None));
        self.btnExportarPDF.setText(QCoreApplication.translate("Form", u"Exportar PDF", None))
        self.btnExportarExcel.setText(QCoreApplication.translate("Form", u"Exportar Excel", None))
        self.btnImprimir.setText(QCoreApplication.translate("Form", u"Imprimir", None))
        self.btnVoltar.setText(QCoreApplication.translate("Form", u"Voltar", None))
    # retranslateUi

