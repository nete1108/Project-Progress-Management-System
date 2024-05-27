# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled_gly_dl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import picture_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(814, 461)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 120, 811, 54))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.label_Login = QLabel(self.layoutWidget)
        self.label_Login.setObjectName(u"label_Login")
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_Login.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_Login)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.layoutWidget_2 = QWidget(Dialog)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 420, 811, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pButtonOk = QPushButton(self.layoutWidget_2)
        self.pButtonOk.setObjectName(u"pButtonOk")
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(10)
        self.pButtonOk.setFont(font1)

        self.horizontalLayout.addWidget(self.pButtonOk)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pButtonCancel = QPushButton(self.layoutWidget_2)
        self.pButtonCancel.setObjectName(u"pButtonCancel")
        self.pButtonCancel.setFont(font1)

        self.horizontalLayout.addWidget(self.pButtonCancel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.layoutWidget_3 = QWidget(Dialog)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 0, 811, 75))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.label = QLabel(self.layoutWidget_3)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Agency FB")
        font2.setPointSize(36)
        self.label.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.layoutWidget_4 = QWidget(Dialog)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 230, 811, 98))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget_4)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Agency FB")
        font3.setPointSize(14)
        self.label_3.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.lineEdit_gly_User = QLineEdit(self.layoutWidget_4)
        self.lineEdit_gly_User.setObjectName(u"lineEdit_gly_User")

        self.horizontalLayout_2.addWidget(self.lineEdit_gly_User)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.lineEdit_gly_Password = QLineEdit(self.layoutWidget_4)
        self.lineEdit_gly_Password.setObjectName(u"lineEdit_gly_Password")

        self.horizontalLayout_3.addWidget(self.lineEdit_gly_Password)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1, 4, 811, 461))
        self.label_5.setPixmap(QPixmap(u":/b2.png"))
        self.label_5.setScaledContents(True)
        self.label_5.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.layoutWidget_4.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7ba1\u7406\u5458\u767b\u5f55", None))
        self.label_Login.setText(QCoreApplication.translate("Dialog", u"\u7ba1\u7406\u5458\u767b\u5f55", None))
        self.pButtonOk.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.pButtonCancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u8fdb\u5ea6\u7ba1\u7406\u7cfb\u7edf", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d\uff1a", None))
        self.lineEdit_gly_User.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801\uff1a", None))
        self.label_5.setText("")
    # retranslateUi

