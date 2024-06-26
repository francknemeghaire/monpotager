# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon

from PySide6.QtWidgets import *

from package import fonctions, bdd
from SubApplication import fenetreapropos, AffichageListingBdd, rechercheinternet



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
        #ajout de plante
        BTNplanteajoutee = QAction(QIcon(os.path.join(basedir, "icons/box.png")),"Ajouter une plante", self, )
        BTNplanteajoutee.triggered.connect(self.affichagefenetreajoutdeplante)
        BTNplanteajoutee.setCheckable(False)
        #menu édition recherche internet
        BTNrechercheinternet = QAction(QIcon(os.path.join(basedir, "icons/box.png")),"recherche internet", self, )
        BTNrechercheinternet.triggered.connect(self.rechercheinternet)
        BTNrechercheinternet.setCheckable(False)
        #affichage de plante
        BTNaffichagelistingplante = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Affichage des plantes de la base de données", self, )
        BTNaffichagelistingplante.triggered.connect(self.affichagelstplante)
        BTNaffichagelistingplante.setCheckable(False)
        #recherche par nom
        BTNrechercheparnom = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Recherche par nom", self, )
        BTNrechercheparnom.triggered.connect(self.rechercheparnom)
        BTNrechercheparnom.setCheckable(False)
        #recherche par taille
        BTNrecherchepartaille = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Recherche par taille", self, )
        BTNrecherchepartaille.triggered.connect(self.recherchepartaille)
        BTNrecherchepartaille.setCheckable(False)
        #recherche par association
        BTNrechercheparassociation = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Recherche par association", self, )
        BTNrechercheparassociation.triggered.connect(self.rechercheparassociation)
        BTNrechercheparassociation.setCheckable(False)
        #recherche par saison de plantation
        BTNrechercheparsaison = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Recherche par saison de plantation", self,)
        BTNrechercheparsaison.triggered.connect(self.rechercheparsaison)
        BTNrechercheparsaison.setCheckable(False)
        #affichage fenetre d'infos appli
        BTNapropos = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "A propos...", self,)
        BTNapropos.triggered.connect(self.affichageapropos)
        BTNapropos.setCheckable(False)
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
        MNUedition.addAction(BTNrechercheinternet)
        MNUedition.addSeparator()
        MNUaffichage.addAction(BTNaffichagelistingplante)
        MNUaffichage.addSeparator()
        MNUrecherche.addAction(BTNrechercheparnom)
        MNUrecherche.addAction(BTNrecherchepartaille)
        MNUrecherche.addAction(BTNrechercheparassociation)
        MNUrecherche.addAction(BTNrechercheparsaison)
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
                    case 5:
                        self.w = AffichageListingBdd.AffichageParTaille()
                    case 6:
                        self.w = AffichageListingBdd.AffichageParAssociation()
                    case 7:
                        self.w = AffichageListingBdd.AffichageParSaison()
                    case 8:
                        critere = QInputDialog.getText(self, "Recherche internet", "Nom de plante à rechercher")
                        self.w = rechercheinternet.rechercheinternet(critere=critere[0])
                #afficher fenetre
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
                    case 5:
                        self.w = AffichageListingBdd.AffichageParTaille()
                    case 6:
                        self.w = AffichageListingBdd.AffichageParAssociation()
                    case 7:
                        self.w = AffichageListingBdd.AffichageParSaison()
                    case 8:
                        critere = QInputDialog.getText(self, "Recherche internet", "Nom de plante à rechercher")
                        self.w = rechercheinternet.rechercheinternet(critere=critere[0])
                self.w.show()

    def affichagefenetreajoutdeplante(self, checked):
        self.gestion_fenetre(1)

    def affichageapropos(self, checked):
        self.gestion_fenetre(2)

    def affichagelstplante(self, checked):
        self.gestion_fenetre(3)

    def rechercheparnom(self, checked):
        self.gestion_fenetre(4)
# recherche par taille
    def recherchepartaille(self, checked):
        self.gestion_fenetre(5)
# recherche par association
    def rechercheparassociation(self, checked):
        self.gestion_fenetre(6)
# recherche par saison de plantation
    def rechercheparsaison(self, checked):
        self.gestion_fenetre(7)
# recherche par internet
    def rechercheinternet(self, checked):
        self.gestion_fenetre(8)
        # fin de la section du menu


bdd.creationBDD()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.resize(800, 600)
app.exec()

