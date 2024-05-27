from PySide2.QtWidgets import QApplication, QDialog, QMessageBox
from PySide2.QtCore import Signal # 信号
from PySide2.QtGui import Qt, QIcon # 图标、窗体设置
import sys, os, sqlite3
from main_body.ui_gl import Ui_Dialog
from PySide2.QtGui import QIcon

class DetailWindow(QDialog, Ui_Dialog):
    detailSiganl = Signal(bool)

    def __init__(self):
        super(DetailWindow, self).__init__()
        self.setupUi(self)
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))

        # self.setWindowFlags(
        #     Qt.WindowMinMaxButtonsHint |
        #     Qt.MSWindowsFixedSizeDialogHint
        # )

        self.actionName = None

        self.pButtonOk.clicked.connect(lambda: self.save2db())
        self.pButtonCancel.clicked.connect(lambda: self.close())

        # 设置窗体图标
        app_icon = QIcon('修改.ico')
        self.setWindowIcon(app_icon)


    def handle_main_signal(self, mainActionName:str, stu:dict):
        self.actionName = mainActionName
        if self.actionName == 'Add':
            self.label_Big_Title.setText('项目添加')
            self.pButtonOk.setText('添加')
            self.lineEdit_No.setText('')
            self.lineEdit_Type.setText('')
            self.lineEdit_Name.setText('')
            self.lineEdit_Start.setText('')
            self.lineEdit_End.setText('')
            self.lineEdit_Completion_Progress.setText('')
            self.lineEdit_People.setText('')
            self.lineEdit_level.setText('')
            self.textEdit_Notes.setText('')

        elif self.actionName == 'Change' and stu is not None:
            self.label_Big_Title.setText('项目修改')
            self.pButtonOk.setText('修改')
            self.lineEdit_No.setText(stu['项目编号'])
            self.lineEdit_Type.setText(stu['项目类型'])
            self.lineEdit_Name.setText(stu['项目名称'])
            self.lineEdit_Start.setText(stu['开始日期'])
            self.lineEdit_End.setText(stu['结束日期'])
            self.lineEdit_Completion_Progress.setText(str(stu['完成进度']))
            self.lineEdit_People.setText(stu['负责人'])
            self.lineEdit_level.setText(stu['项目级别'])
            self.textEdit_Notes.setText(stu['备注'])






    def save2db(self):
        _Id = self.lineEdit_No.text().strip()
        _Type = self.lineEdit_Type.text().strip()
        _Name = self.lineEdit_Name.text().strip()
        _Start = self.lineEdit_Start.text().strip()
        _End = self.lineEdit_End.text().strip()
        _Progress = self.lineEdit_Completion_Progress.text().strip()
        _People = self.lineEdit_People.text().strip()
        _Level = self.lineEdit_level.text().strip()
        _Note = self.textEdit_Notes.toPlainText().strip()

        if self.actionName == 'Add':
            try:
                db_file = os.path.join(self.cur_dir, './data/my_All_Projects.db')
                conn = sqlite3.connect(db_file)
                cur = conn.cursor()
                sql = """
                      INSERT INTO project (Id, Type, Name, Start_date, End_date, Progress, Manager, Level, Remark) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                      """
                stu = (_Id, _Type, _Name, _Start, _End, _Progress, _People, _Level, _Note)
                cur.execute(sql, stu)
                conn.commit()
                QMessageBox.information(self, '添加', '添加成功！')
                self.detailSiganl.emit(True)
            except Exception as e:
                conn.rollback()
                QMessageBox.critical(self, '错误', '添加失败！' + str(e))
                self.detailSiganl.emit(False)
            finally:
                self.close()
                cur.close()
                conn.close()
                cur = None
                conn = None

        elif self.actionName == 'Change':
            try:
                db_file = os.path.join(self.cur_dir, './data/my_All_Projects.db')
                conn = sqlite3.connect(db_file)
                cur = conn.cursor()
                sql = """
                      update project set Type='{0}',Name='{1}',Start_date='{2}',End_date='{3}',
                      Progress={4},Manager='{5}',Level='{6}',Remark='{7}' where Id='{8}'
                      """.format(_Type, _Name, _Start, _End, _Progress, _People, _Level, _Note, _Id)
                cur.execute(sql)
                conn.commit()
                QMessageBox.information(self, '修改', '修改成功！')
                self.detailSiganl.emit(True)
            except Exception as e:
                conn.rollback()
                QMessageBox.critical(self, '错误', '修改失败！' + str(e))
                self.detailSiganl.emit(False)
            finally:
                self.close()
                cur.close()
                conn.close()
                cur = None
                conn = None





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = DetailWindow()
    win_main.show()
    sys.exit(app.exec_())
