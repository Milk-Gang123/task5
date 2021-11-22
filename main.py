import sqlite3
import sys
from coffee_add import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QInputDialog, QDialog, QTableWidgetItem
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.add = Add(self)
        self.create_table()

    def create_table(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["id", "Название сорта", "степень прожарки", "молотый/в зернах", "описание вкуса",
                                                    "цена", "масса упаковки"])
        self.tableWidget.horizontalHeader().setDefaultSectionSize(152)
        self.tableWidget.setColumnWidth(0, 20)
        self.pushButton.clicked.connect(self.run)
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        coffes = sorted(list(cur.execute("SELECT * FROM data")), key=lambda x: x[0])
        for num_x, i in enumerate(coffes):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for num_y, j in enumerate(i):
                self.tableWidget.setItem(num_x, num_y, QTableWidgetItem(str(j)))

    def run(self):
        self.add.show()



app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())