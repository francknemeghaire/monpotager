from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *

class rechercheinternet(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("SubApplication/rechercheinternet.ui",self)
        self.setWindowTitle("Recherche Internet")
        self.show()

