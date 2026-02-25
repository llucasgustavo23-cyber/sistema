# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TELAINICIA.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_telainicial(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 621)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_root = QVBoxLayout(self.centralwidget)
        self.verticalLayout_root.setSpacing(0)
        self.verticalLayout_root.setObjectName(u"verticalLayout_root")
        self.verticalLayout_root.setContentsMargins(0, 0, 0, 0)
        self.frameSamu = QFrame(self.centralwidget)
        self.frameSamu.setObjectName(u"frameSamu")
        self.frameSamu.setStyleSheet(u"#frameSamu {\n"
"    border-image: url(\"C:/Users/61348016/Downloads/samu.png\") 0 0 0 0 stretch stretch;\n"
"}")
        self.frameSamu.setFrameShape(QFrame.NoFrame)
        self.frameSamu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_frame = QVBoxLayout(self.frameSamu)
        self.verticalLayout_frame.setSpacing(0)
        self.verticalLayout_frame.setObjectName(u"verticalLayout_frame")
        self.verticalLayout_frame.setContentsMargins(64, 32, 64, 60)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_frame.addItem(self.verticalSpacer)

        self.horizontalLayout_row = QHBoxLayout()
        self.horizontalLayout_row.setSpacing(0)
        self.horizontalLayout_row.setObjectName(u"horizontalLayout_row")
        self.horizontalLayout_row.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_row.addItem(self.horizontalSpacer_2)

        self.homeBtn = QPushButton(self.frameSamu)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(160, 44))

        self.horizontalLayout_row.addWidget(self.homeBtn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_row.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_row.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_row.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_row.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_row.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_row.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_row.addItem(self.horizontalSpacer)


        self.verticalLayout_frame.addLayout(self.horizontalLayout_row)


        self.verticalLayout_root.addWidget(self.frameSamu)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TELAINICIAL", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
    # retranslateUi

