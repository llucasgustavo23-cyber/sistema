# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

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
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

QLabel {
    background: transparent;
    color: #475569;
    font-size: 13px;
}

QLabel[class="valor"] {
    color: #1e293b;
    font-weight: 700;
}

QComboBox {
    background-color: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 7px 12px;
    font-size: 13px;
    color: #1e293b;
    min-height: 20px;
    min-width: 160px;
}

QComboBox:focus {
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

QDateEdit {
    background-color: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 7px 12px;
    font-size: 13px;
    color: #1e293b;
    min-height: 20px;
}

QDateEdit:focus {
    border-color: #dc2626;
    background-color: #ffffff;
}

QDateEdit::drop-down { border: none; width: 24px; }

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

QListWidget {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 13px;
    color: #475569;
}

QListWidget::item {
    padding: 6px 10px;
    border-bottom: 1px solid #f1f5f9;
}

QListWidget::item:selected {
    background-color: #fee2e2;
    color: #1e293b;
}

QPushButton#btnGerar {
    background-color: #dc2626;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 9px 22px;
    font-size: 13px;
    font-weight: 600;
    min-height: 34px;
}

QPushButton#btnGerar:hover   { background-color: #b91c1c; }
QPushButton#btnGerar:pressed { background-color: #991b1b; }

QPushButton#btnExportarPDF {
    background-color: #dc2626;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 9px 18px;
    font-size: 13px;
    font-weight: 600;
    min-height: 34px;
}

QPushButton#btnExportarPDF:hover { background-color: #b91c1c; }

QPushButton#btnExportarExcel {
    background-color: #16a34a;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 9px 18px;
    font-size: 13px;
    font-weight: 600;
    min-height: 34px;
}

QPushButton#btnExportarExcel:hover { background-color: #15803d; }

QPushButton#btnImprimir {
    background-color: #0284c7;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 9px 18px;
    font-size: 13px;
    font-weight: 600;
    min-height: 34px;
}

QPushButton#btnImprimir:hover { background-color: #0369a1; }

QPushButton#btnVoltar {
    background-color: #ffffff;
    color: #64748b;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    padding: 9px 22px;
    font-size: 13px;
    font-weight: 600;
    min-height: 34px;
}

QPushButton#btnVoltar:hover {
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


