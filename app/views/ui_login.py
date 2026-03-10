# -*- coding: utf-8 -*-

################################################################################
## ui_login.py — redesenhado para seguir o padrão visual da ui_relatorio
##               e ui_usuario (fundo #f0f4f8, card branco, accent #dc2626)
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget,
)

_STYLESHEET = u"""
/* ============================================================
   BASE
   ============================================================ */
QWidget#login {
    background-color: #f0f4f8;
    font-family: "Segoe UI", sans-serif;
    font-size: 15px;
    color: #1e293b;
}

/* ============================================================
   CARD
   ============================================================ */
QFrame#card {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
}

/* ============================================================
   HEADER  (faixa de accent no topo do card)
   ============================================================ */
QFrame#cardHeader {
    background-color: #dc2626;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
}

QLabel#lblTitulo {
    font-size: 22px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.5px;
}

QLabel#lblSubtitulo {
    font-size: 14px;
    font-weight: 400;
    color: rgba(255, 255, 255, 0.75);
}

/* ============================================================
   LABELS DOS CAMPOS
   ============================================================ */
QLabel#lblUsuario,
QLabel#lblSenha {
    background: transparent;
    color: #94a3b8;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.3px;
}

/* ============================================================
   INPUTS
   ============================================================ */
QLineEdit {
    background-color: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 9px 12px;
    font-size: 15px;
    color: #1e293b;
    min-height: 22px;
}

QLineEdit:focus {
    border-color: #dc2626;
    background-color: #ffffff;
}

/* ============================================================
   BOTÃO PRINCIPAL  (mesmo estilo de btnGerar / btnEntrar)
   ============================================================ */
QPushButton#btnEntrar {
    background-color: #dc2626;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 22px;
    font-size: 15px;
    font-weight: 600;
    min-height: 38px;
}

QPushButton#btnEntrar:hover   { background-color: #b91c1c; }
QPushButton#btnEntrar:pressed { background-color: #991b1b; }

/* ============================================================
   BOTÃO SECUNDÁRIO  (mesmo estilo de btnVoltar / btnCancelar)
   ============================================================ */
QPushButton#btnCadastrar {
    background-color: #ffffff;
    color: #64748b;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 22px;
    font-size: 13px;
    font-weight: 600;
    min-height: 36px;
}

QPushButton#btnCadastrar:hover {
    background-color: #f8fafc;
    color: #334155;
    border-color: #cbd5e1;
}

/* ============================================================
   DIVISOR
   ============================================================ */
QFrame#divider {
    background-color: #e2e8f0;
    border: none;
    max-height: 1px;
}
"""


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(440, 480)
        login.setStyleSheet(_STYLESHEET)

        # ── Layout raiz ────────────────────────────────────────────
        self.rootLayout = QVBoxLayout(login)
        self.rootLayout.setContentsMargins(40, 40, 40, 40)
        self.rootLayout.setSpacing(0)

        # centraliza verticalmente
        self.rootLayout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        )

        # ── CARD ───────────────────────────────────────────────────
        self.card = QFrame(login)
        self.card.setObjectName(u"card")
        self.card.setFrameShape(QFrame.NoFrame)

        self.cardLayout = QVBoxLayout(self.card)
        self.cardLayout.setContentsMargins(0, 0, 0, 0)
        self.cardLayout.setSpacing(0)

        # ── HEADER ─────────────────────────────────────────────────
        self.cardHeader = QFrame(self.card)
        self.cardHeader.setObjectName(u"cardHeader")
        self.cardHeader.setFrameShape(QFrame.NoFrame)
        self.cardHeader.setFixedHeight(110)

        self.headerLayout = QVBoxLayout(self.cardHeader)
        self.headerLayout.setContentsMargins(28, 20, 28, 20)
        self.headerLayout.setSpacing(4)

        self.lblTitulo = QLabel(self.cardHeader)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.headerLayout.addWidget(self.lblTitulo)

        self.lblSubtitulo = QLabel(self.cardHeader)
        self.lblSubtitulo.setObjectName(u"lblSubtitulo")
        self.lblSubtitulo.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.headerLayout.addWidget(self.lblSubtitulo)

        self.cardLayout.addWidget(self.cardHeader)

        # ── BODY ───────────────────────────────────────────────────
        self.cardBody = QFrame(self.card)
        self.cardBody.setObjectName(u"cardBody")
        self.cardBody.setFrameShape(QFrame.NoFrame)

        self.bodyLayout = QVBoxLayout(self.cardBody)
        self.bodyLayout.setContentsMargins(28, 24, 28, 24)
        self.bodyLayout.setSpacing(18)

        # ── Form ───────────────────────────────────────────────────
        self.formLayout = QFormLayout()
        self.formLayout.setLabelAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.formLayout.setHorizontalSpacing(16)
        self.formLayout.setVerticalSpacing(14)

        # Campo: Usuário
        self.lblUsuario = QLabel(self.cardBody)
        self.lblUsuario.setObjectName(u"lblUsuario")

        self.lineEdit = QLineEdit(self.cardBody)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        )

        self.formLayout.addRow(self.lblUsuario, self.lineEdit)

        # Campo: Senha
        self.lblSenha = QLabel(self.cardBody)
        self.lblSenha.setObjectName(u"lblSenha")

        self.lineEdit_2 = QLineEdit(self.cardBody)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        )

        self.formLayout.addRow(self.lblSenha, self.lineEdit_2)

        self.bodyLayout.addLayout(self.formLayout)

        # ── Divisor ────────────────────────────────────────────────
        self.divider = QFrame(self.cardBody)
        self.divider.setObjectName(u"divider")
        self.divider.setFrameShape(QFrame.HLine)
        self.bodyLayout.addWidget(self.divider)

        # ── Botões ─────────────────────────────────────────────────
        self.btnsLayout = QHBoxLayout()
        self.btnsLayout.setSpacing(10)

        self.btnEntrar = QPushButton(self.cardBody)
        self.btnEntrar.setObjectName(u"btnEntrar")

        self.btnsLayout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        )
        self.btnsLayout.addWidget(self.btnEntrar)

        self.bodyLayout.addLayout(self.btnsLayout)

        self.cardLayout.addWidget(self.cardBody)
        self.rootLayout.addWidget(self.card)

        self.rootLayout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        )

        self.retranslateUi(login)
        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(
            QCoreApplication.translate("login", u"Login", None)
        )
        self.lblTitulo.setText(
            QCoreApplication.translate("login", u"Bem-vindo!", None)
        )
        self.lblSubtitulo.setText(
            QCoreApplication.translate("login", u"Acesse sua conta para continuar", None)
        )
        self.lblUsuario.setText(
            QCoreApplication.translate("login", u"USUÁRIO", None)
        )
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("login", u"Digite seu usuário", None)
        )
        self.lblSenha.setText(
            QCoreApplication.translate("login", u"SENHA", None)
        )
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("login", u"Digite sua senha", None)
        )
        self.btnEntrar.setText(
            QCoreApplication.translate("login", u"Entrar", None)
        )
    # retranslateUi