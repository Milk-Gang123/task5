import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QInputDialog, QDialog, QTableWidgetItem
from PyQt5 import uic


class Add(QMainWindow):
    def __init__(self, main):
        self.main = main
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.comboBox_2.addItems(['Очень слабая', 'Слабая', 'Средняя', 'Сильная', 'Очень сильная'])
        self.comboBox.addItems(['Молотый', 'В зернах'])
        self.pushButton.clicked.connect(self.run)

    def run(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        a = self.lineEdit.text()
        b = self.lineEdit_4.text()
        c = self.lineEdit_5.text()
        d = self.lineEdit_6.text() + 'г'
        e = self.comboBox_2.currentText()
        f = self.comboBox.currentText()
        res = list(cur.execute("SELECT id from data"))
        if self.lineEdit_2.text() != 'Создать новый':
            id = int(self.lineEdit_2.text())
        else:
            id = -1
            for i in res:
                if i[0] > id:
                    id = i[0]
            id += 1
        try:
            cur.execute(f"""DELETE FROM data WHERE id = {id}""")
            cur.execute(f"""INSERT INTO data(id, name_of_sort, degree_of_roasting, milled_or_in_grains, taste, price, volume_of_package)
             VALUES({id}, "{a}", "{e}", "{f}", "{b}", {c}, "{d}")""")
            con.commit()
        except Exception as e:
            print(e)
        self.main.create_table()