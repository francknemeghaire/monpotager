# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QPixmap

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget,
    QPushButton,
    QToolBar,
    QStatusBar,
)


from package import fonctions,bdd

basedir = os.path.dirname(__file__)


class FenetreApropos(QWidget):
    def __init__(self):
        super().__init__()
        bienvenue = QLabel("Mon potager 1.0")
        # ajout photo écran de démarage
        bienvenue.setAlignment(Qt.AlignTop)
        bienvenue.setAlignment(Qt.AlignHCenter)
        self.apercu = QPixmap("./image/dessinlavande.png")
        self.LBLapercu = QLabel()
        self.LBLapercu.setPixmap(self.apercu)
        self.LBLapercu.setScaledContents(True)
        self.LBLapercu.setAlignment(Qt.AlignBottom)
        self.setCentralWidget(bienvenue)
        self.resize(480, 480)



class Fenetreajoutplante(QWidget):
    def __init__(self):
        super().__init__()
        layoutPrincipal = QHBoxLayout(self)
        layoutGauche = QGridLayout(self)
        layoutDroit = QVBoxLayout(self)
        layoutDroitHaut = QGridLayout(self)
        layoutDroitBas = QVBoxLayout(self)
        layoutPrincipal.addLayout(layoutGauche)
        layoutPrincipal.addLayout(layoutDroit)
        layoutDroit.addLayout(layoutDroitHaut)
        layoutDroit.addLayout(layoutDroitBas)

        self.setWindowTitle("fenêtre d'ajout de plante")
        self.LBLnom = QLabel("Quel est le nom de la plante? ")
        self.LEnom = QLineEdit()
        self.LBLtype = QLabel("Quel type de plante est-ce?")
        self.LEtype = QLineEdit()
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

        # ajout widget layout gauche
        layoutGauche.addWidget(self.LBLnom, 0, 0)
        layoutGauche.addWidget(self.LEnom, 0, 1)
        layoutGauche.addWidget(self.LBLht, 1, 0)
        layoutGauche.addWidget(self.LEht, 1, 1)
        layoutGauche.addWidget(self.LBLenvergure, 2, 0)
        layoutGauche.addWidget(self.LEenvg, 2, 1)
        layoutGauche.addWidget(self.LBLexpo, 3, 0)
        layoutGauche.addWidget(self.LEexpo, 3, 1)
        layoutGauche.addWidget(self.LBLdatesemis, 4, 0)
        layoutGauche.addWidget(self.LEdatesemis, 4, 1)
        layoutGauche.addWidget(self.LBLdateplantation, 5, 0)
        layoutGauche.addWidget(self.LEdateplantation, 5, 1)
        layoutGauche.addWidget(self.LBLduree, 6, 0)
        layoutGauche.addWidget(self.LEduree, 6, 1)
        layoutGauche.addWidget(self.LBLarrosage, 7, 0)
        layoutGauche.addWidget(self.LEarrosage, 7, 1)
        layoutGauche.addWidget(self.LBLsol, 8, 0)
        layoutGauche.addWidget(self.LEsol, 8, 1)
        layoutGauche.addWidget(self.LBLassoc, 9, 0)
        layoutGauche.addWidget(self.LEassoc, 9, 1)
        layoutGauche.addWidget(self.LBLtempgerm, 10, 0)
        layoutGauche.addWidget(self.LEtempgerm, 10, 1)
        layoutDroitHaut.addWidget(self.LBLtype, 0, 0)
        layoutDroitHaut.addWidget(self.LEtype, 0, 1)

        # bouton de commande layout droit
        btnSauvegarde = QPushButton("Sauvegarde", self)
        btnRecherche = QPushButton("Rechercher", self)
        btnAjouter = QPushButton("Ajouter", self)
        btnSupprimer = QPushButton("Supprimer", self)

        # ajout boutons au layout droit
        layoutDroitBas.addWidget(btnAjouter)
        layoutDroitBas.addWidget(btnRecherche)
        layoutDroitBas.addWidget(btnSauvegarde)
        layoutDroitBas.addWidget(btnSupprimer)
        layoutDroitBas.setAlignment(Qt.AlignLeft)
        layoutDroitBas.setAlignment(Qt.AlignBottom)
        self.setLayout(layoutPrincipal)
        self.resize(1024, 768)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = Fenetreajoutplante()
        self.setWindowTitle("Mon Potager")
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


bdd.creationBDD()
app = QApplication(sys.argv)

window = MainWindow()
window.show()
window.resize(1600, 1200)
app.exec()
