# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gl.ui'
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
        Dialog.resize(892, 787)
        icon = QIcon()
        icon.addFile(u"C:/Users/17844/Desktop/Python\u5927\u4f5c\u4e1a/\u9879\u76ee.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 1, 891, 785))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.label_Big_Title = QLabel(self.layoutWidget)
        self.label_Big_Title.setObjectName(u"label_Big_Title")
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Big_Title.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_Big_Title)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.verticalSpacer_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_18)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(10)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEdit_No = QLineEdit(self.layoutWidget)
        self.lineEdit_No.setObjectName(u"lineEdit_No")

        self.horizontalLayout.addWidget(self.lineEdit_No)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.lineEdit_Type = QLineEdit(self.layoutWidget)
        self.lineEdit_Type.setObjectName(u"lineEdit_Type")

        self.horizontalLayout_2.addWidget(self.lineEdit_Type)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.lineEdit_Name = QLineEdit(self.layoutWidget)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")
        self.lineEdit_Name.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_Name)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.horizontalSpacer_13 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.lineEdit_Start = QLineEdit(self.layoutWidget)
        self.lineEdit_Start.setObjectName(u"lineEdit_Start")

        self.horizontalLayout_11.addWidget(self.lineEdit_Start)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.horizontalSpacer_12 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.lineEdit_End = QLineEdit(self.layoutWidget)
        self.lineEdit_End.setObjectName(u"lineEdit_End")

        self.horizontalLayout_10.addWidget(self.lineEdit_End)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.horizontalSpacer_11 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)

        self.lineEdit_Completion_Progress = QLineEdit(self.layoutWidget)
        self.lineEdit_Completion_Progress.setObjectName(u"lineEdit_Completion_Progress")

        self.horizontalLayout_5.addWidget(self.lineEdit_Completion_Progress)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.lineEdit_People = QLineEdit(self.layoutWidget)
        self.lineEdit_People.setObjectName(u"lineEdit_People")

        self.horizontalLayout_8.addWidget(self.lineEdit_People)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.lineEdit_Money = QLineEdit(self.layoutWidget)
        self.lineEdit_Money.setObjectName(u"lineEdit_Money")

        self.horizontalLayout_7.addWidget(self.lineEdit_Money)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_12.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_15)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.horizontalSpacer_7 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.textEdit_Label = QTextEdit(self.layoutWidget)
        self.textEdit_Label.setObjectName(u"textEdit_Label")

        self.horizontalLayout_9.addWidget(self.textEdit_Label)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.horizontalSpacer_8 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.lineEdit_level = QLineEdit(self.layoutWidget)
        self.lineEdit_level.setObjectName(u"lineEdit_level")

        self.horizontalLayout_6.addWidget(self.lineEdit_level)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 1, 0, 1, 1)

        self.textEdit_Notes = QTextEdit(self.layoutWidget)
        self.textEdit_Notes.setObjectName(u"textEdit_Notes")

        self.gridLayout.addWidget(self.textEdit_Notes, 1, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout)


        self.horizontalLayout_14.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_19)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalSpacer_10 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_10)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_20)

        self.pButtonOk = QPushButton(self.layoutWidget)
        self.pButtonOk.setObjectName(u"pButtonOk")
        font2 = QFont()
        font2.setFamily(u"Agency FB")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.pButtonOk.setFont(font2)

        self.horizontalLayout_15.addWidget(self.pButtonOk)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_21)

        self.pButtonCancel = QPushButton(self.layoutWidget)
        self.pButtonCancel.setObjectName(u"pButtonCancel")
        font3 = QFont()
        font3.setFamily(u"Agency FB")
        font3.setPointSize(12)
        self.pButtonCancel.setFont(font3)

        self.horizontalLayout_15.addWidget(self.pButtonCancel)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_22)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1, 4, 891, 781))
        self.label.setPixmap(QPixmap(u":/\u80cc\u666f\u56fe1.png"))
        self.label.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u7ba1\u7406", None))
        self.label_Big_Title.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u7ba1\u7406", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u7f16\u53f7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u7c7b\u578b\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u540d\u79f0\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u65e5\u671f\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u7ed3\u675f\u65e5\u671f\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u5b8c\u6210\u8fdb\u5ea6\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u8d1f\u8d23\u4eba\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u9884\u7b97\u91d1\u989d\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u6807\u7b7e\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u7ea7\u522b\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8\uff1a", None))
        self.pButtonOk.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.pButtonCancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.label.setText("")
    # retranslateUi

