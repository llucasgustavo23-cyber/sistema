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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextEdit, QWidget)

class Ui_login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(432, 459)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush1)
        brush2 = QBrush(QColor(255, 255, 220, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 160, 261, 37))
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background: #d9d9d9;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    padding-right: 22px;              /* espa\u00e7o pro X */\n"
"    qproperty-clearButtonEnabled: true;\n"
"}\n"
"\n"
"QLineEdit::clear-button {\n"
"    image: url(:/icons/clear_14.png);  /* um PNG/SVG 14\u00d714 no .qrc */\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: center right;\n"
"    margin-right: 6px;\n"
"}\n"
"")
        self.lineEdit.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 70, 71, 61))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush1)
        brush3 = QBrush(QColor(208, 22, 9, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush3)
        brush4 = QBrush(QColor(255, 80, 68, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush4)
        brush5 = QBrush(QColor(231, 51, 38, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush5)
        brush6 = QBrush(QColor(104, 11, 4, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush6)
        brush7 = QBrush(QColor(139, 14, 6, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush7)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush1)
        brush8 = QBrush(QColor(231, 138, 132, 255))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush8)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush6)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush7)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush8)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush6)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush7)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush1)
        self.label.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"    color: BLACK;\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 140, 61, 16))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: Black;\n"
"}\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 220, 51, 16))
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: black\n"
";\n"
"}\n"
"")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 240, 261, 37))
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMouseTracking(True)
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    background: #d9d9d9;      /* cinza claro */\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"\n"
"    /* garante que o bot\u00e3o de limpar esteja ativo\n"
"       (no Designer funciona via qproperty) */\n"
"    qproperty-clearButtonEnabled: true;\n"
"\n"
"    /* espa\u00e7o para o bot\u00e3o n\u00e3o sobrepor o texto */\n"
"    padding-right: 22px;\n"
"}\n"
"\n"
"/* diminuir o X (clear-button) */\n"
"QLineEdit::clear-button {\n"
"    width: 14px;              /* tente 12\u201314\u201316 px */\n"
"    height: 14px;\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: center right;\n"
"    margin-right: 6px;        /* afasta do canto */\n"
"    background: transparent;  /* evita fundo estranho em alguns estilos */\n"
"}")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 30, 351, 371))
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush9 = QBrush(QColor(139, 0, 0, 255))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush9)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush9)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush9)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush9)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush1)
        self.textEdit.setPalette(palette2)
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    background: #8B0000;      /* vermelho escuro */\n"
"    border: 2px solid #8B0000;\n"
"    border-radius: 12px;\n"
"    padding: 8px;\n"
"    color: white;             /* texto branco para aparecer bem */\n"
"}\n"
"")
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(95, 310, 251, 41))
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #B30000;     /* vermelho mais claro */\n"
"    border: 2px solid #8B0000;     /* borda vermelho escuro */\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"\n"
"    font-family: Arial;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CC0000;     /* hover mais claro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #990000;     /* quando clicado */\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.textEdit.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Insira Aqui", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Senha :", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Insira Aqui", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
    # retranslateUi

