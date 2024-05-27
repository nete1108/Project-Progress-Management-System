from PySide2.QtWidgets import QApplication, QDialog, QMessageBox
from PySide2.QtCore import Signal # 信号
from PySide2.QtGui import Qt, QIcon # 图标、窗体设置
import sys, os, sqlite3
from main_body.ui_control_gl import Ui_Dialog
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

    def handle_main_signal(self, mainActionName: str, stu: dict):
        self.actionName = mainActionName
        if self.actionName == 'Add':
            self.label_big_title.setText("用户添加")
            self.pButtonOk.setText('添加')
            self.user_type.setText('')
            self.user_name.setText('')
            self.user_password.setText('')
            self.user_times.setText('')
            self.user_last_time.setText('')
            self.checkBoxAdd.setChecked(True)
            self.checkBoxChange.setChecked(True)
            self.checkBoxDelete.setChecked(True)
            self.checkBoxImport.setChecked(True)


        elif self.actionName == 'Change' and stu is not None:
            self.label_big_title.setText('用户修改')
            self.pButtonOk.setText('修改')
            self.user_type.setText(stu['用户类型'])
            self.user_name.setText(stu['用户名'])
            self.user_password.setText(stu['用户密码'])
            self.user_times.setText(stu['登录次数'])
            self.user_last_time.setText(stu['上一次登录时间'])
            if stu['添加'] == 'T':
                self.checkBoxAdd.setChecked(True)
            else:
                self.checkBoxAdd.setChecked(True)
            if stu['添加'] == 'T':
                self.checkBoxChange.setChecked(True)
            else:
                self.checkBoxChange.setChecked(True)
            if stu['添加'] == 'T':
                self.checkBoxDelete.setChecked(True)
            else:
                self.checkBoxDelete.setChecked(True)
            if stu['添加'] == 'T':
                self.checkBoxImport.setChecked(True)
            else:
                self.checkBoxImport.setChecked(True)


    def save2db(self):
        _type = self.user_type.text().strip()
        _name = self.user_name.text().strip()
        _password = self.user_password.text().strip()
        _times = self.user_times.text().strip()
        _last = self.user_last_time.text().strip()
        if self.checkBoxAdd.isChecked():
            _add = 'T'
        else:
            _add = 'F'
        if self.checkBoxChange.isChecked():
            _change = 'T'
        else:
            _change = 'F'
        if self.checkBoxDelete.isChecked():
            _delete = 'T'
        else:
            _delete = 'F'
        if self.checkBoxImport.isChecked():
            _import = 'T'
        else:
            _import = 'F'

        if self.actionName == 'Add':
            try:
                db_file = os.path.join(self.cur_dir, './data/user_password.db')
                conn = sqlite3.connect(db_file)
                cur = conn.cursor()
                sql = """
                      INSERT INTO all_user (user_type,username,password,login_times,last_login,add_right,change_right,
                    import_right,export_right) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                      """
                stu = (_type, _name, _password, _times, _last, _add, _change, _import,_delete )
                cur.execute(sql, stu)
                conn.commit()
                QMessageBox.information(self, '添加', '添加成功！')
                self.detailSiganl.emit(True)
            except Exception as e:
                conn.rollback()
                QMessageBox.critical(self, '错误', '添加失败！' + str(e))
                print(e)
                self.detailSiganl.emit(False)
            finally:
                self.close()
                cur.close()
                conn.close()
                cur = None
                conn = None

        elif self.actionName == 'Change':
            try:
                db_file = os.path.join(self.cur_dir, './data/user_password.db')
                conn = sqlite3.connect(db_file)
                cur = conn.cursor()
                sql = """
                      update all_user set user_type='{0}',password='{1}',login_times='{2}', last_login='{3}',add_right='{4}',
                      change_right='{5}',import_right='{6}',export_right='{7}'
                     where username='{8}'
                      """.format(_type, _password, _times, _last, _add, _change, _import,_delete, _name)
                cur.execute(sql)
                conn.commit()
                QMessageBox.information(self, '修改', '修改成功！')
                self.detailSiganl.emit(True)
            except Exception as e:
                conn.rollback()
                QMessageBox.critical(self, '错误', '修改失败！' + str(e))
                print(e)
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