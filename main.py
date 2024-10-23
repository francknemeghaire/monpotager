# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon

from PySide6.QtWidgets import *

from package import fonctions, bdd
from SubApplication import fenetreapropos, AffichageListingBdd, rechercheinternet, vision3D



basedir = os.path.dirname(__file__)
def repertoirebdd():
    repertoire = os.path.join(basedir,"./plantes")
    return repertoire

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CodeForTerra")
        #self.resize(300, 200)
        self.setGeometry(0,0,800,200)
        toolbar = QToolBar()
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
        # bouton lié à la planification et organisation
        BTNcalendrierjardin = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Calendrier du jardin", self,)
        BTNcalendrierjardin.triggered.connect(self.calendrierjardin)
        BTNcalendrierjardin.setCheckable(False)
        BTNgestiontaches = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Gestion des tâches", self,)
        BTNgestiontaches.triggered.connect(self.gestiontaches)
        BTNgestiontaches.setCheckable(False)
        BTNdiagnostictraitement = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Diagnostic et traitement", self, )
        BTNdiagnostictraitement.triggered.connect(self.DiagnosticTraitement)
        BTNdiagnostictraitement.setCheckable(False)
        BTNvisualisation3D = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Visualisation", self, )
        BTNvisualisation3D.triggered.connect(self.Visualisation3D)
        BTNvisualisation3D.setCheckable(False)
        # ajout d'un menu

        menu = self.menuBar()
        #les différents menus de l'appli
        MNUGestion = menu.addMenu("Gestion")
        MNUVisualisation = menu.addMenu("Visualisation")
        MNUPlanification = menu.addMenu("Planification")
        MNUOrganisation = menu.addMenu("Organisation")
        MNUSanteEntretien = menu.addMenu("Santé et Entretien")

        MNUaide = menu.addMenu("Aide")
        #les différents choix dans chaque menu
        MNUGestion.addAction(BTNplanteajoutee)
        MNUGestion.addSeparator()
        MNUGestion.addAction(BTNaffichagelistingplante)
        MNUGestion.addSeparator()
        MNUGestion.addAction(BTNrechercheparnom)
        MNUGestion.addAction(BTNrecherchepartaille)
        MNUGestion.addAction(BTNrechercheparassociation)
        MNUGestion.addAction(BTNrechercheparsaison)
        MNUVisualisation.addAction(BTNrechercheinternet)
        MNUVisualisation.addSeparator()
        MNUVisualisation.addAction(BTNvisualisation3D)
        MNUPlanification.addAction(BTNcalendrierjardin)
        MNUOrganisation.addAction(BTNgestiontaches)
        MNUOrganisation.addSeparator()
        MNUSanteEntretien.addAction(BTNdiagnostictraitement)

        MNUaide.addAction(BTNapropos)

    def affichagefenetreajoutdeplante(self, checked):
        self.FENajoutplante= fonctions.Fenetreajoutplante()
        self.FENajoutplante.show()

    def affichageapropos(self, checked):
        self.FENapropos = fenetreapropos.Apropos()
        self.FENapropos.show()

    def affichagelstplante(self, checked):
        self.FENlstplante = AffichageListingBdd.AffichagelistingBdd()
        self.FENlstplante.show()

    def rechercheparnom(self, checked):
        self.FENlstparnom = AffichageListingBdd.AffichageParNom()
        self.FENlstparnom.show()
# recherche par taille
    def recherchepartaille(self, checked):
        self.FENlstpartaille = AffichageListingBdd.AffichageParTaille()
        self.FENlstpartaille.show()
# recherche par association
    def rechercheparassociation(self, checked):
        self.FENlstparassociation = AffichageListingBdd.AffichageParAssociation()
        self.FENlstparassociation.show()
# recherche par saison de plantation
    def rechercheparsaison(self, checked):
        self.FENlstparsaison = AffichageListingBdd.AffichageParSaison()
        self.FENlstparsaison.show()
# recherche par internet
    def rechercheinternet(self, checked):
        #self.gestion_fenetre(8)
        critere = QInputDialog.getText(self, "Recherche internet", "Nom de plante à rechercher")
        self.FENrechercheinternet = rechercheinternet.rechercheinternet(critere=critere[0])
        self.FENrechercheinternet.show()
# calendrier jardin
    def calendrierjardin(self, checked):
        #creer une interface pour avoir un calendrier
        pass
# gestion des tâches
    def gestiontaches(self, checked):
        #creer une interface en lien avec le calendrier?
        pass
# diagnostic et traitement
    def DiagnosticTraitement(self, checked):
        pass
        # fin de la section du menu
# visualisation 3D
    def Visualisation3D(self, checked):
        self.FENvisualisation = vision3D.GardenApp()
        self.FENvisualisation.run()

bdd.creationBDD()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

