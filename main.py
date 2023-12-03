# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon

from PySide6.QtWidgets import *


from package import fonctions, bdd
from SubApplication import fenetreapropos

basedir = os.path.dirname(__file__)
def repertoirebdd():
    repertoire = os.path.join(basedir,"./plantes")
    return repertoire

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle("Mon Potager")
        self.resize(1024, 768)
        toolbar = QToolBar("ma barre de menu")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        BTNplanteajoutee = QAction(QIcon(os.path.join(basedir, "icons/box.png")),"Ajouter une plante", self, )
        BTNplanteajoutee.triggered.connect(self.affichagefenetreajoutdeplante)
        BTNplanteajoutee.setCheckable(True)
        BTNrecherchepartaille = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Recherche par taille", self, )
        BTNrecherchepartaille.triggered.connect(self.recherchepartaille)
        BTNrecherchepartaille.setCheckable(True)
        BTNapropos = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "A propos...", self,)
        BTNapropos.triggered.connect(self.affichageapropos)
        BTNapropos.setCheckable(True)
        # ajout d'un menu

        menu = self.menuBar()
        #les différents menus de l'appli
        MNUfichier = menu.addMenu("&Fichier")
        MNUedition = menu.addMenu("Edition")
        MNUaide = menu.addMenu("Aide")
        #les différents choix dans chaque menu
        MNUfichier.addAction(BTNplanteajoutee)
        MNUfichier.addSeparator()
        MNUedition.addAction(BTNrecherchepartaille)
        MNUedition.addSeparator()
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
                self.w.show()
            case False:
                self.w.close()
                self.w = None
                match FENamontrer:
                    case 1:
                        self.w = fonctions.Fenetreajoutplante()
                    case 2:
                        self.w = fenetreapropos.Apropos()
                self.w.show()

    def affichagefenetreajoutdeplante(self, checked):
        self.gestion_fenetre(1)

    def recherchepartaille(self,checked):
        pass
    
    def affichageapropos(self, checked):
        self.gestion_fenetre(2)
         # fin de la section du menu



bdd.creationBDD()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.resize(1600, 1200)
app.exec()

