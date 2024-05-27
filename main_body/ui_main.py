# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import picture_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1253, 840)
        icon = QIcon()
        icon.addFile(u":/\u767b\u5f55.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionMenuOpen = QAction(MainWindow)
        self.actionMenuOpen.setObjectName(u"actionMenuOpen")
        self.actionMenuExit = QAction(MainWindow)
        self.actionMenuExit.setObjectName(u"actionMenuExit")
        self.actionTlbExit = QAction(MainWindow)
        self.actionTlbExit.setObjectName(u"actionTlbExit")
        self.actionTlbAdd = QAction(MainWindow)
        self.actionTlbAdd.setObjectName(u"actionTlbAdd")
        self.actionTlbChange = QAction(MainWindow)
        self.actionTlbChange.setObjectName(u"actionTlbChange")
        self.actionMenuAdd = QAction(MainWindow)
        self.actionMenuAdd.setObjectName(u"actionMenuAdd")
        self.actionMenuChange = QAction(MainWindow)
        self.actionMenuChange.setObjectName(u"actionMenuChange")
        self.actionTlbExport = QAction(MainWindow)
        self.actionTlbExport.setObjectName(u"actionTlbExport")
        self.actionTlbSelect = QAction(MainWindow)
        self.actionTlbSelect.setObjectName(u"actionTlbSelect")
        self.actionquestion = QAction(MainWindow)
        self.actionquestion.setObjectName(u"actionquestion")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 1251, 51))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lineEditUser_Id = QLineEdit(self.layoutWidget)
        self.lineEditUser_Id.setObjectName(u"lineEditUser_Id")
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.lineEditUser_Id.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEditUser_Id)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 60, 1251, 701))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.layoutWidget1)
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

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.pButtonSelect = QPushButton(self.layoutWidget1)
        self.pButtonSelect.setObjectName(u"pButtonSelect")

        self.verticalLayout_3.addWidget(self.pButtonSelect)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pButtonAdd = QPushButton(self.layoutWidget1)
        self.pButtonAdd.setObjectName(u"pButtonAdd")

        self.verticalLayout_2.addWidget(self.pButtonAdd)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.pButtonchange = QPushButton(self.layoutWidget1)
        self.pButtonchange.setObjectName(u"pButtonchange")

        self.verticalLayout_2.addWidget(self.pButtonchange)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.pButtonExport = QPushButton(self.layoutWidget1)
        self.pButtonExport.setObjectName(u"pButtonExport")

        self.verticalLayout_2.addWidget(self.pButtonExport)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.pButtonImport = QPushButton(self.layoutWidget1)
        self.pButtonImport.setObjectName(u"pButtonImport")

        self.verticalLayout_2.addWidget(self.pButtonImport)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.pButtonshow = QPushButton(self.layoutWidget1)
        self.pButtonshow.setObjectName(u"pButtonshow")

        self.verticalLayout_2.addWidget(self.pButtonshow)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pButtonExit = QPushButton(self.layoutWidget1)
        self.pButtonExit.setObjectName(u"pButtonExit")

        self.verticalLayout_2.addWidget(self.pButtonExit)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1253, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAdd = QMenu(self.menubar)
        self.menuAdd.setObjectName(u"menuAdd")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionMenuOpen)
        self.menuFile.addAction(self.actionMenuExit)
        self.menuEdit.addAction(self.actionMenuAdd)
        self.menuEdit.addAction(self.actionMenuChange)
        self.menuHelp.addAction(self.actionquestion)
        self.toolBar.addAction(self.actionTlbExit)
        self.toolBar.addAction(self.actionTlbAdd)
        self.toolBar.addAction(self.actionTlbChange)
        self.toolBar.addAction(self.actionTlbExport)
        self.toolBar.addAction(self.actionTlbSelect)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u4e00\u89c8", None))
        self.actionMenuOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.actionMenuExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actionTlbExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7cfb\u7edf", None))
        self.actionTlbAdd.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u9879\u76ee", None))
        self.actionTlbChange.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u9879\u76ee", None))
        self.actionMenuAdd.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u9879\u76ee", None))
        self.actionMenuChange.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u9879\u76ee", None))
        self.actionTlbExport.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u9879\u76ee", None))
        self.actionTlbSelect.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u9879\u76ee", None))
        self.actionquestion.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u73b0\u9519\u8bef\uff1f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u8fdb\u5ea6\u7ba1\u7406", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u7c7b\u578b", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u540d\u79f0", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e5\u671f", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65e5\u671f", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u5b8c\u6210\u8fdb\u5ea6", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u8d1f\u8d23\u4eba", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u7ea7\u522b", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.pButtonSelect.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u9879\u76ee", None))
        self.pButtonAdd.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u9879\u76ee", None))
        self.pButtonchange.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u9879\u76ee", None))
        self.pButtonExport.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u9879\u76ee", None))
        self.pButtonImport.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u9879\u76ee", None))
        self.pButtonshow.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u9879\u76ee\u53ca\u6570\u636e", None))
        self.pButtonExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7cfb\u7edf", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menuAdd.setTitle("")
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

