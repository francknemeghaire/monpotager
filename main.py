# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar

from package import fonctions, bdd, AffichageListingBdd
from SubApplication import fenetreapropos, FENresultatsrecherche, rechercheinternet, calendrier, FENajoutplantes, Fenaffichagebasededonnee,gestiondestaches



basedir = os.path.dirname(__file__)
icons = os.path.join(basedir, "icons")
def repertoirebdd():
    repertoire = os.path.join(basedir,"./plantes")
    return repertoire

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CodeForTerra")
        #self.resize(300, 200)
        self.setGeometry(0,0,800,200)

        #ajout de plante
        BTNplanteajoutee = QAction(QIcon(os.path.join(icons, "database.png")),"Gestion base de données de plantes", self, )
        BTNplanteajoutee.triggered.connect(self.affichagefenetreajoutdeplante)
        BTNplanteajoutee.setCheckable(True)
        #menu édition recherche internet
        BTNrechercheinternet = QAction(QIcon(os.path.join(basedir, "icons/icons8-google-48.png")),"recherche internet", self, )
        BTNrechercheinternet.triggered.connect(self.rechercheinternet)
        BTNrechercheinternet.setCheckable(True)
        #affichage de plante
        BTNaffichagelistingplante = QAction(QIcon(os.path.join(basedir, "icons/database.png")), "Affichage des plantes de la base de données", self, )
        BTNaffichagelistingplante.triggered.connect(self.affichagelstplante)
        BTNaffichagelistingplante.setCheckable(True)
        #recherche par nom
        BTNrechercheparnom = QAction(QIcon(os.path.join(basedir, "icons/icons8-search-48.png")), "Recherche par nom", self, )
        BTNrechercheparnom.triggered.connect(self.rechercheparnom)
        BTNrechercheparnom.setCheckable(True)
        #recherche par taille
        BTNrecherchepartaille = QAction(QIcon(os.path.join(basedir, "icons/icons8-search-48.png")), "Recherche par taille", self, )
        BTNrecherchepartaille.triggered.connect(self.recherchepartaille)
        BTNrecherchepartaille.setCheckable(True)
        #recherche par association
        BTNrechercheparassociation = QAction(QIcon(os.path.join(basedir, "icons/icons8-search-48.png")), "Recherche par association", self, )
        BTNrechercheparassociation.triggered.connect(self.rechercheparassociation)
        BTNrechercheparassociation.setCheckable(True)
        #recherche par saison de plantation
        BTNrechercheparsaison = QAction(QIcon(os.path.join(basedir, "icons/icons8-search-48.png")), "Recherche par saison de plantation", self,)
        BTNrechercheparsaison.triggered.connect(self.rechercheparsaison)
        BTNrechercheparsaison.setCheckable(True)
        #affichage fenetre d'infos appli
        BTNapropos = QAction(QIcon(os.path.join(basedir, "icons/icons8-question-48.png")), "A propos...", self,)
        BTNapropos.triggered.connect(self.affichageapropos)
        BTNapropos.setCheckable(True)
        # bouton lié à la planification et organisation
        BTNcalendrierjardin = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Calendrier du jardin", self,)
        BTNcalendrierjardin.triggered.connect(self.calendrierjardin)
        BTNcalendrierjardin.setCheckable(True)
        BTNgestiontaches = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Gestion des tâches", self,)
        BTNgestiontaches.triggered.connect(self.gestiontaches)
        BTNgestiontaches.setCheckable(True)
        BTNdiagnostictraitement = QAction(QIcon(os.path.join(basedir, "icons/box.png")), "Diagnostic et traitement", self, )
        BTNdiagnostictraitement.triggered.connect(self.DiagnosticTraitement)
        BTNdiagnostictraitement.setCheckable(True)
        # ajout d'un menu

        menu = self.menuBar()
        #les différents menus de l'appli
        MNUGestion = menu.addMenu("Gestion")
        MNUPlanification = menu.addMenu("Planification")
        MNUOrganisation = menu.addMenu("Organisation")
        MNUSanteEntretien = menu.addMenu("Santé et Entretien")
        MNURecherche = menu.addMenu("Recherche")

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
        MNURecherche.addAction(BTNrechercheinternet)
        MNURecherche.addSeparator()
        MNUPlanification.addAction(BTNcalendrierjardin)
        MNUOrganisation.addAction(BTNgestiontaches)
        MNUOrganisation.addSeparator()
        MNUSanteEntretien.addAction(BTNdiagnostictraitement)
        MNUaide.addAction(BTNapropos)
        #toolbar
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(30, 30))
        self.addToolBar(toolbar)
        # bouton toolbar
        TLBquit = QAction(QIcon(os.path.join(basedir, "icons/exit.png")), "Quitter", self)
        TLBquit.triggered.connect(self.close)
        toolbar.addAction(TLBquit)

    def affichagefenetreajoutdeplante(self, checked):
        #création d'une nouvelle fiche de plante
        self.FENajoutplante = FENajoutplantes.Fenetreajoutplante()
        self.FENajoutplante.show()

    def affichageapropos(self, checked):
        self.FENapropos = fenetreapropos.Apropos()
        self.FENapropos.show()

    def affichagelstplante(self, checked):
        self.FENlstplante = Fenaffichagebasededonnee.Affichagebasededonnee()
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
        self.FENcalendrier = calendrier.Calendrier()
        self.FENcalendrier.show()
# gestion des tâches
    def gestiontaches(self, checked):
        self.FENgestiontaches = gestiondestaches.GestionDesTaches()
        self.FENgestiontaches.show()
        
# diagnostic et traitement
    def DiagnosticTraitement(self, checked):
        pass
        # fin de la section du menu

bdd.creationBDD()
bdd.creationbddtaches()
#creation de la base de données
app = QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()
window.show()
app.exec()

