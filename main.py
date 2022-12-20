# don't forget pip install mysql-connector-python
import sys
import mysql.connector
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
import webbrowser

class ConnectToSQL():
    def __init__(self):
        self.host = 'localhost'
        self.user = 'username'
        self.password = 'userpassword'
        self.port = '3306'
        self.database = 'catshop'
        self.con = None

    def connect(self):
        self.con = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database
        )

    def get_data_from_db(self):
        try:
            self.connect()
            cursor = self.con.cursor(dictionary=True)
            sql = "SELECT * FROM goods;"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

        except Exception as e:
            print('get data fail')
            print(e)

        finally:
            if self.con:
                self.con.close()

    def get_data_from_db1(self):
        try:
            self.connect()
            cursor = self.con.cursor(dictionary=True)
            sql = "SELECT * FROM orders;"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

        except Exception as e:
            print('get data fail')
            print(e)

        finally:
            if self.con:
                self.con.close()

    def get_data_from_db2(self):
        try:
            self.connect()
            cursor = self.con.cursor(dictionary=True)
            sql = "SELECT * FROM customers;"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

        except Exception as e:
            print('get data fail')
            print(e)

class GoodsWindow(QDialog):
    def __init__(self, parent=None):
        super(). __init__(parent)
        loadUi('Goods.ui', self)
        self.loaddata()

        self.btn.clicked.connect(self.SearchModel)
        self.btn_2.clicked.connect(self.SearchModel1)
        self.btn_3.clicked.connect(self.SearchModel2)
        self.btn_4.clicked.connect(self.SearchModel3)
        self.btn1.clicked.connect(self.close)

    def loaddata(self):
        result = ConnectToSQL().get_data_from_db()

        if result:
            self.tableGoods.setRowCount(len(result))

            for row, item in enumerate(result):
                column_1_item = QTableWidgetItem(str(item['id']))
                column_2_item = QTableWidgetItem(str(item['title']))
                column_3_item = QTableWidgetItem(str(item['kg']))
                column_4_item = QTableWidgetItem(str(item['price']))

                self.tableGoods.setItem(row, 0, column_1_item)
                self.tableGoods.setItem(row, 1, column_2_item)
                self.tableGoods.setItem(row, 2, column_3_item)
                self.tableGoods.setItem(row, 3, column_4_item)

    def SearchModel(self):
        name_search = self.lineId.text()
        for row in range(self.tableGoods.rowCount()):
            matching_items = self.tableGoods.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableGoods.item(row, 0)

                self.tableGoods.setRowHidden(row, name_search not in item.text().lower())

    def SearchModel1(self):
        name_search = self.lineTitle.text()
        for row in range(self.tableGoods.rowCount()):
            matching_items = self.tableGoods.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableGoods.item(row, 1)

                self.tableGoods.setRowHidden(row, name_search not in item.text().lower())

    def SearchModel2(self):
        name_search = self.lineKg.text()
        for row in range(self.tableGoods.rowCount()):
            matching_items = self.tableGoods.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableGoods.item(row, 2)

                self.tableGoods.setRowHidden(row, name_search not in item.text().lower())

    def SearchModel3(self):
        name_search = self.linePrice.text()
        for row in range(self.tableGoods.rowCount()):
            matching_items = self.tableGoods.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableGoods.item(row, 3)

                self.tableGoods.setRowHidden(row, name_search not in item.text().lower())

