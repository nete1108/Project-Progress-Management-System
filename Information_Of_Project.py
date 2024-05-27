from PySide2.QtWidgets import QApplication, QDialog, QMessageBox
from PySide2.QtCore import Signal # 信号
from PySide2.QtGui import Qt, QIcon # 图标、窗体设置
import sys, os, sqlite3
from main_body.ui_information_of_projects import Ui_Dialog
from PySide2.QtGui import QIcon

class DetailWindow(QDialog, Ui_Dialog):
    detailSiganl = Signal(bool)

    def __init__(self):
        super(DetailWindow, self).__init__()
        self.setupUi(self)
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))

        # 设置窗体图标
        app_icon = QIcon('详情.ico')
        self.setWindowIcon(app_icon)

    def handle_main_signal(self, mainActionName:str, stu:dict):
        self.actionName = mainActionName
        if self.actionName == 'Watch':
            self.lineEdit_No.setText(stu['项目编号'])
            self.lineEdit_Type.setText(stu['项目类型'])
            self.lineEdit_Name.setText(stu['项目名称'])
            self.lineEdit_Start.setText(stu['开始日期'])
            self.lineEdit_End.setText(stu['结束日期'])
            self.lineEdit_Completion_Progress.setText(str(stu['完成进度']))
            self.lineEdit_People.setText(stu['负责人'])
            self.lineEdit_level.setText(stu['项目级别'])
            self.textEdit_Notes.setText(stu['备注'])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    detail_win = DetailWindow()
    detail_win.show()
    sys.exit(app.exec_())