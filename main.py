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
        layout = QVBoxLayout()
        self.setWindowTitle("fenêtre d'ajout de plante")
        self.label = QLabel("nom de la plante: ")

        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = Fenetreajoutplante()
        self.setWindowTitle("Mon Potager")
        bienvenue = QLabel("Bonjour")
        bienvenue.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(bienvenue)

        toolbar = QToolBar("ma barre de menu")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        planteajoutee = QAction(QIcon(os.path.join(basedir, "icons/box.png")),"Ajouter une plante", self,)
        planteajoutee.triggered.connect(self.affichagefenetreajoutdeplante)
        planteajoutee.setCheckable(True)
        # ajout d'un menu

        menu = self.menuBar()

        file_menu = menu.addMenu("&Fichier")
        file_menu.addAction(planteajoutee)
        file_menu.addSeparator()

    def affichagefenetreajoutdeplante(self, checked):
        self.w.show()
        # fin de la section du menu


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
