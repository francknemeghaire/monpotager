import os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sqlite3
from package import requetesql


class Taches():
    # création d'une classe "taches" pour l'ajout de taches
    def __init__(self):
        self.nom = ""
        self.date = ""
        self.heure = ""
        self.description = ""
        self.priorite = 0
        
tachesajoutees = Taches()
TMPtachesajoutee = []

class GestionDesTaches(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des Tâches")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        # Initialisation de l'interface utilisateur
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.id = 0

        # Ajout de champs pour la saisie de tâches
        self.tache_input = QLineEdit()
        self.tache_input.setPlaceholderText("Entrez une tâche")
        self.layout.addWidget(self.tache_input)
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        self.layout.addWidget(self.date_input)
        self.heure_input = QTimeEdit()
        self.heure_input.setTime(QTime.currentTime())
        self.layout.addWidget(self.heure_input)
        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Description de la tâche")
        self.layout.addWidget(self.description_input)
        self.priorite_input = QSpinBox()
        self.legendepriorite = QLabel("Niveau de priorité")
        self.priorite_input.setRange(1, 5)
        self.priorite_input.setValue(3)
        self.layout.addWidget(self.legendepriorite)
        self.layout.addWidget(self.priorite_input)
        self.listetaches = QTableWidget()
        self.listetaches.setColumnCount(5)
        self.listetaches.setHorizontalHeaderLabels(["id","Tâche", "Date", "Heure", "Description", "Priorité"])
        self.listetaches.setSortingEnabled(True)
        self.listetaches.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.listetaches.customContextMenuRequested.connect(self.contextMenuEvent)
        self.afficher_taches()
        self.layout.addWidget(self.listetaches)
        
        # Ajout d'un bouton pour ajouter une tâche
        self.add_task_button = QPushButton("Ajouter une tâche")
        self.add_task_button.clicked.connect(self.ajouter_tache)
        self.BTNmodifier = QPushButton("Modifier une tâche")
        self.BTNmodifier.clicked.connect(self.encodage_tache_modifiee)
        self.layout.addWidget(self.add_task_button)
        self.layout.addWidget(self.BTNmodifier)
        
    def ajouter_tache(self):
        # Fonction pour ajouter une tâche à la base de données
        TMPtachesajoutee.append((self.tache_input.text(), self.date_input.date().toString("dd/MM/yyyy"), self.heure_input.time().toString("HH:mm"), self.description_input.toPlainText(), self.priorite_input.value()))
        requetesql.maj_bdd_taches(TMPtachesajoutee)
        TMPtachesajoutee.clear()
        self.tache_input.clear()
        self.description_input.clear()
        self.priorite_input.setValue(3)
        self.date_input.setDate(QDate.currentDate())
        self.heure_input.setTime(QTime.currentTime())
        QMessageBox.information(self, "Tâche ajoutée", "La tâche a été ajoutée avec succès.")
        # Rafraîchir la liste des tâches
        self.afficher_taches()
    
    def contextMenuEvent(self, event):
        # Fonction pour afficher le menu contextuel
        menu = QMenu(self)
        delete_action = menu.addAction("Supprimer la tâche")
        delete_action.triggered.connect(self.supprimer_tache)
        menu.addAction(delete_action)
        modification_action = menu.addAction("Modifier la tâche")
        modification_action.triggered.connect(self.modifier_tache)
        menu.addAction(modification_action)
        menu.exec(self.listetaches.mapToGlobal(event))
    
    def afficher_taches(self):
        # Chargement des tâches existantes
        connection = sqlite3.connect('taches.db')
        cur = connection.cursor()
        results = cur.execute("SELECT * FROM taches")
        self.listetaches.setRowCount(requetesql.tailledelabddtache())
        tablerow = 0
        for row in results:
            for colonnes in range(6):
                self.listetaches.setItem(tablerow, colonnes, QTableWidgetItem(str(row[colonnes])))
            tablerow += 1
        self.listetaches.setSortingEnabled(True)
        connection.close()
    
    def supprimer_tache(self):
        # Fonction pour supprimer une tâche sélectionnée
        # recupérer l'id de la tâche sélectionnée et la supprimer
        requetesql.supprimer_tache(id=self.listetaches.item(self.listetaches.currentRow(), 0).text())
        self.afficher_taches()
        QMessageBox.information(self, "Tâche supprimée", "La tâche a été supprimée avec succès.")
    
    def modifier_tache(self):
        # Fonction pour modifier une tâche sélectionnée
        # afficher les données de la tâche sélectionnée dans les champs de saisie
        self.id = self.listetaches.item(self.listetaches.currentRow(), 0).text()
        self.tache_input.setText(self.listetaches.item(self.listetaches.currentRow(), 1).text())
        self.date_input.setDate(QDate.fromString(self.listetaches.item(self.listetaches.currentRow(), 2).text(), "dd/MM/yyyy"))
        self.heure_input.setTime(QTime.fromString(self.listetaches.item(self.listetaches.currentRow(), 3).text(), "HH:mm"))
        self.description_input.setText(self.listetaches.item(self.listetaches.currentRow(), 4).text())
        self.priorite_input.setValue(int(self.listetaches.item(self.listetaches.currentRow(), 5).text()))
    
    def encodage_tache_modifiee(self):
        # Fonction pour encoder les modifications d'une tâche
        requetesql.modifier_tache(id=self.id, nom=self.tache_input.text(), date=self.date_input.date().toString("dd/MM/yyyy"), heure=self.heure_input.time().toString("HH:mm"), description=self.description_input.toPlainText(), priorite=self.priorite_input.value())
        self.afficher_taches()
        QMessageBox.information(self, "Tâche modifiée", "La tâche a été modifiée avec succès.")
        self.tache_input.clear()
        self.description_input.clear()
        self.priorite_input.setValue(3)
        self.date_input.setDate(QDate.currentDate())
        self.heure_input.setTime(QTime.currentTime())
        self.id = 0