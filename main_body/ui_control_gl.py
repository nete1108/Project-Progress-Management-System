# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'control_gl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(928, 602)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 40, 831, 341))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_big_title = QLabel(self.layoutWidget)
        self.label_big_title.setObjectName(u"label_big_title")
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_big_title.setFont(font)

        self.horizontalLayout.addWidget(self.label_big_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.user_type = QLineEdit(self.layoutWidget)
        self.user_type.setObjectName(u"user_type")

        self.horizontalLayout_2.addWidget(self.user_type)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.user_name = QLineEdit(self.layoutWidget)
        self.user_name.setObjectName(u"user_name")

        self.horizontalLayout_3.addWidget(self.user_name)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.user_password = QLineEdit(self.layoutWidget)
        self.user_password.setObjectName(u"user_password")

        self.horizontalLayout_4.addWidget(self.user_password)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.user_times = QLineEdit(self.layoutWidget)
        self.user_times.setObjectName(u"user_times")

        self.horizontalLayout_5.addWidget(self.user_times)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.user_last_time = QLineEdit(self.layoutWidget)
        self.user_last_time.setObjectName(u"user_last_time")

        self.horizontalLayout_6.addWidget(self.user_last_time)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(150, 500, 601, 30))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.pButtonOk = QPushButton(self.layoutWidget1)
        self.pButtonOk.setObjectName(u"pButtonOk")

        self.horizontalLayout_10.addWidget(self.pButtonOk)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.pButtonCancel = QPushButton(self.layoutWidget1)
        self.pButtonCancel.setObjectName(u"pButtonCancel")

        self.horizontalLayout_10.addWidget(self.pButtonCancel)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(170, 430, 671, 22))
        self.horizontalLayout_11 = QHBoxLayout(self.widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.checkBoxAdd = QCheckBox(self.widget)
        self.checkBoxAdd.setObjectName(u"checkBoxAdd")

        self.horizontalLayout_11.addWidget(self.checkBoxAdd)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.checkBoxChange = QCheckBox(self.widget)
        self.checkBoxChange.setObjectName(u"checkBoxChange")

        self.horizontalLayout_11.addWidget(self.checkBoxChange)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_16)

        self.checkBoxDelete = QCheckBox(self.widget)
        self.checkBoxDelete.setObjectName(u"checkBoxDelete")

        self.horizontalLayout_11.addWidget(self.checkBoxDelete)

        self.horizontalSpacer_17 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)

        self.checkBoxImport = QCheckBox(self.widget)
        self.checkBoxImport.setObjectName(u"checkBoxImport")

        self.horizontalLayout_11.addWidget(self.checkBoxImport)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7528\u6237\u7ba1\u7406", None))
        self.label_big_title.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u7ba1\u7406", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u7c7b\u578b", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u5bc6\u7801", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55\u6b21\u6570", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u6b21\u767b\u5f55\u65f6\u95f4", None))
        self.pButtonOk.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.pButtonCancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.checkBoxAdd.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        self.checkBoxChange.setText(QCoreApplication.translate("Dialog", u"\u4fee\u6539", None))
        self.checkBoxDelete.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664", None))
        self.checkBoxImport.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u5165", None))
    # retranslateUi

