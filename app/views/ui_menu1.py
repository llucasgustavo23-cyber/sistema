# -*- coding: utf-8 -*-

################################################################################
## ui_menu1.py — redesenhado para seguir o padrão visual do sistema
##               sidebar escura + cards de ação no conteúdo principal
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QFrame, QGridLayout, QPushButton, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget,
)

_STYLESHEET = u"""
/* ============================================================
   BASE
   ============================================================ */
QWidget#Form {
    background-color: #f0f4f8;
    font-family: "Segoe UI", sans-serif;
    font-size: 15px;
    color: #1e293b;
}

/* ============================================================
   SIDEBAR
   ============================================================ */
QFrame#menuLateral {
    background-color: #7f1d1d;
    border: none;
    border-radius: 0px;
}

/* Logo/título da sidebar */
QLabel#lblAppName {
    color: #ffffff;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

QLabel#lblAppSub {
    color: rgba(255,255,255,0.45);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.3px;
}

/* Divisor da sidebar */
QFrame#sidebarDivider {
    background-color: rgba(255,255,255,0.10);
    border: none;
    max-height: 1px;
}

/* Botões da sidebar — estado normal */
QPushButton#btnInicio,
QPushButton#btnConfig,
QPushButton#pushButton {
    background-color: transparent;
    color: rgba(255,255,255,0.90);
    border: none;
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 14px;
    font-weight: 600;
    text-align: left;
}

QPushButton#btnInicio:hover,
QPushButton#btnConfig:hover,
QPushButton#pushButton:hover {
    background-color: rgba(255,255,255,0.08);
    color: #ffffff;
}

QPushButton#btnInicio:pressed,
QPushButton#btnConfig:pressed,
QPushButton#pushButton:pressed {
    background-color: rgba(79,70,229,0.35);
    color: #ffffff;
}

/* Botão ativo na sidebar */
QPushButton#btnInicio[active="true"] {
    background-color: #dc2626;
    color: #ffffff;
}

/* ============================================================
   ÁREA DE CONTEÚDO
   ============================================================ */
QFrame#contentArea {
    background-color: #f0f4f8;
    border: none;
}

/* ============================================================
   CARDS DE AÇÃO (botões grandes)
   ============================================================ */
QPushButton#btnCadastroAmb,
QPushButton#btnModificarAmb,
QPushButton#btnRelatorio,
QPushButton#btnInserirDados {
    background-color: #ffffff;
    color: #1e293b;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    font-size: 15px;
    font-weight: 700;
    padding: 16px;
}

QPushButton#btnCadastroAmb:hover,
QPushButton#btnModificarAmb:hover,
QPushButton#btnRelatorio:hover,
QPushButton#btnInserirDados:hover {
    background-color: #f8fafc;
    border-color: #dc2626;
    color: #dc2626;
}

QPushButton#btnCadastroAmb:pressed,
QPushButton#btnModificarAmb:pressed,
QPushButton#btnRelatorio:pressed,
QPushButton#btnInserirDados:pressed {
    background-color: #fee2e2;
    border-color: #dc2626;
}
"""


