from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from PySide2.QtWidgets import QAbstractItemView, QLineEdit, QPushButton
import sys, os
from main_body.ui_main import Ui_MainWindow as MainWin

from PySide2.QtWidgets import QHeaderView
import sqlite3

from PySide2.QtWidgets import QFileDialog, QMessageBox, QMenu
import chardet, csv

from PySide2.QtCore import Signal, Qt
from gl import DetailWindow as DetailWind

from search import DetailWindow as Searchwind

from tkinter import *
from tkinter import messagebox

from question import DetailWindow  as qwind

from control_user import MainWindow as conwind

from PySide2.QtGui import Qt, QIcon # 图标、窗体设置


class MainWindow(QMainWindow, MainWin):
    mainSignal = Signal(str, dict)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.cur_dir = os.path.dirname(os.path.abspath(__file__))

        # 设置窗体图标
        app_icon = QIcon('项目新.ico')
        self.setWindowIcon(app_icon)

        self.pButtonExit.clicked.connect(lambda: self.Close())
        self.pButtonshow.clicked.connect(lambda: self.Show())
        self.pButtonImport.clicked.connect(lambda: self.Import())

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gl_win = None
        self.pButtonAdd.clicked.connect(lambda: self.Project_Add())
        self.pButtonchange.clicked.connect(lambda: self.Project_Change())
        self.pButtonExport.clicked.connect(lambda: self.Export())
        self.pButtonSelect.clicked.connect(lambda: self.Select())

        self.stuAction = None
        self.YhName = None

        self.actionTlbExit.triggered.connect(lambda: self.Close())
        self.actionTlbAdd.triggered.connect(lambda: self.Project_Add())
        self.actionTlbChange.triggered.connect(lambda: self.Project_Change())
        self.actionTlbExport.triggered.connect(lambda: self.Export())
        self.actionTlbSelect.triggered.connect(lambda: self.Select())
        # self.tableWidget.setSelectionBehavior(
        #     QAbstractItemView.SelectRows  # 行选
        # )
        # self.tableWidget.setSelectionMode(
        #     QAbstractItemView.SingleSelection  # 单选
        # )


        self.actionMenuExit.triggered.connect(lambda: self.Close())
        self.actionMenuOpen.triggered.connect(lambda: self.Import())
        self.actionMenuAdd.triggered.connect(lambda: self.Project_Add())
        self.actionMenuChange.triggered.connect(lambda: self.Project_Change())
        self.actionquestion.triggered.connect(lambda: self.question())

        # self.Show()
        # self.pButtonshow.setVisible(False)

        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.menu_pop)

########################################################################################################################
# 显示all_projects的数据
    def Show(self, actionGl=False):
        db_file = os.path.join(self.cur_dir, './data/my_All_Projects.db')
        try:
            if actionGl == True:
                while self.tableWidget.rowCount() > 0:
                    self.tableWidget.removeRow(0)
                self.tableWidget.setRowCount(0)
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            sql = '''
                   select  Id, Type, Name, Start_date, End_date, Progress, Manager, Level, Remark
                   from project
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
########################################################################################################################
# 导入all_Projects的数据
    def Import(self):
        # 选择要导入的CSV文件
        csv_file, _ = QFileDialog.getOpenFileName(None, '选择 CSV 文件', '', 'CSV 文件(*.csv)')

        if not csv_file:
            return

        # 获取导入数据库路径
        # db_file, _ = QFileDialog.getOpenFileName(None, '选择数据库文件', '', 'SQLite 数据库(*.db *.sqlite)')
        db_file = os.path.join(self.cur_dir, './data/my_All_Projects.db')

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
                        'INSERT INTO project (Id, Type, Name, Start_date, End_date, Progress, Manager, Level, Remark) SELECT ?, ?, ?, ?, ?, ?, ?, ?, ? WHERE NOT EXISTS (SELECT 1 FROM project WHERE Id = ?)',
                        (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[0]))

            conn.commit()
            QMessageBox.information(None, '导入成功', '数据已成功导入到SQLite数据库中！')
        except Exception as e:
            conn.rollback()
            QMessageBox.warning(None, '导入失败', '导入过程中发生错误：{}'.format(str(e)))
        finally:
            cur.close()
            conn.close()

            # opened_file = QFileDialog().getOpenFileName(
        #     parent=self,
        #     caption='选择要导入的文件',
        #     dir=self.cur_dir,
        #     filter='CSV文件(*.csv);;文本文件(*.txt)'
        # )
        # if len(opened_file[0]) > 0:
        #     db_file = os.path.join(self.cur_dir, './data/all_projects.db')
        #     try:
        #         conn = sqlite3.connect(db_file)
        #         cur = conn.cursor()
        #         sql = '''
        #               INSERT INTO project (Id, Type, Name, Start_date, End_date, Progress, Manager, Level, Remark)
        #               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        #               '''
        #         data = open(opened_file[0], mode='rb').read()
        #         encoding = chardet.detect(data).get('encoding')
        #         with open(opened_file[0], mode='r', encoding=encoding) as f:
        #             csv_reader = csv.DictReader(f)
        #             rows = []
        #             for row in csv_reader:
        #                 rows.append((row['项目编号'], row['项目类型'], row['项目名称'],
        #                 row['开始日期'], row['结束日期'], row['完成进度'], row['负责人'],
        #                 row['项目级别'], row['备注']))
        #             cur.executemany(sql, rows)
        #         conn.commit()
        #         QMessageBox.information(self, '消息', '导入成功！')

                #self.db2screen()

            # except Exception as e:
            #     conn.rollback()
            #     QMessageBox.critical(self, '错误', '导入失败！' + str(e))
            # finally:
            #     cur.close()
            #     conn.close()
            #     cur = None
            #     conn = None
