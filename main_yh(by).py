from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from PySide2.QtWidgets import QAbstractItemView, QLineEdit, QPushButton
import sys, os
from main_body.ui_yh_window import Ui_MainWindow as MainWin

from PySide2.QtWidgets import QHeaderView
import sqlite3

from PySide2.QtWidgets import QFileDialog, QMessageBox, QMenu
import chardet, csv

from PySide2.QtCore import Signal, Qt

from tkinter import *
from tkinter import messagebox

from Information_Of_Project import DetailWindow

from search import DetailWindow as Searchwind

from question import  DetailWindow as qwind

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
        # self.pButtonImport.clicked.connect(lambda: self.Import())
        self.pButtonWatch.clicked.connect(lambda: self.Watch())
        self.pButtonSelect.clicked.connect(lambda: self.Select())
        self.pButtonExport.clicked.connect(lambda: self.Export())


        self.gl_win = None
        

        self.stuAction = None

        self.actionTlbExit.triggered.connect(lambda: self.Close())
        self.actionTlbSelect.triggered.connect(lambda: self.Select())
        self.actionMenuExit.triggered.connect(lambda: self.Close())
        self.actionMenuOpen.triggered.connect(lambda: self.Import())
        self.actionTlbWatch.triggered.connect(lambda: self.Watch())
        self.actionquestion.triggered.connect(lambda: self.question())
        # self.Show()
        # self.pButtonshow.setVisible(False)

        self.tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectRows  # 行选
        )


########################################################################################################################
# 显示项目
    def Show(self):
        db_file = os.path.join(self.cur_dir, './data/my_All_Projects.db')
        try:
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
# # 导入项目
#     def Import(self):
#         opened_file = QFileDialog().getOpenFileName(
#             parent=self,
#             caption='选择要导入的文件',
#             dir=self.cur_dir,
#             filter='CSV文件(*.csv);;文本文件(*.txt)'
#         )
#         if len(opened_file[0]) > 0:
#             db_file = os.path.join(self.cur_dir, './data/all_projects.db')
#             try:
#                 conn = sqlite3.connect(db_file)
#                 cur = conn.cursor()
#                 sql = '''
#                       INSERT INTO project (Id, Type, Name, Start_date, End_date, Progress, Manager, Level, Remark)
#                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#                       '''
#                 data = open(opened_file[0], mode='rb').read()
#                 encoding = chardet.detect(data).get('encoding')
#                 with open(opened_file[0], mode='r', encoding=encoding) as f:
#                     csv_reader = csv.DictReader(f)
#                     rows = []
#                     for row in csv_reader:
#                         rows.append((row['项目编号'], row['项目类型'], row['项目名称'],
#                         row['开始日期'], row['结束日期'], row['完成进度'], row['负责人'],
#                         row['项目级别'], row['备注']))
#                     cur.executemany(sql, rows)
#                 conn.commit()
#                 QMessageBox.information(self, '消息', '导入成功！')
#             except Exception as e:
#                 conn.rollback()
#                 QMessageBox.critical(self, '错误', '导入失败！' + str(e))
#             finally:
#                 cur.close()
#                 conn.close()
#                 cur = None
#                 conn = None
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
# 查看当前项目
    def Watch(self):
        self.stuAction = 'Watch'
        selected_ranges = self.tableWidget.selectedRanges()

        if len(selected_ranges) > 1 or len(selected_ranges) == 0:
            QMessageBox.warning(self, '警告', '请选择一行')
            return

        self.gl_win = DetailWindow()
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
    def question(self):
        self.que_win = qwind()
        self.que_win.setModal(True)
        self.que_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = MainWindow()
    win_main.show()
    sys.exit(app.exec_())