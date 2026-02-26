# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TELADELOGIN.UI'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(410, 531)
        palette = QPalette()
        brush = QBrush(QColor(43, 45, 49, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        gradient = QLinearGradient(0, 0, 1, 1)
        gradient.setSpread(QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(247, 241, 242, 255))
        gradient.setColorAt(1, QColor(240, 244, 248, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        gradient1 = QLinearGradient(0, 0, 1, 1)
        gradient1.setSpread(QGradient.Spread.PadSpread)
        gradient1.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(247, 241, 242, 255))
        gradient1.setColorAt(1, QColor(240, 244, 248, 255))
        brush2 = QBrush(gradient1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        gradient2 = QLinearGradient(0, 0, 1, 1)
        gradient2.setSpread(QGradient.Spread.PadSpread)
        gradient2.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(247, 241, 242, 255))
        gradient2.setColorAt(1, QColor(240, 244, 248, 255))
        brush3 = QBrush(gradient2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        gradient3 = QLinearGradient(0, 0, 1, 1)
        gradient3.setSpread(QGradient.Spread.PadSpread)
        gradient3.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(247, 241, 242, 255))
        gradient3.setColorAt(1, QColor(240, 244, 248, 255))
        brush4 = QBrush(gradient3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        gradient4 = QLinearGradient(0, 0, 1, 1)
        gradient4.setSpread(QGradient.Spread.PadSpread)
        gradient4.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(247, 241, 242, 255))
        gradient4.setColorAt(1, QColor(240, 244, 248, 255))
        brush5 = QBrush(gradient4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush5)
        gradient5 = QLinearGradient(0, 0, 1, 1)
        gradient5.setSpread(QGradient.Spread.PadSpread)
        gradient5.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(247, 241, 242, 255))
        gradient5.setColorAt(1, QColor(240, 244, 248, 255))
        brush6 = QBrush(gradient5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush6)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        gradient6 = QLinearGradient(0, 0, 1, 1)
        gradient6.setSpread(QGradient.Spread.PadSpread)
        gradient6.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(247, 241, 242, 255))
        gradient6.setColorAt(1, QColor(240, 244, 248, 255))
        brush7 = QBrush(gradient6)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush7)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        gradient7 = QLinearGradient(0, 0, 1, 1)
        gradient7.setSpread(QGradient.Spread.PadSpread)
        gradient7.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(247, 241, 242, 255))
        gradient7.setColorAt(1, QColor(240, 244, 248, 255))
        brush8 = QBrush(gradient7)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush8)
        gradient8 = QLinearGradient(0, 0, 1, 1)
        gradient8.setSpread(QGradient.Spread.PadSpread)
        gradient8.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(247, 241, 242, 255))
        gradient8.setColorAt(1, QColor(240, 244, 248, 255))
        brush9 = QBrush(gradient8)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        login.setPalette(palette)
        login.setStyleSheet(u"\n"
"QWidget#login {\n"
"  background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                              stop:0 #f7f1f2, stop:1 #f0f4f8);\n"
"  font-family: \"Segoe UI\", Arial;\n"
"  color: #2b2d31;\n"
"}\n"
"QFrame#card {\n"
"  background: BLACK;\n"
"  border: 1px solid #f0d5d9; /* borda com leve tom vermelho */\n"
"  border-radius: 12px;\n"
"}\n"
"QLabel#lblTitulo { font-size: 20px; font-weight: 800; color: #1f2328; }\n"
"QLabel#lblSubtitulo { font-size: 12px; color: #6b7280; }\n"
"\n"
"QLineEdit {\n"
"  background: #ffffff;\n"
"  border: 1px solid #cbd5e1;\n"
"  border-radius: 8px;\n"
"  padding: 6px 10px;\n"
"}\n"
"QLineEdit:focus { border-color: #e11d48; }\n"
"\n"
"QTextEdit {\n"
"  background: #fff5f5;\n"
"  border: 1px solid #ffc7c7;\n"
"  border-radius: 8px;\n"
"  padding: 6px;\n"
"  color: #7a2416;\n"
"}\n"
"\n"
"QPushButton { border: none; border-radius: 8px; padding: 10px 14px; font-weight: 700; }\n"
"QPushButton#btnEntrar {\n"
"  background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    "
                        "                          stop:0 #e11d48, stop:1 #be123c);\n"
"  color: #ffffff;\n"
"}\n"
"QPushButton#btnEntrar:hover { background: #cc143d; }\n"
"QPushButton#btnEntrar:pressed { background: #a50f33; }\n"
"\n"
"QPushButton#btnCadastrar {\n"
"  background: #f3f4f6;\n"
"  color: #111827;\n"
"  border: 1px solid #e5e7eb;\n"
"}\n"
"QPushButton#btnCadastrar:hover { background: #e5e7eb; }\n"
"QPushButton#btnCadastrar:pressed { background: #d1d5db; }\n"
"   ")
        self.rootLayout = QVBoxLayout(login)
        self.rootLayout.setSpacing(16)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setProperty(u"contentsMargins", QRect(24, 24, 24, 24))
        self.card = QFrame(login)
        self.card.setObjectName(u"card")
        palette1 = QPalette()
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush10)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush10)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush10)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush10)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush10)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush10)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush10)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush10)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush10)
        self.card.setPalette(palette1)
        self.card.setFrameShape(QFrame.NoFrame)
        self.cardLayout = QVBoxLayout(self.card)
        self.cardLayout.setSpacing(12)
        self.cardLayout.setObjectName(u"cardLayout")
        self.cardLayout.setProperty(u"contentsMargins", QRect(20, 20, 20, 20))
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setSpacing(4)
        self.titleLayout.setObjectName(u"titleLayout")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.titleLayout.addItem(self.verticalSpacer_8)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.titleLayout.addItem(self.verticalSpacer_9)

        self.lblTitulo = QLabel(self.card)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblTitulo.setAlignment(Qt.AlignCenter)

        self.titleLayout.addWidget(self.lblTitulo)

        self.lblSubtitulo = QLabel(self.card)
        self.lblSubtitulo.setObjectName(u"lblSubtitulo")
        self.lblSubtitulo.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.lblSubtitulo.setAlignment(Qt.AlignCenter)

        self.titleLayout.addWidget(self.lblSubtitulo)


        self.cardLayout.addLayout(self.titleLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.lblUsuario = QLabel(self.card)
        self.lblUsuario.setObjectName(u"lblUsuario")
        self.lblUsuario.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblUsuario)

        self.lineEdit = QLineEdit(self.card)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.lblSenha = QLabel(self.card)
        self.lblSenha.setObjectName(u"lblSenha")
        self.lblSenha.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblSenha)

        self.lineEdit_2 = QLineEdit(self.card)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(0, QFormLayout.ItemRole.FieldRole, self.verticalSpacer_7)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(1, QFormLayout.ItemRole.FieldRole, self.verticalSpacer_10)


        self.cardLayout.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.cardLayout.addItem(self.verticalSpacer_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.cardLayout.addItem(self.verticalSpacer_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.cardLayout.addItem(self.verticalSpacer_6)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(10)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setProperty(u"contentsMargins", QRect(0, 0, 0, 0))
        self.hLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.hLeft)

        self.btnEntrar = QPushButton(self.card)
        self.btnEntrar.setObjectName(u"btnEntrar")

        self.buttonsLayout.addWidget(self.btnEntrar)

        self.btnCadastrar = QPushButton(self.card)
        self.btnCadastrar.setObjectName(u"btnCadastrar")

        self.buttonsLayout.addWidget(self.btnCadastrar)

        self.hRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.hRight)


        self.cardLayout.addLayout(self.buttonsLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.cardLayout.addItem(self.verticalSpacer_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.cardLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.cardLayout.addItem(self.verticalSpacer)


        self.rootLayout.addWidget(self.card)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Login", None))
        self.lblTitulo.setText(QCoreApplication.translate("login", u"Bem-vindo!", None))
        self.lblSubtitulo.setText(QCoreApplication.translate("login", u"Acesse sua conta para continuar", None))
        self.lblUsuario.setText(QCoreApplication.translate("login", u"Usu\u00e1rio", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("login", u"Digite seu usu\u00e1rio", None))
        self.lblSenha.setText(QCoreApplication.translate("login", u"Senha", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("login", u"Digite sua senha", None))
        self.btnEntrar.setText(QCoreApplication.translate("login", u"Entrar", None))
        self.btnCadastrar.setText(QCoreApplication.translate("login", u"Cadastrar", None))
    # retranslateUi

