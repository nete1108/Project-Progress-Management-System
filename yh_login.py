from PySide2.QtWidgets import QApplication, QDialog, QMessageBox
from PySide2.QtCore import Signal # 信号
from PySide2.QtGui import Qt, QIcon # 图标、窗体设置
import sqlite3
import sys, os
from ui.ui_untitled_yh_dl import Ui_Dialog
from main import MainWindow


class YhWindow(QDialog, Ui_Dialog):
    # 定义一个信号，从子窗体向主窗体返回信号
    MainSiganl = Signal(bool)
    UserSignal = Signal(str)
    #################################
    # 子窗体初始化、声明信号、设置围标等
    def __init__(self):
        super(YhWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("用户登录")
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

        self.stuAction = None

        self.main_win = None


    def check_login_info(self):
        conn = sqlite3.connect(os.path.join(self.cur_dir, './data/user_password.db'))
        c = conn.cursor()

        user = self.lineEdit_yh_User.text()
        password = self.lineEdit_yh_Password.text()



        # print(user)
        # print(type(user))
        sql = f"select * from all_user where user_type='普通用户' and  username='{user}' and password='{password}'"
        cursor = c.execute(sql)
        result = cursor.fetchone()

        if result is None:
            QMessageBox.warning(self, '警告', '用户名或密码错误或为管理员用户！')
            self.lineEdit_yh_Password.clear()
            self.lineEdit_yh_Password.setFocus()
        else:
            self.MainSiganl.emit(True)
            self.main_win = MainWindow()
            self.main_win.show()
            self.accept()

            self.stuAction = user
            self.UserSignal.connect(self.main_win.yh_login_Signal)
            self.UserSignal.emit(self.stuAction)

        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    detail_win = YhWindow()
    detail_win.show()
    sys.exit(app.exec_())
