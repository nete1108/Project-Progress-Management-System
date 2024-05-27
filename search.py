from PySide2.QtWidgets import QApplication, QDialog, QMessageBox
from PySide2.QtCore import Signal # 信号
from PySide2.QtGui import Qt, QIcon # 图标、窗体设置
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from PySide2.QtWidgets import QHeaderView
import sys, os, sqlite3
from PySide2.QtGui import QIcon
from main_body.ui_search import Ui_Dialog

class DetailWindow(QDialog, Ui_Dialog):
    detailSiganl = Signal(bool)

    def __init__(self):
        super(DetailWindow, self).__init__()
        self.setupUi(self)
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))

        # 设置窗体图标
        app_icon = QIcon('选择.ico')
        self.setWindowIcon(app_icon)
        # self.setWindowFlags(
        #     Qt.WindowMinMaxButtonsHint |
        #     Qt.MSWindowsFixedSizeDialogHint
        # )

        self.actionName = None
        self.pButtonShow.clicked.connect(lambda: self.Show())
        self.pButtonSearch.clicked.connect(lambda: self.Search())
        self.comboBox_Type.currentIndexChanged.connect(lambda: self.Select())
        self.comboBox_Level.currentIndexChanged.connect(lambda: self.Select())

        self.lineEditsearch.setText('')           # 初始化搜索框
        # self.Show()
########################################################################################################################
# 关键字搜索
    def Search(self):
        _info = self.lineEditsearch.text().strip()
        try:
            db_file = os.path.join(self.cur_dir, './data/my_All_Projects.db')
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            sql = '''
                  select  Id, Type, Name, Start_date, End_date, Progress, Manager, Level, Remark 
                  from project 
                 WHERE Id || Type || Name || Start_date || End_date || Progress || Manager || Level || Remark
                    LIKE ? ;
                  '''
            stu = ('%' + _info + '%',)
            cur.execute(sql, stu)
            conn.commit()

            self.tableWidget.clearContents()  # 清空表格内容
            self.tableWidget.setRowCount(0)  # 清空表格行数

            row_index = 0
            while True:  # 使用True代替stu，因为查询结果为None时stu值为False，不能作为循环条件
                stu = cur.fetchone()
                if stu is None:  # 如果查询结果为None，退出循环
                    break
                self.tableWidget.insertRow(row_index)
                for col_index, data in enumerate(stu):
                    TblItem = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_index, col_index, TblItem)
                row_index += 1
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            conn.rollback()
        finally:
            cur.close()
            conn.close()
            cur = None
            conn = None
########################################################################################################################
# 下拉框搜索
    def Select(self):
        current_type = self.comboBox_Type.currentText()
        current_level = self.comboBox_Level.currentText()
        try:
            db_file = os.path.join(self.cur_dir, './data/my_All_Projects.db')
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()

            sql = '''
                  select  Id, Type, Name, Start_date, End_date, Progress, Manager, Level, Remark 
                    from project 
                  WHERE Type = ?  AND Level = ?
                  '''
            stu = (current_type, current_level)
            cur.execute(sql, stu)
            conn.commit()

            self.tableWidget.clearContents()  # 清空表格内容
            self.tableWidget.setRowCount(0)  # 清空表格行数

            row_index = 0
            while True:  # 使用True代替stu，因为查询结果为None时stu值为False，不能作为循环条件
                stu = cur.fetchone()
                if stu is None:  # 如果查询结果为None，退出循环
                    break
                self.tableWidget.insertRow(row_index)
                for col_index, data in enumerate(stu):
                    TblItem = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_index, col_index, TblItem)
                row_index += 1
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            conn.rollback()

        finally:
            cur.close()
            conn.close()
            cur = None
            conn = None
########################################################################################################################
# 显示项目
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
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = DetailWindow()
    win_main.show()
    sys.exit(app.exec_())