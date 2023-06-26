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


from package import fonctions, bdd

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = fonctions.Fenetreajoutplante()
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

    def FNTapropos(self):
        self.apropos.show


bdd.creationBDD()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.resize(1600, 1200)
app.exec()