class Ui_relatorio(object):
    def setupUi(self, relatorio):
        if not relatorio.objectName():
            relatorio.setObjectName(u"relatorio")
        relatorio.resize(900, 860)
        relatorio.setStyleSheet(_STYLESHEET)

        self.verticalLayout = QVBoxLayout(relatorio)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)

        self.groupFiltros = QGroupBox(relatorio)
        self.groupFiltros.setObjectName(u"groupFiltros")
        self.horizontalLayout_filtros = QHBoxLayout(self.groupFiltros)
        self.horizontalLayout_filtros.setSpacing(12)
        self.horizontalLayout_filtros.setObjectName(u"horizontalLayout_filtros")
        self.labelAmb = QLabel(self.groupFiltros)
        self.labelAmb.setObjectName(u"labelAmb")
        self.horizontalLayout_filtros.addWidget(self.labelAmb)
        self.comboAmbulancia = QComboBox(self.groupFiltros)
        self.comboAmbulancia.setObjectName(u"comboAmbulancia")
        self.horizontalLayout_filtros.addWidget(self.comboAmbulancia)
        self.labelAno = QLabel(self.groupFiltros)
        self.labelAno.setObjectName(u"labelAno")
        self.horizontalLayout_filtros.addWidget(self.labelAno)
        self.dateEdit = QDateEdit(self.groupFiltros)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.horizontalLayout_filtros.addWidget(self.dateEdit)
        self.spacerFiltros1 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_filtros.addItem(self.spacerFiltros1)
        self.btnGerar = QPushButton(self.groupFiltros)
        self.btnGerar.setObjectName(u"btnGerar")
        self.horizontalLayout_filtros.addWidget(self.btnGerar)
        self.verticalLayout.addWidget(self.groupFiltros)

        self.groupInfo = QGroupBox(relatorio)
        self.groupInfo.setObjectName(u"groupInfo")
        self.gridLayout_info = QGridLayout(self.groupInfo)
        self.gridLayout_info.setObjectName(u"gridLayout_info")
        self.gridLayout_info.setHorizontalSpacing(16)
        self.gridLayout_info.setVerticalSpacing(10)
        self.lblChassiTitle = QLabel(self.groupInfo)
        self.lblChassiTitle.setObjectName(u"lblChassiTitle")
        self.gridLayout_info.addWidget(self.lblChassiTitle, 0, 0, 1, 1)
        self.lblChassi = QLabel(self.groupInfo)
        self.lblChassi.setObjectName(u"lblChassi")
        self.gridLayout_info.addWidget(self.lblChassi, 1, 0, 1, 1)
        self.gridLayout_info.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum), 0, 1, 2, 1)
        self.lblAnoTitle = QLabel(self.groupInfo)
        self.lblAnoTitle.setObjectName(u"lblAnoTitle")
        self.gridLayout_info.addWidget(self.lblAnoTitle, 0, 2, 1, 1)
        self.lblAno = QLabel(self.groupInfo)
        self.lblAno.setObjectName(u"lblAno")
        self.gridLayout_info.addWidget(self.lblAno, 1, 2, 1, 1)
        self.gridLayout_info.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum), 0, 3, 2, 1)
        self.lblPlacaTitle = QLabel(self.groupInfo)
        self.lblPlacaTitle.setObjectName(u"lblPlacaTitle")
        self.gridLayout_info.addWidget(self.lblPlacaTitle, 0, 4, 1, 1)
        self.lblPlaca = QLabel(self.groupInfo)
        self.lblPlaca.setObjectName(u"lblPlaca")
        self.gridLayout_info.addWidget(self.lblPlaca, 1, 4, 1, 1)
        self.gridLayout_info.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum), 0, 5, 2, 1)
        self.lblFormaTitle = QLabel(self.groupInfo)
        self.lblFormaTitle.setObjectName(u"lblFormaTitle")
        self.gridLayout_info.addWidget(self.lblFormaTitle, 0, 6, 1, 1)
        self.lblForma = QLabel(self.groupInfo)
        self.lblForma.setObjectName(u"lblForma")
        self.gridLayout_info.addWidget(self.lblForma, 1, 6, 1, 1)
        self.lblDataTitle = QLabel(self.groupInfo)
        self.lblDataTitle.setObjectName(u"lblDataTitle")
        self.gridLayout_info.addWidget(self.lblDataTitle, 2, 0, 1, 1)
        self.lblData = QLabel(self.groupInfo)
        self.lblData.setObjectName(u"lblData")
        self.gridLayout_info.addWidget(self.lblData, 3, 0, 1, 1)
        self.lblUnidadeTitle = QLabel(self.groupInfo)
        self.lblUnidadeTitle.setObjectName(u"lblUnidadeTitle")
        self.gridLayout_info.addWidget(self.lblUnidadeTitle, 2, 4, 1, 1)
        self.lblUnidade = QLabel(self.groupInfo)
        self.lblUnidade.setObjectName(u"lblUnidade")
        self.gridLayout_info.addWidget(self.lblUnidade, 3, 4, 1, 1)
        self.lblTipoTitle = QLabel(self.groupInfo)
        self.lblTipoTitle.setObjectName(u"lblTipoTitle")
        self.gridLayout_info.addWidget(self.lblTipoTitle, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupInfo)

        self.groupResumo = QGroupBox(relatorio)
        self.groupResumo.setObjectName(u"groupResumo")
        self.horizontalLayout_resumo = QHBoxLayout(self.groupResumo)
        self.horizontalLayout_resumo.setSpacing(0)
        self.horizontalLayout_resumo.setObjectName(u"horizontalLayout_resumo")

        for attr, title_attr in [
            ("vboxLayout", "lblDiasRodadosTitle"), ("vboxLayout1", "lblDiasParadosTitle"),
            ("vboxLayout2", "lblKmTotalTitle"),     ("vboxLayout3", "lblMediaDiariaTitle"),
            ("vboxLayout4", "lblMaiorDiaTitle"),
        ]:
            vbox = QVBoxLayout()
            vbox.setSpacing(6)
            setattr(self, attr, vbox)
            lbl_title = QLabel(self.groupResumo)
            lbl_title.setObjectName(title_attr)
            vbox.addWidget(lbl_title)
            setattr(self, title_attr, lbl_title)
            val_attr = title_attr.replace("Title", "")
            lbl_val = QLabel(self.groupResumo)
            lbl_val.setObjectName(val_attr)
            vbox.addWidget(lbl_val)
            setattr(self, val_attr, lbl_val)
            self.horizontalLayout_resumo.addLayout(vbox)
            if attr != "vboxLayout4":
                sep = QLabel(self.groupResumo)
                sep.setObjectName(f"sep_{attr}")
                self.horizontalLayout_resumo.addWidget(sep)

        self.horizontalLayout_resumo.addItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        )

        self.groupMotivos = QGroupBox(self.groupResumo)
        self.groupMotivos.setObjectName(u"groupMotivos")
        self.groupMotivos.setMinimumSize(QSize(180, 0))
        self.verticalLayout_motivos = QVBoxLayout(self.groupMotivos)
        self.verticalLayout_motivos.setContentsMargins(8, 8, 8, 8)
        self.listMotivos = QListWidget(self.groupMotivos)
        self.listMotivos.setObjectName(u"listMotivos")
        self.verticalLayout_motivos.addWidget(self.listMotivos)
        self.horizontalLayout_resumo.addWidget(self.groupMotivos)
        self.verticalLayout.addWidget(self.groupResumo)

        self.groupTabela = QGroupBox(relatorio)
        self.groupTabela.setObjectName(u"groupTabela")
        self.verticalLayout_tabela = QVBoxLayout(self.groupTabela)
        self.verticalLayout_tabela.setSpacing(0)
        self.verticalLayout_tabela.setContentsMargins(8, 8, 8, 8)
        self.tableDiario = QTableWidget(self.groupTabela)
        self.tableDiario.setColumnCount(6)
        for i, txt in enumerate(["Data", "Km Inicial", "Km Final", "Total do Dia", "Rodou?", "Motivo"]):
            self.tableDiario.setHorizontalHeaderItem(i, QTableWidgetItem())
        self.tableDiario.setObjectName(u"tableDiario")
        self.tableDiario.setAlternatingRowColors(True)
        self.tableDiario.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableDiario.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableDiario.setRowCount(0)
        self.verticalLayout_tabela.addWidget(self.tableDiario)
        self.verticalLayout.addWidget(self.groupTabela)

        self.horizontalLayout_acoes = QHBoxLayout()
        self.horizontalLayout_acoes.setSpacing(10)
        self.btnExportarPDF = QPushButton(relatorio)
        self.btnExportarPDF.setObjectName(u"btnExportarPDF")
        self.horizontalLayout_acoes.addWidget(self.btnExportarPDF)
        self.btnExportarExcel = QPushButton(relatorio)
        self.btnExportarExcel.setObjectName(u"btnExportarExcel")
        self.horizontalLayout_acoes.addWidget(self.btnExportarExcel)
        self.btnImprimir = QPushButton(relatorio)
        self.btnImprimir.setObjectName(u"btnImprimir")
        self.horizontalLayout_acoes.addWidget(self.btnImprimir)
        self.horizontalLayout_acoes.addItem(
            QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        )
        self.btnVoltar = QPushButton(relatorio)
        self.btnVoltar.setObjectName(u"btnVoltar")
        self.horizontalLayout_acoes.addWidget(self.btnVoltar)
        self.verticalLayout.addLayout(self.horizontalLayout_acoes)

        self.retranslateUi(relatorio)
        QMetaObject.connectSlotsByName(relatorio)

    def retranslateUi(self, relatorio):
        relatorio.setWindowTitle(QCoreApplication.translate("relatorio", u"Relatório de Quilometragem", None))
        self.groupFiltros.setTitle(QCoreApplication.translate("relatorio", u"Filtros", None))
        self.labelAmb.setText(QCoreApplication.translate("relatorio", u"Ambulância:", None))
        self.labelAno.setText(QCoreApplication.translate("relatorio", u"Data:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("relatorio", u"MM/yyyy", None))
        self.btnGerar.setText(QCoreApplication.translate("relatorio", u"Gerar Relatório", None))
        self.groupInfo.setTitle(QCoreApplication.translate("relatorio", u"Informações da Ambulância", None))

        _title_style = "color: #94a3b8; font-size: 11px; font-weight: 600; letter-spacing: 0.3px;"
        _val_style   = "font-weight: 700; font-size: 13px; color: #1e293b;"

        self.lblChassiTitle.setText("Chassi:")
        self.lblChassiTitle.setStyleSheet(_title_style)
        self.lblChassi.setText("-")
        self.lblChassi.setStyleSheet(_val_style)

        self.lblAnoTitle.setText("Ano:")
        self.lblAnoTitle.setStyleSheet(_title_style)
        self.lblAno.setText("-")
        self.lblAno.setStyleSheet(_val_style)

        self.lblPlacaTitle.setText("Placa:")
        self.lblPlacaTitle.setStyleSheet(_title_style)
        self.lblPlaca.setText("-")
        self.lblPlaca.setStyleSheet("font-weight: 700; font-size: 13px; color: #dc2626;")

        self.lblFormaTitle.setText("Forma de Aquisição:")
        self.lblFormaTitle.setStyleSheet(_title_style)
        self.lblForma.setText("-")
        self.lblForma.setStyleSheet(_val_style)

        self.lblDataTitle.setText("Data de Aquisição:")
        self.lblDataTitle.setStyleSheet(_title_style)
        self.lblData.setText("-")
        self.lblData.setStyleSheet(_val_style)

        self.lblUnidadeTitle.setText("Unidade (CNES):")
        self.lblUnidadeTitle.setStyleSheet(_title_style)
        self.lblUnidade.setText("-")
        self.lblUnidade.setStyleSheet(_val_style)

        self.lblTipoTitle.setText("")

        self.groupResumo.setTitle(QCoreApplication.translate("relatorio", u"Resumo do Mês", None))

        self.lblDiasRodadosTitle.setText("Dias rodados")
        self.lblDiasRodadosTitle.setStyleSheet(_title_style)
        self.lblDiasRodados.setText("0")
        self.lblDiasRodados.setStyleSheet("font-weight: 800; font-size: 22px; color: #16a34a;")

        self.lblDiasParadosTitle.setText("Dias parados")
        self.lblDiasParadosTitle.setStyleSheet(_title_style)
        self.lblDiasParados.setText("0")
        self.lblDiasParados.setStyleSheet("font-weight: 800; font-size: 22px; color: #dc2626;")

        self.lblKmTotalTitle.setText("Quilometragem total")
        self.lblKmTotalTitle.setStyleSheet(_title_style)
        self.lblKmTotal.setText("0 km")
        self.lblKmTotal.setStyleSheet("font-weight: 800; font-size: 22px; color: #dc2626;")

        self.lblMediaDiariaTitle.setText("Média por dia rodado")
        self.lblMediaDiariaTitle.setStyleSheet(_title_style)
        self.lblMediaDiaria.setText("0 km")
        self.lblMediaDiaria.setStyleSheet("font-weight: 800; font-size: 22px; color: #0284c7;")

        self.lblMaiorDiaTitle.setText("Maior km diário")
        self.lblMaiorDiaTitle.setStyleSheet(_title_style)
        self.lblMaiorDia.setText("0 km")
        self.lblMaiorDia.setStyleSheet("font-weight: 800; font-size: 22px; color: #d97706;")

        self.groupMotivos.setTitle(QCoreApplication.translate("relatorio", u"Motivos de parada", None))
        self.groupTabela.setTitle(QCoreApplication.translate("relatorio", u"Quilometragem Diária", None))

        headers = ["Data", "Km Inicial", "Km Final", "Total do Dia", "Rodou?", "Motivo"]
        for i, txt in enumerate(headers):
            self.tableDiario.horizontalHeaderItem(i).setText(txt)

        self.btnExportarPDF.setText("Exportar PDF")
        self.btnExportarExcel.setText("Exportar Excel")
        self.btnImprimir.setText("Imprimir")
        self.btnVoltar.setText("Voltar")