class OrdersWindow(QDialog):
    def __init__(self, parent=None):
        super(). __init__(parent)
        loadUi('Orders.ui', self)
        self.loaddata()

        self.btn.clicked.connect(self.SearchModel)
        self.btn_2.clicked.connect(self.SearchModel1)
        self.btn_3.clicked.connect(self.SearchModel2)
        self.btn_4.clicked.connect(self.SearchModel3)
        self.btn_5.clicked.connect(self.SearchModel4)
        self.btn_6.clicked.connect(self.SearchModel5)
        self.btn1.clicked.connect(self.close)

    def loaddata(self):
        result = ConnectToSQL().get_data_from_db1()

        if result:
            self.tableWidget.setRowCount(len(result))

            for row, item in enumerate(result):
                column_1_item = QTableWidgetItem(str(item['id']))
                column_2_item = QTableWidgetItem(str(item['ordernumber']))
                column_3_item = QTableWidgetItem(str(item['animalsid']))
                column_4_item = QTableWidgetItem(str(item['customersid']))
                column_5_item = QTableWidgetItem(str(item['goodsid']))
                column_6_item = QTableWidgetItem(str(item['date']))

                self.tableWidget.setItem(row, 0, column_1_item)
                self.tableWidget.setItem(row, 1, column_2_item)
                self.tableWidget.setItem(row, 2, column_3_item)
                self.tableWidget.setItem(row, 3, column_4_item)
                self.tableWidget.setItem(row, 4, column_5_item)
                self.tableWidget.setItem(row, 5, column_6_item)

    def SearchModel(self):
        name_search = self.lineId.text()
        for row in range(self.tableWidget.rowCount()):
            matching_items = self.tableWidget.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableWidget.item(row, 0)

                self.tableWidget.setRowHidden(row, name_search not in item.text().lower())

    def SearchModel1(self):
        name_search = self.lineOrd.text()
        for row in range(self.tableWidget.rowCount()):
            matching_items = self.tableWidget.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableWidget.item(row, 1)

                self.tableWidget.setRowHidden(row, name_search not in item.text().lower())

    def SearchModel2(self):
        name_search = self.lineAnim.text()
        for row in range(self.tableWidget.rowCount()):
            matching_items = self.tableWidget.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableWidget.item(row, 2)

                self.tableWidget.setRowHidden(row, name_search not in item.text().lower())

    def SearchModel3(self):
        name_search = self.lineCust.text()
        for row in range(self.tableWidget.rowCount()):
            matching_items = self.tableWidget.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableWidget.item(row, 3)

                self.tableWidget.setRowHidden(row, name_search not in item.text().lower())

    def SearchModel4(self):
        name_search = self.lineGood.text()
        for row in range(self.tableWidget.rowCount()):
            matching_items = self.tableWidget.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableWidget.item(row, 4)

                self.tableWidget.setRowHidden(row, name_search not in item.text().lower())

    def SearchModel5(self):
        name_search = self.lineDate.text()
        for row in range(self.tableWidget.rowCount()):
            matching_items = self.tableWidget.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableWidget.item(row, 5)

                self.tableWidget.setRowHidden(row, name_search not in item.text().lower())

class ProfilesWindow(QDialog):
    def __init__(self, parent=None):
        super(). __init__(parent)
        loadUi('Profiles.ui', self)
        self.loaddata()

        self.btn.clicked.connect(self.SearchModels)
        self.btn_2.clicked.connect(self.SearchModels1)
        self.btn_3.clicked.connect(self.SearchModels2)
        self.btn1.clicked.connect(self.close)

    def loaddata(self):
        result = ConnectToSQL().get_data_from_db2()

        if result:
            self.tableWidget.setRowCount(len(result))

            for row, item in enumerate(result):
                column_1_item = QTableWidgetItem(str(item['id']))
                column_2_item = QTableWidgetItem(str(item['name']))
                column_3_item = QTableWidgetItem(str(item['cell']))

                self.tableWidget.setItem(row, 0, column_1_item)
                self.tableWidget.setItem(row, 1, column_2_item)
                self.tableWidget.setItem(row, 2, column_3_item)

    def SearchModels(self):
        name_search = self.lineEdit.text()
        for row in range(self.tableWidget.rowCount()):
            matching_items = self.tableWidget.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableWidget.item(row, 0)

                self.tableWidget.setRowHidden(row, name_search not in item.text().lower())

    def SearchModels1(self):
        name_search = self.lineEdit_2.text()
        for row in range(self.tableWidget.rowCount()):
            matching_items = self.tableWidget.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableWidget.item(row, 1)

                self.tableWidget.setRowHidden(row, name_search not in item.text().lower())

    def SearchModels2(self):
        name_search = self.lineEdit_3.text()
        for row in range(self.tableWidget.rowCount()):
            matching_items = self.tableWidget.findItems(name_search, Qt.MatchContains)
            if matching_items:
                item = self.tableWidget.item(row, 2)

                self.tableWidget.setRowHidden(row, name_search not in item.text().lower())


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self). __init__()
        loadUi('MainWindow.ui', self)
        self.btn.clicked.connect(self.create_new_window)
        self.btn1.clicked.connect(self.create_new_window2)
        self.btn2.clicked.connect(self.create_new_window3)
        self.btn3.clicked.connect(QCoreApplication.instance().quit)
        self.btn4.clicked.connect(self.open_search)

    def create_new_window(self):
        self.MainWindow = GoodsWindow(self)
        self.MainWindow.show()

    def create_new_window2(self):
        self.MainWindow = OrdersWindow(self)
        self.MainWindow.show()

    def create_new_window3(self):
        self.MainWindow = ProfilesWindow(self)
        self.MainWindow.show()

    def open_search(url):
        webbrowser.open('https://www.google.com')

def application():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(600)
    widget.setFixedHeight(600)
    widget.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    application()