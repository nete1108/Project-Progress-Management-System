# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
        Dialog.resize(1172, 733)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 1, 1171, 731))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pButtonShow = QPushButton(self.layoutWidget)
        self.pButtonShow.setObjectName(u"pButtonShow")

        self.horizontalLayout.addWidget(self.pButtonShow)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.lineEditsearch = QLineEdit(self.layoutWidget)
        self.lineEditsearch.setObjectName(u"lineEditsearch")

        self.horizontalLayout_4.addWidget(self.lineEditsearch)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.pButtonSearch = QPushButton(self.layoutWidget)
        self.pButtonSearch.setObjectName(u"pButtonSearch")

        self.horizontalLayout_4.addWidget(self.pButtonSearch)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.comboBox_Type = QComboBox(self.layoutWidget)
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.addItem("")
        self.comboBox_Type.setObjectName(u"comboBox_Type")

        self.horizontalLayout_2.addWidget(self.comboBox_Type)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.comboBox_Level = QComboBox(self.layoutWidget)
        self.comboBox_Level.addItem("")
        self.comboBox_Level.addItem("")
        self.comboBox_Level.addItem("")
        self.comboBox_Level.addItem("")
        self.comboBox_Level.addItem("")
        self.comboBox_Level.setObjectName(u"comboBox_Level")

        self.horizontalLayout_3.addWidget(self.comboBox_Level)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.tableWidget = QTableWidget(self.layoutWidget)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u67e5\u8be2", None))
        self.pButtonShow.setText(QCoreApplication.translate("Dialog", u"\u663e\u793a\u9879\u76ee", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u67e5\u8be2", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u5173\u952e\u5b57\uff1a", None))
        self.pButtonSearch.setText(QCoreApplication.translate("Dialog", u"\u641c\u7d22", None))
#if QT_CONFIG(shortcut)
        self.pButtonSearch.setShortcut(QCoreApplication.translate("Dialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u7c7b\u578b", None))
        self.comboBox_Type.setItemText(0, QCoreApplication.translate("Dialog", u"\u6280\u672f\u7814\u53d1", None))
        self.comboBox_Type.setItemText(1, QCoreApplication.translate("Dialog", u"\u5e02\u573a\u8425\u9500", None))
        self.comboBox_Type.setItemText(2, QCoreApplication.translate("Dialog", u"\u751f\u4ea7\u5236\u9020", None))
        self.comboBox_Type.setItemText(3, QCoreApplication.translate("Dialog", u"\u4eba\u529b\u8d44\u6e90", None))
        self.comboBox_Type.setItemText(4, QCoreApplication.translate("Dialog", u"\u8d22\u52a1\u7ba1\u7406", None))
        self.comboBox_Type.setItemText(5, QCoreApplication.translate("Dialog", u"\u8f6f\u4ef6\u5f00\u53d1", None))
        self.comboBox_Type.setItemText(6, QCoreApplication.translate("Dialog", u"\u7f51\u7edc\u8fd0\u7ef4", None))
        self.comboBox_Type.setItemText(7, QCoreApplication.translate("Dialog", u"\u54a8\u8be2\u670d\u52a1", None))
        self.comboBox_Type.setItemText(8, QCoreApplication.translate("Dialog", u"\u5e02\u573a\u8c03\u7814", None))
        self.comboBox_Type.setItemText(9, QCoreApplication.translate("Dialog", u"\u57f9\u8bad\u670d\u52a1", None))
        self.comboBox_Type.setItemText(10, QCoreApplication.translate("Dialog", u"\u6d3b\u52a8\u7b56\u5212", None))
        self.comboBox_Type.setItemText(11, QCoreApplication.translate("Dialog", u"\u7269\u6d41\u914d\u9001", None))
        self.comboBox_Type.setItemText(12, QCoreApplication.translate("Dialog", u"\u8d22\u52a1\u5ba1\u8ba1", None))
        self.comboBox_Type.setItemText(13, QCoreApplication.translate("Dialog", u"\u73af\u5883\u76d1\u6d4b", None))
        self.comboBox_Type.setItemText(14, QCoreApplication.translate("Dialog", u"\u6cd5\u5f8b\u54a8\u8be2", None))

        self.comboBox_Type.setCurrentText(QCoreApplication.translate("Dialog", u"\u6280\u672f\u7814\u53d1", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u7ea7\u522b", None))
        self.comboBox_Level.setItemText(0, QCoreApplication.translate("Dialog", u"A", None))
        self.comboBox_Level.setItemText(1, QCoreApplication.translate("Dialog", u"B", None))
        self.comboBox_Level.setItemText(2, QCoreApplication.translate("Dialog", u"C", None))
        self.comboBox_Level.setItemText(3, QCoreApplication.translate("Dialog", u"D", None))
        self.comboBox_Level.setItemText(4, QCoreApplication.translate("Dialog", u"E", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u7c7b\u578b", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u540d\u79f0", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u65e5\u671f", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u7ed3\u675f\u65e5\u671f", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u5b8c\u6210\u8fdb\u5ea6", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"\u8d1f\u8d23\u4eba", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u7ea7\u522b", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8", None));
    # retranslateUi

