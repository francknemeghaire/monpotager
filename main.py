# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon

from PySide6.QtWidgets import *


from package import fonctions, bdd
from SubApplication import fenetreapropos, AffichageListingBdd

basedir = os.path.dirname(__file__)
def repertoirebdd():
    repertoire = os.path.join(basedir,"./plantes")
    return repertoire

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle("Mon Potager")
        self.resize(800, 600)
        toolbar = QToolBar("ma barre de menu")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        BTNplanteajoutee = QAction(QIcon(os.path.join(basedir, "icons/box.png")),"Ajouter une plante", self, )
        BTNplanteajoutee.triggered.connect(self.affichagefenetreajoutdeplante)
        BTNplanteajoutee.setCheckable(True)
        BTNaffichagelistingplante = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Affichage des plantes de la base de données", self, )
        BTNaffichagelistingplante.triggered.connect(self.affichagelstplante)
        BTNaffichagelistingplante.setCheckable(True)
        BTNrechercheparnom = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Recherche par nom", self, )
        BTNrechercheparnom.triggered.connect(self.rechercheparnom)
        BTNrechercheparnom.setCheckable(True)
        BTNapropos = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "A propos...", self,)
        BTNapropos.triggered.connect(self.affichageapropos)
        BTNapropos.setCheckable(True)
        # ajout d'un menu

        menu = self.menuBar()
        #les différents menus de l'appli
        MNUfichier = menu.addMenu("Fichier")
        MNUedition = menu.addMenu("Edition")
        MNUaffichage = menu.addMenu("Affichage")
        MNUrecherche = menu.addMenu("Recherche")
        MNUaide = menu.addMenu("Aide")
        #les différents choix dans chaque menu
        MNUfichier.addAction(BTNplanteajoutee)
        MNUfichier.addSeparator()
        MNUedition.addAction(BTNaffichagelistingplante)
        MNUedition.addSeparator()
        MNUaffichage.addAction(BTNaffichagelistingplante)
        MNUaffichage.addSeparator()
        MNUrecherche.addAction(BTNrechercheparnom)
        MNUaide.addAction(BTNapropos)
        MNUfichier.addSeparator()

    def gestion_fenetre(self, FENamontrer):
        #vérifier W cloturée ou pas
        match self.w is None:
            case True:
                match FENamontrer:
                    #fenetre ajout de plantes
                    case 1:
                        self.w = fonctions.Fenetreajoutplante()
                    case 2:
                        self.w = fenetreapropos.Apropos()
                    case 3:
                        self.w = AffichageListingBdd.AffichagelistingBdd()
                    case 4:
                        self.w = AffichageListingBdd.AffichageParNom()
                self.w.show()
            case False:
                self.w.close()
                self.w = None
                match FENamontrer:
                    case 1:
                        self.w = fonctions.Fenetreajoutplante()
                    case 2:
                        self.w = fenetreapropos.Apropos()
                    case 3:
                        self.w = AffichageListingBdd.AffichagelistingBdd()
                    case 4:
                        self.w = AffichageListingBdd.AffichageParNom()
                self.w.show()

    def affichagefenetreajoutdeplante(self, checked):
        self.gestion_fenetre(1)

    def affichageapropos(self, checked):
        self.gestion_fenetre(2)

    def affichagelstplante(self, checked):
        self.gestion_fenetre(3)

    def rechercheparnom(self, checked):
        self.gestion_fenetre(4)
         # fin de la section du menu



bdd.creationBDD()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.resize(800, 600)
app.exec()

