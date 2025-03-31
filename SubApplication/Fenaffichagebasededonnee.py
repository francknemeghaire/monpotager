#importation des lib
import os
import sys
#import sqlite3

#from PySide6.QtCore import QSize, Qt
#from PySide6.QtGui import QAction, QIcon
#from PySide6.QtWidgets import *
import sqlite3
#from PyQt6 import QtWidgets
#from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QMainWindow, QToolBar, QMenu, QTableWidget, QTableWidgetItem
from PyQt6.QtWidgets import QWidget, QGridLayout, QHBoxLayout

from SubApplication import FENresultatsrecherche
from package import requetesql, fonctions
from SubApplication import rechercheinternet


#creation de la class
class Affichagebasededonnee(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layoutPrincipal = QHBoxLayout(widget)
        layoutGauche = QGridLayout(widget)
        layoutPrincipal.addLayout(layoutGauche)

        # création d'un menu
        menu = self.menuBar()
        # création d'un toolbar
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(30, 30))
        self.addToolBar(toolbar)
        # bouton du toolbar
        TLBquit = QAction(QIcon(os.path.join("icons", "exit.png")), "Quitter", self)
        TLBquit.triggered.connect(self.close)
        toolbar.addAction(TLBquit)
        #listwidget avec menu contextuel?

        self.listeplante = QTableWidget()
        self.listeplante.setColumnCount(22)
        for colonne in range(22):
            self.listeplante.setColumnWidth(colonne, 150)
        self.listeplante.setHorizontalHeaderLabels(["id","Nom", "Envergure", "Hauteur", "Exposition", "Date de semis", "Date de plantation", "Durée de vie", "Type d'arrosage", "Type de sol", "Association", "Température de germination", "Type de plante", "Couleur", "Emplacement", "Feuillage persistant", "Mellifère", "Mois de floraison", "Mois de récolte", "Plante parfumée", "Plante vivace", "Chemin d'accès image"])
        self.listeplante.setSortingEnabled(True)
        self.loaddata()
        layoutGauche.addWidget(self.listeplante, 0, 0)
        self.listeplante.setSortingEnabled(True)
        self.listeplante.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.listeplante.customContextMenuRequested.connect(self.contextMenuEvent)
        # ajout du layout à widget
        widget.setLayout(layoutPrincipal)
        self.setCentralWidget(widget)
        self.resize(800, 800)

    def loaddata(self):
        connection = sqlite3.connect('plantes.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM plantes ORDER BY id'

        tablerow = 0
        results = cur.execute(sqlstr)
        self.listeplante.setRowCount(requetesql.tailledelabdd())
        for row in results:
            for colonnes in range(22):
                self.listeplante.setItem(tablerow, colonnes, QTableWidgetItem(str(row[colonnes])))
            tablerow += 1

    def contextMenuEvent(self, e):
        context = QMenu()
        action_recherche_internet = context.addAction("Recherche sur internet")
        action_recherche_internet.triggered.connect(self.recherchersurinternet)
        action_recherche_fiche = context.addAction("Rechercher/modifier la fiche")
        action_recherche_fiche.triggered.connect(self.modifierlafiche)

        context.addAction(action_recherche_internet)
        context.addAction(action_recherche_fiche)
        # context.addAction(QAction("impression de la fiche", self))
        context.exec(self.listeplante.mapToGlobal(e))

    # actions liées au choix du menu contextuel

    # selection de listeplante : self.listeplante.selectedItems()[0].text()
    def recherchersurinternet(self):
        self.FENrecherche = rechercheinternet.rechercheinternet(critere=self.listeplante.selectedItems()[0].text())
        self.FENrecherche.show()

    def modifierlafiche(self):
        #self.FENrecherchefiche = FENresultatsrecherche.FENresultatsrecherche(nomdelaplante=self.listeplante.selectedItems()[0].text())
        self.FENmodifierfiche = fonctions.modifierFichePlante(id=self.listeplante.item(self.listeplante.currentRow(), 0).text())
        self.FENmodifierfiche.show()

    def imprimerlafiche(self):
        pass