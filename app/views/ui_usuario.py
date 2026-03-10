# -*- coding: utf-8 -*-

################################################################################
## ui_usuario.py — redesenhado para seguir o padrão visual da ui_relatorio
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (
    QApplication, QFormLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QHBoxLayout, QWidget, QSpacerItem,
)

_STYLESHEET = u"""
/* ============================================================
   BASE — mesmo fundo e fonte da ui_relatorio
   ============================================================ */
QWidget#login {
    background-color: #f0f4f8;
    font-family: "Segoe UI", sans-serif;
    font-size: 13px;
    color: #1e293b;
}

/* ============================================================
   CARD CENTRAL
   ============================================================ */
QFrame#card {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
}

/* ============================================================
   HEADER DO CARD  (faixa roxa no topo)
   ============================================================ */
QFrame#cardHeader {
    background-color: #dc2626;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
}

QLabel#lblTitulo {
    font-size: 18px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.5px;
}

QLabel#lblSubtitulo {
    font-size: 12px;
    font-weight: 400;
    color: rgba(255,255,255,0.75);
}

/* ============================================================
   LABELS dos campos  — igual ao GroupBox da relatorio
   ============================================================ */
QLabel.fieldLabel {
    background: transparent;
    color: #94a3b8;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.3px;
}

/* ============================================================
   INPUTS — herda estilo da relatorio (QDateEdit / QComboBox)
   ============================================================ */
QLineEdit {
    background-color: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 9px 12px;
    font-size: 13px;
    color: #1e293b;
    min-height: 20px;
}

QLineEdit:focus {
    border-color: #dc2626;
    background-color: #ffffff;
}

QLineEdit:disabled {
    background-color: #f1f5f9;
    color: #94a3b8;
}

/* ============================================================
   BOTÃO PRINCIPAL — igual ao btnGerar da relatorio
   ============================================================ */
QPushButton#btnEntrar {
    background-color: #dc2626;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 22px;
    font-size: 13px;
    font-weight: 600;
    min-height: 36px;
}

QPushButton#btnEntrar:hover  { background-color: #b91c1c; }
QPushButton#btnEntrar:pressed { background-color: #991b1b; }

/* ============================================================
   BOTÃO SECUNDÁRIO — igual ao btnVoltar da relatorio
   ============================================================ */
QPushButton#btnCancelar {
    background-color: #ffffff;
    color: #64748b;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 22px;
    font-size: 13px;
    font-weight: 600;
    min-height: 36px;
}

QPushButton#btnCancelar:hover {
    background-color: #f8fafc;
    color: #334155;
    border-color: #cbd5e1;
}

/* ============================================================
   SEPARADOR
   ============================================================ */
QFrame#divider {
    background-color: #e2e8f0;
    border: none;
    max-height: 1px;
}
"""


class Ui_usuario(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(440, 520)
        login.setStyleSheet(_STYLESHEET)

        # ── Layout raiz ────────────────────────────────────────────
        self.rootLayout = QVBoxLayout(login)
        self.rootLayout.setContentsMargins(40, 40, 40, 40)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName(u"rootLayout")

        # ── CARD ───────────────────────────────────────────────────
        self.card = QFrame(login)
        self.card.setObjectName(u"card")
        self.card.setFrameShape(QFrame.NoFrame)

        self.cardLayout = QVBoxLayout(self.card)
        self.cardLayout.setContentsMargins(0, 0, 0, 0)
        self.cardLayout.setSpacing(0)
        self.cardLayout.setObjectName(u"cardLayout")

        # ── HEADER ─────────────────────────────────────────────────
        self.cardHeader = QFrame(self.card)
        self.cardHeader.setObjectName(u"cardHeader")
        self.cardHeader.setFrameShape(QFrame.NoFrame)
        self.cardHeader.setFixedHeight(88)

        self.headerLayout = QVBoxLayout(self.cardHeader)
        self.headerLayout.setContentsMargins(24, 18, 24, 18)
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
        self.bodyLayout.setContentsMargins(24, 24, 24, 24)
        self.bodyLayout.setSpacing(18)

        # ── FormLayout ─────────────────────────────────────────────
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(16)
        self.formLayout.setVerticalSpacing(14)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)

        # Campo: Usuário
        self.lblUsuario = QLabel(self.cardBody)
        self.lblUsuario.setObjectName(u"lblUsuario")
        self.lblUsuario.setProperty("class", "fieldLabel")

        self.lineEdit = QLineEdit(self.cardBody)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(self._body_font())

        self.formLayout.addRow(self.lblUsuario, self.lineEdit)

        # Campo: Senha
        self.lblSenha = QLabel(self.cardBody)
        self.lblSenha.setObjectName(u"lblSenha")
        self.lblSenha.setProperty("class", "fieldLabel")

        self.lineEdit_2 = QLineEdit(self.cardBody)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(self._body_font())
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

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

        self.btnCancelar = QPushButton(self.cardBody)
        self.btnCancelar.setObjectName(u"btnCancelar")

        self.btnEntrar = QPushButton(self.cardBody)
        self.btnEntrar.setObjectName(u"btnEntrar")

        spacer = QSpacerItem(20, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.btnsLayout.addItem(spacer)
        self.btnsLayout.addWidget(self.btnCancelar)
        self.btnsLayout.addWidget(self.btnEntrar)

        self.bodyLayout.addLayout(self.btnsLayout)

        self.cardLayout.addWidget(self.cardBody)
        self.rootLayout.addWidget(self.card)

        # ── Centraliza verticalmente ───────────────────────────────
        self.rootLayout.insertSpacerItem(
            0, QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        )
        self.rootLayout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        )

        self.retranslateUi(login)
        QMetaObject.connectSlotsByName(login)

    # ── Fonte do corpo ─────────────────────────────────────────────
    def _body_font(self) -> QFont:
        f = QFont()
        f.setPointSize(10)
        return f

    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(
            QCoreApplication.translate("login", u"Cadastrar Usuário", None)
        )
        self.lblTitulo.setText(
            QCoreApplication.translate("login", u"Cadastrar Usuário", None)
        )
        self.lblSubtitulo.setText(
            QCoreApplication.translate("login", u"Crie um usuário para continuar", None)
        )
        self.lblUsuario.setText(
            QCoreApplication.translate("login", u"USUÁRIO", None)
        )
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("login", u"Digite o usuário", None)
        )
        self.lblSenha.setText(
            QCoreApplication.translate("login", u"SENHA", None)
        )
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("login", u"Digite a senha", None)
        )
        self.btnEntrar.setText(
            QCoreApplication.translate("login", u"Cadastrar", None)
        )
        self.btnCancelar.setText(
            QCoreApplication.translate("login", u"Cancelar", None)
        )

    # retranslateUi