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
    QGridLayout,
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
        layout = QGridLayout(self)
        self.setWindowTitle("fenêtre d'ajout de plante")
        self.LBLnom = QLabel("Quel est le nom de la plante? ")
        self.LEnom = QLineEdit()
        self.LBLht = QLabel("Quelle est la hauteur de la plante? ")
        self.LEht = QLineEdit()
        self.LBLenvergure = QLabel("Quelle est son envergure? ")
        self.LEenvg = QLineEdit()
        self.LBLexpo = QLabel("A quelle exposition peut on la planter (ombre, mi-ombre, etc): ")
        self.LEexpo = QLineEdit()
        self.LBLdatesemis = QLabel("Quand peut-on débuter les semis: ")
        self.LEdatesemis = QLineEdit()
        self.LBLdateplantation = QLabel("Quand peut on les mettre en pleine terre: ")
        self.LEdateplantation = QLineEdit()
        self.LBLduree = QLabel("combien de temps occupe-t-il l'espace octroyer dans le jardin? ")
        self.LEduree = QLineEdit()
        self.LBLarrosage = QLabel("Quel est son besoin en eau? ")
        self.LEarrosage = QLineEdit()
        self.LBLsol = QLabel("Quelle doit être la richesse du sol? ")
        self.LEsol = QLineEdit()
        self.LBLassoc = QLabel("Avec quelles autres plantes peut-on l'associer? ")
        self.LEassoc = QLineEdit()
        self.LBLtempgerm = QLabel("Quelle est la température de germination? ")
        self.LEtempgerm = QLineEdit()

        layout.addWidget(self.LBLnom, 0, 0)
        layout.addWidget(self.LEnom, 0, 1)
        layout.addWidget(self.LBLht, 1, 0)
        layout.addWidget(self.LEht, 1, 1)
        layout.addWidget(self.LBLenvergure, 2, 0)
        layout.addWidget(self.LEenvg, 2, 1)
        layout.addWidget(self.LBLexpo, 3, 0)
        layout.addWidget(self.LEexpo, 3, 1)
        layout.addWidget(self.LBLdatesemis, 4, 0)
        layout.addWidget(self.LEdatesemis, 4, 1)
        layout.addWidget(self.LBLdateplantation, 5, 0)
        layout.addWidget(self.LEdateplantation, 5, 1)
        layout.addWidget(self.LBLduree, 6, 0)
        layout.addWidget(self.LEduree, 6, 1)
        layout.addWidget(self.LBLarrosage, 7, 0)
        layout.addWidget(self.LEarrosage, 7, 1)
        layout.addWidget(self.LBLsol, 8, 0)
        layout.addWidget(self.LEsol, 8, 1)
        layout.addWidget(self.LBLassoc, 9, 0)
        layout.addWidget(self.LEassoc, 9, 1)
        layout.addWidget(self.LBLtempgerm, 10, 0)
        layout.addWidget(self.LEtempgerm, 10, 1)
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

        BTNplanteajoutee = QAction(QIcon(os.path.join(basedir, "icons/box.png")),"Ajouter une plante", self,)
        BTNplanteajoutee.triggered.connect(self.affichagefenetreajoutdeplante)
        BTNplanteajoutee.setCheckable(True)
        # ajout d'un menu

        menu = self.menuBar()

        MNUfichier = menu.addMenu("&Fichier")
        MNUfichier.addAction(BTNplanteajoutee)
        MNUfichier.addSeparator()

    def affichagefenetreajoutdeplante(self, checked):
        self.w.show()
        # fin de la section du menu


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
