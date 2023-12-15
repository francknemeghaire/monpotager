import sys
import sqlite3
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from package import requetesql

class AffichagelistingBdd(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listing des plantes de la base de données")
        loadUi("SubApplication/AffichagePlantesBdd.ui",self)
        self.loaddata()
        self.show()

    def loaddata(self):
        connection = sqlite3.connect('plantes.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM plantes LIMIT 40'

        tablerow = 0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(40)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            tablerow += 1