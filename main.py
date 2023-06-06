# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QToolBar,
    QStatusBar,
)


from package import fonctions, requetesql

basedir = os.path.dirname(__file__)


class Fenetreajoutplante(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("fenêtre d'ajout de plante")
        self.nom = QLabel("Quel est le nom de la plante? ")
        self.nouveaunom = QLineEdit()
        self.hauteur = QLabel("Quelle est la hauteur de la plante? ")
        self.htplante = QLineEdit()
        self.envergure = QLabel("Quelle est son envergure? ")
        self.envg = QLineEdit()
        self.exposition = QLabel("A quelle exposition peut on la planter (ombre, mi-ombre, etc): ")
        self.datesemis = QLabel("Quand peut-on débuter les semis: ")
        self.dateplantation = QLabel("Quand peut on les mettre en pleine terre: ")
        self.duree = QLabel("combien de temps occupe-t-il l'espace octroyer dans le jardin? ")
        self.arrosage = QLabel("Quel est son besoin en eau? ")
        self.richesse_sol = QLabel("Quelle doit être la richesse du sol? ")
        self.associations = QLabel("Avec quelles autres plantes peut-on l'associer? ")
        self.temperaturegermination = QLabel("Quelle est la température de germination? ")

        layout.addWidget(self.nom)
        layout.addWidget(self.nouveaunom)
        layout.addWidget(self.hauteur)
        layout.addWidget(self.htplante)
        layout.addWidget(self.envergure)
        layout.addWidget(self.envg)
        layout.addWidget(self.exposition)
        layout.addWidget(self.datesemis)
        layout.addWidget(self.dateplantation)
        layout.addWidget(self.duree)
        layout.addWidget(self.arrosage)
        layout.addWidget(self.richesse_sol)
        layout.addWidget(self.associations)
        layout.addWidget(self.temperaturegermination)
        self.setLayout(layout)
        self.resize(800, 600)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = Fenetreajoutplante()
        self.setWindowTitle("Mon Potager")
        bienvenue = QLabel("Bonjour")
        bienvenue.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(bienvenue)
        self.resize(1024, 768)

        toolbar = QToolBar("ma barre de menu")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        planteajoutee = QAction(QIcon(os.path.join(basedir, "icons/box.png")),"Ajouter une plante", self,)
        planteajoutee.triggered.connect(self.affichagefenetreajoutdeplante)
        planteajoutee.setCheckable(True)
        # ajout d'un menu

        menu = self.menuBar()

        file_menu = menu.addMenu("&Fichier")
        file_menu.addAction(planteajoutee)
        file_menu.addSeparator()

    def affichagefenetreajoutdeplante(self, checked):
        self.w.show()
        # fin de la section du menu


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
