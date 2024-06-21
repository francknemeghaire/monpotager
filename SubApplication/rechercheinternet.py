from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from package import fonctions
from googlesearch import search


class rechercheinternet(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("SubApplication/rechercheinternet.ui",self)
        self.setWindowTitle("Recherche Internet")
        critere = QInputDialog.getText(self, "Recherche Internet", "Que recherchez vous ?")
        resultatrecherche = fonctions.recherche_internet(critere[0])
        for resultat in enumerate(resultatrecherche, 1):
            self.listWidget.addItem(resultat)
        # for result in search(critere[0], stop=10):
        #     self.listWidget.addItem(result)
        self.show()