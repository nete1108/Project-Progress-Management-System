from PySide2.QtWidgets import QApplication, QDialog, QMessageBox
from PySide2.QtCore import Signal # 信号
from PySide2.QtGui import Qt, QIcon # 图标、窗体设置
from PySide2.QtWidgets import QLineEdit, QPushButton
import sqlite3
import sys, os
from ui.ui_untitled_gly_dl import Ui_Dialog
from gly_select import GsWindow

class GlyWindow  (QDialog , Ui_Dialog):
    # 定义一个信号，从子窗体向主窗体返回信号
    MainSiganl = Signal(bool)
    # 子窗体初始化、声明信号、设置围标等
#############################################################################
    def __init__(self):
        super(GlyWindow, self).__init__()
        self.setupUi(self)
        # 记录当前应用程序路径
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))
        # 设置窗体图标
        app_icon = QIcon('登录配置.ico')
        self.setWindowIcon(app_icon)

        # 默认操作
        self.actionName = None
        # 按纽绑定
        self.pButtonCancel.clicked.connect(lambda: self.close())
        self.pButtonOk.clicked.connect(lambda: self.check_login_info())


    def check_login_info(self):
        conn = sqlite3.connect(os.path.join(self.cur_dir, './data/user_password.db'))
        c = conn.cursor()

        user = self.lineEdit_gly_User.text()
        password = self.lineEdit_gly_Password.text()

        sql = f"select * from all_user where user_type='管理员' and  username='{user}' and password='{password}'"
        cursor = c.execute(sql)
        result = cursor.fetchone()

        if result is None:
            QMessageBox.warning(self, '警告', '用户名或密码错误或非管理员用户！')
            self.lineEdit_gly_Password.clear()
            self.lineEdit_gly_Password.setFocus()
        else:
            self.MainSiganl.emit(True)
            main_window = GsWindow()
            main_window.show()
            self.accept()
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    detail_win = GlyWindow()
    detail_win.show()
    sys.exit(app.exec_())

