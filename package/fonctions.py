from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class Plante:
    """création structure pour bdd de plantes"""

    def __init__(self):
        self.nom = ""
        self.envergure = 0
        self.hauteur = 0
        self.exposition = ""
        self.datedesemis = ""
        self.datedeplantation = ""
        self.duree = ""
        self.arrosage = ""
        self.typesol = ""
        self.associations = ""
        self.temperaturegermination = 0
        self.type = ""
        self.couleur = ""
        self.emplacement = ""
        self.feuillagepersistant = 0
        self.mellifere = 0
        self.moisdefloraison = ""
        self.moisderecolte = ""
        self.planteparfumee = 0
        self.plantevivace = 0
        self.cheminaccesimage = ""



    def parcourirlabasededonnee(self):
        connection = sqlite3.connect("plantes.db")
        cursor = connection.cursor()
        sqlstr = 'SELECT * FROM plantes'
        plantedelabdd = cursor.execute(sqlstr)
        donnees = plantedelabdd.fetchall()
        for plante in donnees:
            print(plante)


class apercuphoto(QWidget):
    def __init__(self,nom):
        super().__init__()
        self.nomfichier = nom
        self.image = QImage(self.nomfichier)
        layout = QVBoxLayout()
        self.nomphoto = QPixmap(self.image.scaled(800,600))
        self.photo = QLabel()
        self.photo.setPixmap(self.nomphoto)
        layout.addWidget(self.photo)
        self.setLayout(layout)