# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'control_user.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1242, 687)
        self.actionTlbAdd = QAction(MainWindow)
        self.actionTlbAdd.setObjectName(u"actionTlbAdd")
        self.actionTlbChange = QAction(MainWindow)
        self.actionTlbChange.setObjectName(u"actionTlbChange")
        self.actionTlbSearch = QAction(MainWindow)
        self.actionTlbSearch.setObjectName(u"actionTlbSearch")
        self.actionMenuopen = QAction(MainWindow)
        self.actionMenuopen.setObjectName(u"actionMenuopen")
        self.actionMenuexport = QAction(MainWindow)
        self.actionMenuexport.setObjectName(u"actionMenuexport")
        self.actionMenuExport = QAction(MainWindow)
        self.actionMenuExport.setObjectName(u"actionMenuExport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1241, 611))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.pButtonSelect = QPushButton(self.layoutWidget)
        self.pButtonSelect.setObjectName(u"pButtonSelect")

        self.verticalLayout_3.addWidget(self.pButtonSelect)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pButtonDisplay = QPushButton(self.layoutWidget)
        self.pButtonDisplay.setObjectName(u"pButtonDisplay")

        self.verticalLayout.addWidget(self.pButtonDisplay)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pButtonChange = QPushButton(self.layoutWidget)
        self.pButtonChange.setObjectName(u"pButtonChange")

        self.verticalLayout.addWidget(self.pButtonChange)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pButtonAdd = QPushButton(self.layoutWidget)
        self.pButtonAdd.setObjectName(u"pButtonAdd")

        self.verticalLayout_2.addWidget(self.pButtonAdd)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.pButtonImport = QPushButton(self.layoutWidget)
        self.pButtonImport.setObjectName(u"pButtonImport")

        self.verticalLayout_2.addWidget(self.pButtonImport)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.pButtonExit = QPushButton(self.layoutWidget)
        self.pButtonExit.setObjectName(u"pButtonExit")

        self.verticalLayout_2.addWidget(self.pButtonExit)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1242, 26))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menufile.addAction(self.actionMenuopen)
        self.menufile.addAction(self.actionMenuExport)
        self.toolBar.addAction(self.actionTlbAdd)
        self.toolBar.addAction(self.actionTlbChange)
        self.toolBar.addAction(self.actionTlbSearch)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7ba1\u7406", None))
        self.actionTlbAdd.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.actionTlbChange.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.actionTlbSearch.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.actionMenuopen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.actionMenuexport.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.actionMenuExport.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7ba1\u7406", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7c7b\u578b", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u5bc6\u7801", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u6b21\u6570", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u6b21\u767b\u5f55\u65f6\u95f4", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None));
        self.pButtonSelect.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7528\u6237", None))
        self.pButtonDisplay.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u7528\u6237", None))
        self.pButtonChange.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u7528\u6237", None))
        self.pButtonAdd.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u7528\u6237", None))
        self.pButtonImport.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u7528\u6237", None))
        self.pButtonExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7cfb\u7edf", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

