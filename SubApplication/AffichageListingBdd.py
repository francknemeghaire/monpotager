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
            for colonnes in range(12):
                self.tableWidget.setItem(tablerow, colonnes, QtWidgets.QTableWidgetItem(str(row[colonnes])))
            tablerow += 1
        self.tableWidget.setSortingEnabled(True)

class AffichageParNom(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listing des plantes de la base de données")
        loadUi("SubApplication/AffichagePlantesBdd.ui",self)
        nom = QInputDialog.getText(self, "Recherche par nom", "Nom de plante à rechercher")
        self.loaddata(nom[0])
        self.show()

    def loaddata(self, param):
        connection = sqlite3.connect('plantes.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM plantes WHERE nom = (?)'

        tablerow = 0
        results = cur.execute(sqlstr, (param,))
        self.tableWidget.setRowCount(40)
        for row in results:
            for colonnes in range(12):
                self.tableWidget.setItem(tablerow, colonnes, QtWidgets.QTableWidgetItem(str(row[colonnes])))
            tablerow += 1
        self.tableWidget.setSortingEnabled(True)

class AffichageParTaille(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listing des plantes de la base de données")
        loadUi("SubApplication/AffichagePlantesBdd.ui",self)
        nom = QInputDialog.getText(self, "Recherche par taille", "taille de plante à rechercher")
        self.loaddata(nom[0])
        self.show()

    def loaddata(self, param):
        connection = sqlite3.connect('plantes.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM plantes WHERE taille = (?)'

        tablerow = 0
        results = cur.execute(sqlstr, (param,))
        self.tableWidget.setRowCount(40)
        for row in results:
            for colonnes in range(12):
                self.tableWidget.setItem(tablerow, colonnes, QtWidgets.QTableWidgetItem(str(row[colonnes])))
            tablerow += 1
        self.tableWidget.setSortingEnabled(True)

class AffichageParAssociation(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listing des plantes de la base de données")
        loadUi("SubApplication/AffichagePlantesBdd.ui", self)
        nom = QInputDialog.getText(self, "Recherche par associations", "nom de plante à rechercher pour association")
        self.loaddata(nom[0])
        self.show()

    def loaddata(self, param):
        connection = sqlite3.connect('plantes.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM plantes WHERE association = (?)'
        tablerow = 0
        results = cur.execute(sqlstr, (param,))
        #association => colonne 10 => tuple !!!
        data = results.fetchall()
        # tri de data / param
        # sauvegarder le tri? avec sqlite? un tuple?
        #afficher les données triées
        self.tableWidget.setRowCount(40)
        for nbrchamp in range(0, len(data)):
            if data[nbrchamp][9] == param:
                for item in data:
                    for colonnes in range(12):
                        self.tableWidget.setItem(tablerow, colonnes, QtWidgets.QTableWidgetItem(str(item[colonnes])))
                    tablerow += 1
        self.tableWidget.setSortingEnabled(True)


class AffichageParSaison(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listing des plantes de la base de données")
        loadUi("SubApplication/AffichagePlantesBdd.ui", self)
        nom = QInputDialog.getText(self, "Recherche par saison de plantation", "Pour quelle saison faut-il faire une recherche?")
        self.loaddata(nom[0])
        self.show()

    def loaddata(self, param):
        connection = sqlite3.connect('plantes.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM plantes WHERE dateplantation = (?)'

        tablerow = 0
        results = cur.execute(sqlstr, (param,))
        self.tableWidget.setRowCount(40)
        for row in results:
            for colonnes in range(12):
                self.tableWidget.setItem(tablerow, colonnes, QtWidgets.QTableWidgetItem(str(row[colonnes])))
            tablerow += 1
        self.tableWidget.setSortingEnabled(True)