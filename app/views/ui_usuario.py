# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastrodeusuario.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_usuario(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(420, 540)
        login.setStyleSheet(u"\n"
"QWidget#login {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #eceff4, stop:1 #d8dee9\n"
"    );\n"
"    font-family: \"Segoe UI\", Arial;\n"
"}\n"
"\n"
"/* ----- CARD ----- */\n"
"QFrame#card {\n"
"    background: rgba(255,255,255,0.90);\n"
"    border-radius: 16px;\n"
"    border: 1px solid #e5e7eb;\n"
"    padding: 18px;\n"
"}\n"
"\n"
"/* ----- TEXTOS ----- */\n"
"QLabel#lblTitulo {\n"
"    font-size: 22px;\n"
"    font-weight: 700;\n"
"    color: #1f2937;\n"
"}\n"
"QLabel#lblSubtitulo {\n"
"    font-size: 13px;\n"
"    color: #6b7280;\n"
"}\n"
"QLabel {\n"
"    font-size: 14px;\n"
"    color: #374151;\n"
"}\n"
"\n"
"/* ----- CAMPOS INPUT ----- */\n"
"QLineEdit {\n"
"    background: #ffffff;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #cbd5e1;\n"
"    padding: 8px 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4f46e5;\n"
"}\n"
"\n"
"/* ----- BOT\u00d5ES ----- */\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
""
                        "    font-size: 14px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"/* Bot\u00e3o principal */\n"
"QPushButton#btnEntrar {\n"
"    background-color: #4f46e5;\n"
"    color: white;\n"
"}\n"
"QPushButton#btnEntrar:hover {\n"
"    background-color: #4338ca;\n"
"}\n"
"QPushButton#btnEntrar:pressed {\n"
"    background-color: #372fbd;\n"
"}\n"
"   ")
        self.mainLayout = QVBoxLayout(login)
        self.mainLayout.setSpacing(20)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(32, 32, 32, 32)
        self.card = QFrame(login)
        self.card.setObjectName(u"card")
        self.card.setStyleSheet(u"background-color: rgb(144, 0, 0);")
        self.card.setFrameShape(QFrame.NoFrame)
        self.cardLayout = QVBoxLayout(self.card)
        self.cardLayout.setSpacing(14)
        self.cardLayout.setObjectName(u"cardLayout")
        self.cardLayout.setContentsMargins(20, 20, 20, 20)
        self.lblTitulo = QLabel(self.card)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblTitulo.setAlignment(Qt.AlignCenter)

        self.cardLayout.addWidget(self.lblTitulo)

        self.lblSubtitulo = QLabel(self.card)
        self.lblSubtitulo.setObjectName(u"lblSubtitulo")
        self.lblSubtitulo.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblSubtitulo.setAlignment(Qt.AlignCenter)

        self.cardLayout.addWidget(self.lblSubtitulo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(12)
        self.lblUsuario = QLabel(self.card)
        self.lblUsuario.setObjectName(u"lblUsuario")
        self.lblUsuario.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblUsuario)

        self.lineEdit = QLineEdit(self.card)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.lineEdit.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.lblSenha = QLabel(self.card)
        self.lblSenha.setObjectName(u"lblSenha")
        self.lblSenha.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblSenha)

        self.lineEdit_2 = QLineEdit(self.card)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_2)


        self.cardLayout.addLayout(self.formLayout)

        self.btnEntrar = QPushButton(self.card)
        self.btnEntrar.setObjectName(u"btnEntrar")
        self.btnEntrar.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.cardLayout.addWidget(self.btnEntrar)


        self.mainLayout.addWidget(self.card)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Login", None))
        self.lblTitulo.setText(QCoreApplication.translate("login", u"CADASTRAR USU\u00c1RIO", None))
        self.lblSubtitulo.setText(QCoreApplication.translate("login", u"Crie um usu\u00e1rio para continuar", None))
        self.lblUsuario.setText(QCoreApplication.translate("login", u"Usu\u00e1rio", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("login", u"Digite o usu\u00e1rio", None))
        self.lblSenha.setText(QCoreApplication.translate("login", u"Senha", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("login", u"Digite a senha", None))
        self.btnEntrar.setText(QCoreApplication.translate("login", u"Cadastrar", None))
    # retranslateUi

