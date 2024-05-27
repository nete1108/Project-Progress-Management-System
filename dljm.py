from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ui.ui_untitled_login_select import Ui_MainWindow
from gly_login import GlyWindow as Gly
from yh_login import YhWindow as Yh
import os, sys
from PySide2.QtGui import Qt, QIcon # 图标、窗体设置



class LoginWindow(QMainWindow, Ui_MainWindow):
    mainSingnal = Signal(str, dict)
    # 初始化窗体
    def __init__(self):
        # 初始化基类
        super(LoginWindow, self).__init__()
        # 初始化当前窗体及窗体中的所有控件
        self.setupUi(self)
        # 记录当前应用所在路径
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))

        # 设置窗体图标
        app_icon = QIcon('选择.ico')
        self.setWindowIcon(app_icon)

        # 绑定信号与槽，实现按纽单击调用对应的槽函数(选择登录)
        # 声明子窗体(一个管理员登录，一个普通用户登录)
        self.gly_dl = None
        self.yh_dl = None
        self.pButtonadministrator.clicked.connect(lambda: self.gly())
        self.pButtonuser.clicked.connect(lambda: self.yh())

        # 绑定菜单栏(左上角的'退出系统'按钮）
        self.actionTlbExit.triggered.connect(lambda: self.Close())


    def gly(self):
        # 记录当前动作
        self.stuAction = 'gly_dl'
        # 创建子窗体
        self.gly_dl = Gly()
        # 设置该子窗体的对话框状态为“模态对话框”
        self.gly_dl.setModal(True)
        # 显示子窗体
        self.gly_dl.show()
        # # 信号与槽绑定
        # # 主窗体向子窗体发送数据（不能使用Lambda表达式，仅为窗体名.函数名）
        # self.mainSingnal.connect(self.gly_dl.handle_main_signal)
        # # 主窗体发射信号给子窗体
        # self.mainSignal.emit(self.stuAction)

    def yh(self):
        # 记录当前动作
        self.stuAction = 'yh_dl'
        # 创建子窗体()
        self.yh_dl = Yh()
        # 设置该子窗体的对话框状态为“模态对话框”
        self.yh_dl.setModal(True)
        # 显示子窗体
        self.yh_dl.show()
        # # 信号与槽绑定
        # # 主窗体向子窗体发送数据（不能使用Lambda表达式，仅为窗体名.函数名）
        # self.mainSingnal.connect(self.yh_dl.handle_main_signal)
        # # 主窗体发射信号给子窗体
        # self.mainSignal.emit(self.stuAction, None)

    def Close(self):
        reply = QMessageBox.question(self, '关闭提示', "是否要退出系统?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        elif reply == QMessageBox.No:
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = LoginWindow()
    win_main.show()
    sys.exit(app.exec_())

