# This Python file uses the following encoding: utf-8
import os.path

from PySide6.QtWidgets import(
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QPushButton,
)

import sys
from package import fonctions, requetesql


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon Potager")

        self.button = QPushButton("menu principal")
        self.button.clicked.connect(self.afficher_menu_principal)

        self.setCentralWidget(self.button)

    def afficher_menu_principal(self):
        self.setWindowTitle("Menu principal")
        self.choixmenu1 = QLabel("1) Ajouter une plante")
        self.choixmenu2 = QLabel("2) Enregistrer dans la base de donnée")
        self.choixmenu3 = QLabel("3) Rechercher une plante")
        self.choixmenu4 = QLabel("4) Quitter")
        self.label = QLabel()
        self.input = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.choixmenu1)
        layout.addWidget(self.choixmenu2)
        layout.addWidget(self.choixmenu3)
        layout.addWidget(self.choixmenu4)
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.input.textChanged.connect(self.testvaleur)

    def testvaleur(self, s):
        fonctions.testchoixmenu(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
