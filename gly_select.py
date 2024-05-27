from PySide2.QtWidgets import QApplication, QDialog, QMessageBox
from PySide2.QtCore import Signal # 信号
from PySide2.QtGui import Qt, QIcon # 图标、窗体设置
from PySide2.QtWidgets import QLineEdit, QPushButton
import sqlite3
import sys, os
from main_body.ui_gly_select import Ui_Dialog
from main import MainWindow as projectwindow
from control_user import MainWindow as userwindow

from PyQt5.QtWidgets import QApplication, QWidget

class GsWindow(QDialog , Ui_Dialog):
    MainSiganl = Signal(bool)

    def __init__(self):
        super(GsWindow, self).__init__()
        self.setupUi(self)
        # 记录当前应用程序路径
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))
        # 设置窗体图标
        app_icon = QIcon('登录配置.ico')
        self.setWindowIcon(app_icon)

        self.pButtonuser.clicked.connect(lambda: self.User())
        self.pButtonproject.clicked.connect(lambda: self.Project())

        self.setStyleSheet("background-image: url(b1.jpg);")

    def User(self):
        self.user_win = userwindow()
        self.user_win.show()

    def Project(self):
        self.pro_win = projectwindow()
        self.pro_win.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    detail_win = GsWindow()
    detail_win.show()
    sys.exit(app.exec_())
