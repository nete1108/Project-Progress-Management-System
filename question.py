from PySide2.QtWidgets import QApplication, QDialog, QMessageBox
from PySide2.QtCore import Signal # 信号
from PySide2.QtGui import Qt, QIcon # 图标、窗体设置
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from PySide2.QtWidgets import QHeaderView
from main_body.ui_untitled_question import Ui_Dialog
import sys, os, sqlite3

class DetailWindow(QDialog, Ui_Dialog):
    detailSiganl = Signal(bool)

    def __init__(self):
        super(DetailWindow, self).__init__()
        self.setupUi(self)
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))

        # 设置窗体图标
        app_icon = QIcon('问题解答.ico')
        self.setWindowIcon(app_icon)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = DetailWindow()
    win_main.show()
    sys.exit(app.exec_())
