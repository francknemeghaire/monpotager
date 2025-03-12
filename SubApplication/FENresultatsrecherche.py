import sys
import sqlite3
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PySide6.QtCore import Qt

from package import requetesql, fonctions



class FENresultatsrecherche(QDialog):
    def __init__(self):
        super().__init__()
        #self.nomdelaplante = nomdelaplante
        loadUi("SubApplication/AffichagePlantesBdd.ui",self)
        self.setWindowTitle("Résultats de la recherche")
        self.setGeometry(0,0,500,500)
        self.show()
        #affichage résultat recherche
        connection = sqlite3.connect("plantes.db")
        cursor = connection.cursor()
        #sqlstr = "select id, nom==self.nomdelaplante from plantes"
        sqlstr = 'SELECT * FROM plantes'
        cursor.execute(sqlstr)
        resultatrechercheplante = cursor.fetchall()

        tablerow = 0
        self.tableWidget.setRowCount(requetesql.tailledelabdd())
        for row in resultatrechercheplante:
            for colonnes in range(21):
                self.tableWidget.setItem(tablerow, colonnes, QtWidgets.QTableWidgetItem(str(row[colonnes])))
            tablerow += 1
        self.tableWidget.setSortingEnabled(True)
