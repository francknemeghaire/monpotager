import os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sqlite3


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

class modifierFichePlante(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layoutPrincipal = QHBoxLayout(widget)
        layoutGauche = QGridLayout(widget)
        layoutPrincipal.addLayout(layoutGauche)
        # création d'un toolbar
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(30, 30))
        self.addToolBar(toolbar)
        # bouton toolbar
        TLBquit = QAction(QIcon(os.path.join("icons", "exit.png")), "Quitter", self)
        TLBquit.triggered.connect(self.close)
        toolbar.addAction(TLBquit)

        self.LBLid = QLabel("id de la plante?: ")
        self.LEid = QLineEdit()
        self.LBLnom = QLabel("Quel est le nom de la plante? ")
        self.LEnom = QLineEdit()
        self.LBLenvergure = QLabel("Quelle est son envergure? ")
        self.LEenvg = QLineEdit()
        self.LBLht = QLabel("Quelle est la hauteur de la plante? ")
        self.LEht = QLineEdit()
        self.LBLexpo = QLabel("A quelle exposition peut on la planter (ombre, mi-ombre, etc): ")
        self.LEexpo = QLineEdit()
        self.LBLdatesemis = QLabel("Quand peut-on débuter les semis: ")
        self.LEdatesemis = QLineEdit()
        self.LBLdateplantation = QLabel("Quand peut on les mettre en pleine terre: ")
        self.LEdateplantation = QLineEdit()
        self.LBLduree = QLabel("combien de temps occupe-t-il l'espace octroyer dans le jardin? ")
        self.LEduree = QLineEdit()
        self.LBLarrosage = QLabel("Quel est son besoin en eau? ")
        self.LEarrosage = QLineEdit()
        self.LBLsol = QLabel("Quelle doit être la richesse du sol? ")
        self.LEsol = QLineEdit()
        self.LBLassoc = QLabel("Avec quelles autres plantes peut-on l'associer? ")
        self.LEassoc = QLineEdit()
        self.LBLtempgerm = QLabel("Quelle est la température de germination? ")
        self.LEtempgerm = QLineEdit()
        # ajout caractéristique supplémentaires 8/5/24
        self.LBLtypedeplante = QLabel("Quelle type de plante est-ce ? ")
        self.LEtypedeplante = QLineEdit()
        self.LBLcouleurdeplante = QLabel("Quelle est la couleur de la plante ?")
        self.LEcouleurdeplante = QLineEdit()
        self.LBLemplacement = QLabel("Où va-t-on placer cette plante? ")
        self.LEemplacement = QLineEdit()
        self.LBLfeuillagepersistant = QLabel("Est-ce une plante avec un feuillage persistant ?")
        self.CHKBOXfeuillagepersistant = QCheckBox()
        self.CHKBOXfeuillagepersistant.setChecked(False)
        self.LBLmellifere = QLabel("Est-ce un mellifère ?")
        self.CHKBOXmellifere = QCheckBox()
        self.CHKBOXmellifere.setChecked(False)
        self.LBLmoisdefloraison = QLabel("Quelle est la mois de floraison ?")
        self.LEmoisdefloraison = QLineEdit()
        self.LBLmoisderecolte = QLabel("Quel est le mois de recolte ?")
        self.LEmoisderecolte = QLineEdit()
        self.LBLplanteparfumee = QLabel("La plante est-elle parfumée ?")
        self.CHKBOXplanteparfumee = QCheckBox()
        self.CHKBOXplanteparfumee.setChecked(False)
        self.LBLplantevivace = QLabel("Est-ce une plante vivace ?")
        self.CHKBOXplantevivace = QCheckBox()
        self.CHKBOXplantevivace.setChecked(False)
        # partie du code pour traitement des photos
        self.LBLcheminaccesimage = QLabel("chemin d'accès de la photo ?")
        self.LEcheminaccesimage = QLineEdit()

        # ajout widget layout gauche
        layoutGauche.addWidget(self.LBLid, 0, 0)
        layoutGauche.addWidget(self.LEid, 0, 1)
        layoutGauche.addWidget(self.LBLnom, 1, 0)
        layoutGauche.addWidget(self.LEnom, 1, 1)
        layoutGauche.addWidget(self.LBLenvergure, 2, 0)
        layoutGauche.addWidget(self.LEenvg, 2, 1)
        layoutGauche.addWidget(self.LBLht, 3, 0)
        layoutGauche.addWidget(self.LEht, 3, 1)
        layoutGauche.addWidget(self.LBLexpo, 4, 0)
        layoutGauche.addWidget(self.LEexpo, 4, 1)
        layoutGauche.addWidget(self.LBLdatesemis, 5, 0)
        layoutGauche.addWidget(self.LEdatesemis, 5, 1)
        layoutGauche.addWidget(self.LBLdateplantation, 6, 0)
        layoutGauche.addWidget(self.LEdateplantation, 6, 1)
        layoutGauche.addWidget(self.LBLduree, 7, 0)
        layoutGauche.addWidget(self.LEduree, 7, 1)
        layoutGauche.addWidget(self.LBLarrosage, 8, 0)
        layoutGauche.addWidget(self.LEarrosage, 8, 1)
        layoutGauche.addWidget(self.LBLsol, 9, 0)
        layoutGauche.addWidget(self.LEsol, 9, 1)
        layoutGauche.addWidget(self.LBLassoc, 10, 0)
        layoutGauche.addWidget(self.LEassoc, 10, 1)
        layoutGauche.addWidget(self.LBLtempgerm, 11, 0)
        layoutGauche.addWidget(self.LEtempgerm, 11, 1)
        layoutGauche.addWidget(self.LBLtypedeplante, 12, 0)
        layoutGauche.addWidget(self.LEtypedeplante, 12, 1)
        layoutGauche.addWidget(self.LBLcouleurdeplante, 13, 0)
        layoutGauche.addWidget(self.LEcouleurdeplante, 13, 1)
        layoutGauche.addWidget(self.LBLemplacement, 14, 0)
        layoutGauche.addWidget(self.LEemplacement, 14, 1)
        layoutGauche.addWidget(self.LBLfeuillagepersistant, 15, 0)
        layoutGauche.addWidget(self.CHKBOXfeuillagepersistant, 15, 1)
        layoutGauche.addWidget(self.LBLmellifere, 16, 0)
        layoutGauche.addWidget(self.CHKBOXmellifere, 16, 1)
        layoutGauche.addWidget(self.LBLmoisdefloraison, 17, 0)
        layoutGauche.addWidget(self.LEmoisdefloraison, 17, 1)
        layoutGauche.addWidget(self.LBLmoisderecolte, 18, 0)
        layoutGauche.addWidget(self.LEmoisderecolte, 18, 1)
        layoutGauche.addWidget(self.LBLplanteparfumee, 19, 0)
        layoutGauche.addWidget(self.CHKBOXplanteparfumee, 19, 1)
        layoutGauche.addWidget(self.LBLplantevivace, 20, 0)
        layoutGauche.addWidget(self.CHKBOXplantevivace, 20, 1)
        layoutGauche.addWidget(self.LBLcheminaccesimage, 21, 0)
        layoutGauche.addWidget(self.LEcheminaccesimage, 21, 1)
        layoutGauche.setVerticalSpacing(5)

        # ajout boutons au layout droit
        widget.setLayout(layoutPrincipal)
        self.setCentralWidget(widget)
        self.resize(1280, 1024)