class Ui_menu(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1100, 660)
        Form.setStyleSheet(_STYLESHEET)

        # ── Layout raiz: sidebar | conteúdo ───────────────────────
        self.rootLayout = QGridLayout(Form)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)

        # ── SIDEBAR ───────────────────────────────────────────────
        self.menuLateral = QFrame(Form)
        self.menuLateral.setObjectName(u"menuLateral")
        self.menuLateral.setFixedWidth(200)
        self.menuLateral.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        )
        self.menuLateral.setFrameShape(QFrame.NoFrame)

        self.menuLayout = QVBoxLayout(self.menuLateral)
        self.menuLayout.setContentsMargins(12, 24, 12, 24)
        self.menuLayout.setSpacing(4)
        self.menuLayout.setObjectName(u"menuLayout")

        # — Logo ——————————————————————————————————————————————————
        self.lblAppName = QLabel(self.menuLateral)
        self.lblAppName.setObjectName(u"lblAppName")
        self.lblAppName.setContentsMargins(8, 0, 0, 0)
        self.menuLayout.addWidget(self.lblAppName)

        self.lblAppSub = QLabel(self.menuLateral)
        self.lblAppSub.setObjectName(u"lblAppSub")
        self.lblAppSub.setContentsMargins(8, 0, 0, 0)
        self.menuLayout.addWidget(self.lblAppSub)

        self.menuLayout.addSpacing(16)

        self.sidebarDivider = QFrame(self.menuLateral)
        self.sidebarDivider.setObjectName(u"sidebarDivider")
        self.sidebarDivider.setFrameShape(QFrame.HLine)
        self.menuLayout.addWidget(self.sidebarDivider)

        self.menuLayout.addSpacing(12)

        # — Botões da sidebar ————————————————————————————————————
        self.btnInicio = QPushButton(self.menuLateral)
        self.btnInicio.setObjectName(u"btnInicio")
        self.btnInicio.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        )
        self.btnInicio.setIconSize(QSize(18, 18))
        self.menuLayout.addWidget(self.btnInicio)

        self.btnConfig = QPushButton(self.menuLateral)
        self.btnConfig.setObjectName(u"btnConfig")
        self.btnConfig.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        )
        self.btnConfig.setIconSize(QSize(18, 18))
        self.menuLayout.addWidget(self.btnConfig)

        self.pushButton = QPushButton(self.menuLateral)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        )
        self.pushButton.setIconSize(QSize(18, 18))
        self.menuLayout.addWidget(self.pushButton)

        # espaçador empurra tudo para cima
        self.menuSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )
        self.menuLayout.addItem(self.menuSpacer)

        self.rootLayout.addWidget(self.menuLateral, 0, 0, 1, 1)

        # ── ÁREA DE CONTEÚDO ──────────────────────────────────────
        self.contentArea = QFrame(Form)
        self.contentArea.setObjectName(u"contentArea")
        self.contentArea.setFrameShape(QFrame.NoFrame)

        self.contentLayout = QVBoxLayout(self.contentArea)
        self.contentLayout.setContentsMargins(28, 28, 28, 28)
        self.contentLayout.setSpacing(20)

        # — Grid de cards ————————————————————————————————————————
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(16)
        self.gridLayout.setObjectName(u"gridLayout")

        self.btnCadastroAmb = QPushButton(self.contentArea)
        self.btnCadastroAmb.setObjectName(u"btnCadastroAmb")
        _expand = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.btnCadastroAmb.setSizePolicy(_expand)
        self.btnCadastroAmb.setIconSize(QSize(64, 64))
        self.gridLayout.addWidget(self.btnCadastroAmb, 0, 0, 1, 1)

        self.btnModificarAmb = QPushButton(self.contentArea)
        self.btnModificarAmb.setObjectName(u"btnModificarAmb")
        self.btnModificarAmb.setSizePolicy(_expand)
        self.btnModificarAmb.setIconSize(QSize(64, 64))
        self.gridLayout.addWidget(self.btnModificarAmb, 0, 1, 1, 1)

        self.btnRelatorio = QPushButton(self.contentArea)
        self.btnRelatorio.setObjectName(u"btnRelatorio")
        self.btnRelatorio.setSizePolicy(_expand)
        self.btnRelatorio.setIconSize(QSize(64, 64))
        self.gridLayout.addWidget(self.btnRelatorio, 1, 0, 1, 1)

        self.btnInserirDados = QPushButton(self.contentArea)
        self.btnInserirDados.setObjectName(u"btnInserirDados")
        self.btnInserirDados.setSizePolicy(_expand)
        self.btnInserirDados.setIconSize(QSize(64, 64))
        self.gridLayout.addWidget(self.btnInserirDados, 1, 1, 1, 1)

        self.contentLayout.addLayout(self.gridLayout)

        self.rootLayout.addWidget(self.contentArea, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate("Form", u"Sistema de Ambulâncias", None)
        )
        self.lblAppName.setText(
            QCoreApplication.translate("Form", u"Ambulâncias", None)
        )
        self.lblAppSub.setText(
            QCoreApplication.translate("Form", u"Sistema de Gestão", None)
        )
        self.btnInicio.setText(
            QCoreApplication.translate("Form", u"  Início", None)
        )
        self.btnConfig.setText(
            QCoreApplication.translate("Form", u"  Ajuste", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("Form", u"  Cadastrar Usuário", None)
        )
        self.btnCadastroAmb.setText(
            QCoreApplication.translate("Form", u"Cadastro de\nAmbulância", None)
        )
        self.btnModificarAmb.setText(
            QCoreApplication.translate("Form", u"Ambulâncias\nCadastradas", None)
        )
        self.btnRelatorio.setText(
            QCoreApplication.translate("Form", u"Relatório", None)
        )
        self.btnInserirDados.setText(
            QCoreApplication.translate("Form", u"Inserir Dados", None)
        )
    # retranslateUi