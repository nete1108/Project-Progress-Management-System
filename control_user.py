from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from PySide2.QtWidgets import QAbstractItemView, QLineEdit, QPushButton
import sys, os
from PySide2.QtWidgets import QHeaderView
import sqlite3
from PySide2.QtWidgets import QFileDialog, QMessageBox, QMenu
import chardet, csv
from PySide2.QtCore import Signal, Qt
from tkinter import *
from tkinter import messagebox
from PySide2.QtGui import Qt, QIcon # 图标、窗体设置
from main_body.ui_control_user import Ui_MainWindow
from control_gl import DetailWindow as DetailWind

class MainWindow(QMainWindow, Ui_MainWindow):
    mainSignal = Signal(str, dict)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.cur_dir = os.path.dirname(os.path.abspath(__file__))

        # 设置窗体图标
        app_icon = QIcon('项目新.ico')
        self.setWindowIcon(app_icon)

        self.pButtonExit.clicked.connect(lambda: self.Close())
        self.pButtonDisplay.clicked.connect(lambda: self.Show())

        self.user_win = None
        self.pButtonAdd.clicked.connect(lambda: self.User_Add())
        self.pButtonChange.clicked.connect(lambda: self.User_Change())
        self.pButtonSelect.clicked.connect(lambda: self.Select())
        self.pButtonImport.clicked.connect(lambda: self.Import())

        self.stuAction = None

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        self.actionTlbSearch.triggered.connect(lambda: self.Select())
        self.actionMenuopen.triggered.connect(lambda: self.Import())
        self.actionMenuExport.triggered.connect(lambda: self.Export())
        self.actionTlbAdd.triggered.connect(lambda: self.User_Add())
        self.actionTlbChange.triggered.connect(lambda: self.User_Change())
        # 右键菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.menu_pop)

    def Show(self, actionGl=False):
        db_file = os.path.join(self.cur_dir, './data/user_password.db')
        try:
            if actionGl == True:
                while self.tableWidget.rowCount() > 0:
                    self.tableWidget.removeRow(0)
                self.tableWidget.setRowCount(0)
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            sql = '''
                   select  *
                   from all_user
                  '''
            cur.execute(sql)
            stu = cur.fetchone()
            row_index = 0
            while stu:
                self.tableWidget.insertRow(row_index)
                for colIdx, data in enumerate(stu):
                    TblItem = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_index, colIdx, TblItem)
                stu = cur.fetchone()
                row_index = row_index + 1
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
            cur = None
            conn = None

# 添加用户
    def User_Add(self):
        self.stuAction = 'Add'
        self.gl_win = DetailWind()
        self.gl_win.setModal(True)
        self.gl_win.show()
        self.mainSignal.connect(self.gl_win.handle_main_signal)
        self.mainSignal.emit(self.stuAction, None)
        self.gl_win.detailSiganl.connect(self.Show)


# 修改用户
    def User_Change(self):
        self.stuAction = 'Change'
        selected_ranges = self.tableWidget.selectedRanges()

        if len(selected_ranges) > 1 or len(selected_ranges) == 0:
            QMessageBox.warning(self, '警告', '请选择一行')
            return

        self.gl_win = DetailWind()
        self.gl_win.setModal(True)
        self.gl_win.show()
        self.mainSignal.connect(self.gl_win.handle_main_signal)

        stu = {}
        current_row = self.tableWidget.currentRow()
        for c in range(self.tableWidget.columnCount()):
            item_data = self.tableWidget.item(current_row, c).text()
            item_name = self.tableWidget.horizontalHeaderItem(c).text()
            stu[item_name] = item_data

        self.mainSignal.emit(self.stuAction, stu)
        self.gl_win.detailSiganl.connect(self.Show)


