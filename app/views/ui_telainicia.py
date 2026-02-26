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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_telainicia(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(961, 645)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameSamu = QFrame(Form)
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


        self.verticalLayout.addWidget(self.frameSamu)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.homeBtn.setText(QCoreApplication.translate("Form", u"LOGIN", None))
    # retranslateUi

