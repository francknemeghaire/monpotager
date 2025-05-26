from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (QCalendarWidget, QGridLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QDialog, QMenu, QTableWidget, QTableWidgetItem)
import sqlite3
from package import requetesql

class Calendrier(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        #creation du calendrier
        self.OBJcalendrier = QCalendarWidget(self)
        self.OBJcalendrier.setMinimumDate(QDate.currentDate())
        self.OBJcalendrier.setMaximumDate(QDate(2054, 1, 1))
        self.dateselectionnee = QLabel(self)
        self.affichagedestaches = QLabel(self)
        self.listetaches = QTableWidget()
        self.listetaches.setColumnCount(5)
        self.listetaches.setHorizontalHeaderLabels(["id","Tâche", "Date", "Heure", "Description", "Priorité"])
        self.listetaches.setSortingEnabled(True)
        self.listetaches.setColumnWidth(0, 15)
        self.listetaches.setColumnWidth(1, 150)
        self.listetaches.setColumnWidth(2, 50)
        self.listetaches.setColumnWidth(3, 50)
        self.listetaches.setColumnWidth(4, 300)
        self.listetaches.setColumnWidth(5, 50)
        # creation bouton
        self.BTNquitter = QPushButton('Quitter', self)
        self.BTNquitter.clicked.connect(self.quitter)

        #configuration de l'interface
        layoutprincipal = QHBoxLayout(self)
        layoutgauche = QVBoxLayout(self)
        layoutdroit = QGridLayout(self)
        layoutprincipal.addLayout(layoutgauche)
        layoutprincipal.addLayout(layoutdroit)
        layoutgauche.addWidget(self.OBJcalendrier)
        layoutdroit.addWidget(self.dateselectionnee, 0, 0)
        layoutdroit.addWidget(self.affichagedestaches, 1, 0)
        layoutdroit.addWidget(self.listetaches, 2, 0)
        layoutdroit.addWidget(self.BTNquitter, 3, 0)

        #selection de date par clic de souris
        self.OBJcalendrier.selectionChanged.connect(self.selectiondate)
        self.resize(1280, 1024)
        self.setWindowTitle("Calendrier")
        self.setLayout(layoutprincipal)
        self.show()

    #code lié à la selection d'une date
    def selectiondate(self):
        date = self.OBJcalendrier.selectedDate()
        self.dateselectionnee.setText(date.toString("dd MMMM yy"))
        self.afficherlestaches(date.toString("dd/MM/yyyy"))

    # code lié à l'action des boutons
    def quitter(self):
        self.close()
    
    def contextMenuEvent(self, element):
        # Créez un menu contextuel
        menu = QMenu(self)
        # Ajoutez des actions au menu
        ajouttache = menu.addAction("Ajouter une tâche")
        ajouttache.triggered.connect(self.ajouttaches)
        supprimertache = menu.addAction("Supprimer une tâche")
        supprimertache.triggered.connect(self.supprimertaches)
        
        menu.addAction(ajouttache)
        menu.addAction(supprimertache)
        menu.exec(element.globalPos())
        
    def ajouttaches(self):
        print("Ajouter une tâche")
    
    def supprimertaches(self):
        print("Supprimer une tâche")
    
    def afficherlestaches(self, date):
        connection = sqlite3.connect("taches.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM taches WHERE date = (?)', (date,))
        taches = cursor.fetchall()
        #print(len(taches))
        if len(taches) == 0:
            self.affichagedestaches.setText("Aucune tâche à afficher")
        else:
            self.affichagedestaches.setText("Tâches à afficher : " + str(len(taches)))
            self.listetaches.setRowCount(len(taches))
            for i in range(len(taches)):
                for j in range(5):
                    self.listetaches.setItem(i, j, QTableWidgetItem(str(taches[i][j])))
                
        connection.close()
        # Affichez les tâches dans un widget ou une boîte de dialogue