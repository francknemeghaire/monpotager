from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (QCalendarWidget, QGridLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QDialog)

class Calendrier(QDialog):
    def __init__(self):
        super().__init__()
        #self.setGeometry(0, 0, 500, 500)
        #creation du calendrier
        self.OBJcalendrier = QCalendarWidget(self)
        self.OBJcalendrier.setMinimumDate(QDate.currentDate())
        self.OBJcalendrier.setMaximumDate(QDate(2054, 1, 1))
        self.dateselectionnee = QLabel(self)

        # creation bouton
        self.BTNquitter = QPushButton('Quitter', self)
        self.BTNquitter.clicked.connect(self.quitter)

        #configuration de l'interface
        layoutprincipal = QHBoxLayout(self)
        layoutgauche = QVBoxLayout(self)
        layoutdroit = QGridLayout(self)
        layoutprincipal.addLayout(layoutgauche)
        layoutprincipal.addLayout(layoutdroit)
        layoutgauche.addWidget(self.OBJcalendrier)
        layoutdroit.addWidget(self.dateselectionnee, 0, 0)
        layoutdroit.addWidget(self.BTNquitter, 1, 0)

        #selection de date par clic de souris
        self.OBJcalendrier.selectionChanged.connect(self.selectiondate)
        self.show()

    #code lié à la selection d'une date
    def selectiondate(self):
        date = self.OBJcalendrier.selectedDate()
        self.dateselectionnee.setText(date.toString("dd MMMM yy"))

    # code lié à l'action des boutons
    def quitter(self):
        self.close()