########################################################################################################################
# 添加项目
    def Project_Add(self):
        self.stuAction = 'Add'
        self.gl_win = DetailWind()
        self.gl_win.setModal(True)
        self.gl_win.show()
        self.mainSignal.connect(self.gl_win.handle_main_signal)
        self.mainSignal.emit(self.stuAction, None)
        self.gl_win.detailSiganl.connect(self.Show)
########################################################################################################################
# 修改项目
    def Project_Change(self):
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
########################################################################################################################
# 右键菜单
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
            self.Project_Add()
        elif actionName == actionEdit:
            self.Project_Change()
        elif actionName == actionDel:
            stu_People = stu['负责人']
            stu_No = stu['项目编号']
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
########################################################################################################################
# 右键菜单中的删除键所使用的功能
    def del_from_db(self, stu_No):
        conn, cur = None, None
        try:
            db_file = os.path.join(self.cur_dir, './data/my_All_Projects.db')
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            sql = '''
                    delete from project where Id = '{}'
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
########################################################################################################################
# 退出系统
    def Close(self):
        reply = QMessageBox.question(self,'关闭提示',"是否要退出界面?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        elif reply == QMessageBox.No:
            return
########################################################################################################################
# 导出项目
    def Export(self):
        # 选择要导出的数据库文件
        # db_file, _ = QFileDialog.getOpenFileName(None, '选择数据库文件', '', 'SQLite 数据库(*.db *.sqlite)')
        db_file = os.path.join(self.cur_dir, './data/my_All_Projects.db')

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
            cur.execute('SELECT * FROM project')
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
########################################################################################################################
# 搜索项目
    def Select(self):
        self.se_win = Searchwind()
        self.se_win.setModal(True)
        self.se_win.show()
#     def Select(self):
#         e = 0
#         root = Tk()
#         root.title("查询项目")
#         Label(root, text='输入项目编号:').grid(row=0, column=0)
#         e1 = Entry(root)
#         e1.grid(row=0, column=1, padx=10, pady=5)
#
#         def showData(e):
#             dept = str(e1.get())
#             db_file = os.path.join(self.cur_dir, './data/my_All_Projects.db')
#             conn = sqlite3.connect(db_file)
#             cur = conn.cursor()
#             sql = '''
#                     select  Id, Type, Name, Start_date, End_date, Progress, Manager, Level, Remark
#                     from project
#                     where Id = ?
#                   '''
#             cur.execute(sql, (dept,))
#             data = cur.fetchone()
#             if data:
#                 messagebox.showinfo("查询结果", "{}".format(data))
#             else:
#                 messagebox.showwarning("查询结果", "未查询到相关信息")
#
#             cur.close()
#             conn.close()
#
#         bTnOk = Button(text='查询')
#         bTnOk.grid(row=3, column=1)
#         bTnOk.bind("<Button-1>", showData)
#         mainloop()
########################################################################################################################
    def question(self):
        self.que_win = qwind()
        self.que_win.setModal(True)
        self.que_win.show()
########################################################################################################################
    def yh_login_Signal(self, yhActionName:str):
        self.YhName = yhActionName
        self.lineEditUser_Id.setText('欢迎！'+ self.YhName)
        # print(self.YhName)
        # print(type(self.YhName))
        conn = sqlite3.connect(os.path.join(self.cur_dir, './data/user_password.db'))
        c = conn.cursor()

        sql_add = f"select add_right from all_user where username='{self.YhName}'"
        sql_change = f"select change_right from all_user where username='{self.YhName}'"
        sql_import = f"select import_right from all_user where username='{self.YhName}'"
        sql_export = f"select export_right from all_user where username='{self.YhName}'"
        cursor_add = c.execute(sql_add)
        result_add = cursor_add.fetchone()                 # 返回元组，取第一个值
        # print(result_add[0])
        # print(type(result_add[0]))

        cursor_change = c.execute(sql_change)
        result_change = cursor_change.fetchone()

        cursor_import = c.execute(sql_import)
        result_import = cursor_import.fetchone()

        cursor_export = c.execute(sql_export)
        result_export = cursor_export.fetchone()

        if result_add[0] == 'F':
            self.pButtonAdd.setVisible(False)
        else:
            self.pButtonAdd.setVisible(True)

        if result_change[0] == 'F':
            self.pButtonchange.setVisible(False)
        else:
            self.pButtonchange.setVisible(True)

        if result_import[0] == 'F':
            self.pButtonImport.setVisible(False)
        else:
            self.pButtonImport.setVisible(True)

        if result_export[0] == 'F':
            self.pButtonAdd.setVisible(False)
        else:
            self.pButtonAdd.setVisible(True)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = MainWindow()
    win_main.show()
    sys.exit(app.exec_())