# 退出系统
    def Close(self):
        reply = QMessageBox.question(self,'关闭提示',"是否要退出界面?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        elif reply == QMessageBox.No:
            return

    def Select(self):
        e = 0
        root = Tk()
        root.title("查询项目")
        Label(root, text='输入项目编号:').grid(row=0, column=0)
        e1 = Entry(root)
        e1.grid(row=0, column=1, padx=10, pady=5)

        def showData(e):
            dept = str(e1.get())
            db_file = os.path.join(self.cur_dir, './data/user_password.db')
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            sql = '''
                    select  user_type,username,password,login_times,last_login,add_right,change_right,
                    import_right,export_right
                    from all_user
                    where username = ?
                  '''
            cur.execute(sql, (dept,))
            data = cur.fetchone()
            if data:
                messagebox.showinfo("查询结果", "用户类型{},用户名{},用户密码{}\n登录次数{},上一次登录时间{}\n添加权限{},修改权限{},导入权限{},导出权限{}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))
            else:
                messagebox.showwarning("查询结果", "未查询到相关信息")

            cur.close()
            conn.close()

        bTnOk = Button(text='查询')
        bTnOk.grid(row=3, column=1)
        bTnOk.bind("<Button-1>", showData)
        mainloop()


    def Import(self):
        # 选择要导入的CSV文件
        csv_file, _ = QFileDialog.getOpenFileName(None, '选择 CSV 文件', '', 'CSV 文件(*.csv)')

        if not csv_file:
            return

        # 获取导入数据库路径
        # db_file, _ = QFileDialog.getOpenFileName(None, '选择数据库文件', '', 'SQLite 数据库(*.db *.sqlite)')
        db_file = os.path.join(self.cur_dir, './data/user_password.db')

        if not db_file:
            return

        try:
            # 连接数据库并创建表格
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            # cur.execute(
            #     'CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)')

            # 读取CSV文件并插入数据
            with open(csv_file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    cur.execute(
                        'INSERT INTO all_user (user_type,username,password,login_times,last_login) SELECT ?, ?, ?, ?, ? WHERE NOT EXISTS (SELECT 1 FROM all_user WHERE username = ?)',
                        (row[0], row[1], row[2], row[3], row[4], row[0]))

            conn.commit()
            QMessageBox.information(None, '导入成功', '数据已成功导入到SQLite数据库中！')
        except Exception as e:
            conn.rollback()
            QMessageBox.warning(None, '导入失败', '导入过程中发生错误：{}'.format(str(e)))
        finally:
            cur.close()
            conn.close()

    def Export(self):
        # 选择要导出的数据库文件
        # db_file, _ = QFileDialog.getOpenFileName(None, '选择数据库文件', '', 'SQLite 数据库(*.db *.sqlite)')
        db_file = os.path.join(self.cur_dir, './data/user_password.db')

        if not db_file:
            return

        # 获取导出路径
        csv_file, _ = QFileDialog.getSaveFileName(None, '保存 CSV 文件', '', 'CSV 文件(*.csv)')

        if not csv_file:
            return

        try:
            # 连接数据库并查询数据
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            cur.execute('SELECT * FROM all_user')
            data = cur.fetchall()

            # 将数据写入CSV文件
            with open(csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([i[0] for i in cur.description])  # 写入表头
                for row in data:
                    writer.writerow(row)

            QMessageBox.information(None, '导出成功', '数据已成功导出到CSV文件中！')
        except Exception as e:
            QMessageBox.warning(None, '导出失败', '导出过程中发生错误：{}'.format(str(e)))
        finally:
            cur.close()
            conn.close()


    def menu_pop(self, pos):
        row = self.tableWidget.currentRow()
        stu = {}
        for col in range(self.tableWidget.columnCount()):
            col_name = self.tableWidget.horizontalHeaderItem(col).text()
            col_value = self.tableWidget.item(row, col).text()
            stu[col_name] = col_value

        menu = QMenu()
        actionAdd = menu.addAction(u'添加')
        actionEdit = menu.addAction(u'编辑')
        actionDel = menu.addAction(u'删除')

        actionName = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if actionName == actionAdd:
            self.User_Add()
        elif actionName == actionEdit:
            self.User_Change()
        elif actionName == actionDel:
            stu_People = stu['用户名']
            stu_No = stu['用户密码']
            answer = QMessageBox.question(
                self,
                '确认删除',
                '是否删除{}行的项目'.format(row+1, stu_People),
                QMessageBox.Yes | QMessageBox.No
            )
            if answer == QMessageBox.No:
                return
            self.tableWidget.removeRow(row)
            self.del_from_db(stu_No)


    def del_from_db(self, stu_No):
        conn, cur = None, None
        try:
            db_file = os.path.join(self.cur_dir, './data/user_password.db')
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            sql = '''
                    delete from all_user where password = '{}'
                  '''.format(stu_No)
            cur.execute(sql)
            conn.commit()
            QMessageBox.information(
                self,
                '删除成功',
                '成功删除项目:{}!'.format(stu_No),
                QMessageBox.Ok
            )
        except Exception as e:
            conn.rollback()
            QMessageBox.critical(
                self,
                '删除失败！',
                str(e),
                QMessageBox.Ok
            )
        finally:
            cur.close()
            conn.close()
            cur = None
            conn = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = MainWindow()
    win_main.show()
    sys.exit(app.exec_())