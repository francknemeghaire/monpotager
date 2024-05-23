from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QStringListModel
from googlesearch import search


class FENrechercheinternet(QWidget):
    def __init__(self):
        super().__init__()
        layoutPrincipal = QHBoxLayout(self)
        layoutGauche = QGridLayout(self)
        layoutDroit = QVBoxLayout(self)
        layoutPrincipal.addLayout(layoutGauche)
        layoutPrincipal.addLayout(layoutDroit)
        self.setWindowTitle("Recherche internet")
        self.LBLcritere = QLabel("Que recherchez vous ? ")
        self.LEcritere = QLineEdit()
        self.LSTVIEWresultat = QListView()
        self.modele = QStringListModel()
        self.tableaumodele = []
        self.btnQuitter = QPushButton("Quitter", self)
        self.btnRecherche = QPushButton("Recherche", self)
        self.btnQuitter.clicked.connect(self.quitter_recherche)
        #critere =
        self.btnRecherche.clicked.connect(self.recherchesurinternet)
        #layout
        layoutGauche.addWidget(self.LBLcritere,0,0)
        layoutGauche.addWidget(self.LEcritere,0,1)
        layoutGauche.addWidget(self.LSTVIEWresultat,1,0)
        layoutDroit.addWidget(self.btnQuitter)
        layoutDroit.addWidget(self.btnRecherche)
        self.setLayout(layoutPrincipal)
        self.resize(800, 400)

    def quitter_recherche(self):
        self.close()

    def recherchesurinternet(self):
        proxy = 'http://API:@proxy.host.com:8080/'

        j = search("tomates", lang="fr")
        for i in j:
            #return(i)
            self.tableaumodele.append(i)
        self.modele.setStringList(self.tableaumodele)
        self.LSTVIEWresultat.setModel(self.modele)