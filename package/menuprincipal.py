from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

import sys

class Menuprincipal(QMainWindow):
    def __init__(self):
        super().__init__(self)

        self.setWindowTitle("Menu principal")

        self.ajoutplante = QLabel()
        self.planteaajouter = QLineEdit()
        self.afficherplanteajoutee = QLabel()
        self.ajoutplante.setText("Quel est le nom de la plante à ajouter?")
        self.planteaajouter.textChanged.connect(self.afficherplanteajoutee.setText)
        layout = QVBoxLayout()
        layout.addWidget(self.ajoutplante)
        layout.addWidget(self.planteaajouter)
        layout.addWidget(self.afficherplanteajoutee)

        container =QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

fenmenu = Menuprincipal()
fenmenu.show()

app.exec()