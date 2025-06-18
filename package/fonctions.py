import os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sqlite3
from package import requetesql
from SubApplication import Fenaffichagebasededonnee
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet



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

Plantemodifiee = Plante()

#def parcourirlabasededonnee(self):
#        connection = sqlite3.connect("plantes.db")
#        cursor = connection.cursor()
#        sqlstr = 'SELECT * FROM plantes'
#        plantedelabdd = cursor.execute(sqlstr)
#        donnees = plantedelabdd.fetchall()
#        for plante in donnees:
#            print(plante)


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
    def __init__(self, id):
        super().__init__()
        self.id_plante = id
        self.setWindowTitle("Modifier une fiche plante")
        self.setGeometry(100, 100, 800, 600)
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
        TLBadd = QAction(QIcon(os.path.join("icons", "plus.png")), "Ajouter", self)
        TLBadd.triggered.connect(self.modifierplante)
        toolbar.addAction(TLBadd)
        #
        # lire l'id de la plante pour afficher les données dans les champs
        connection = sqlite3.connect("plantes.db")
        cursor = connection.cursor()
        sqlstr = 'SELECT * FROM plantes WHERE id = ?'
        plantedelabdd = cursor.execute(sqlstr, (self.id_plante,))
        for row in plantedelabdd:
            print(row[1])
        #self.PlanteAModifier = self.import_bdd_data(self.id_plante)
        # mettre les données dans les champs
        #
        self.LBLid = QLabel("id de la plante?: ")
        self.LEid = QLineEdit(str(self.id_plante))
        self.LEid.setReadOnly(True)
        self.LBLnom = QLabel("Quel est le nom de la plante? ")
        self.LEnom = QLineEdit(row[1])
        self.LBLenvergure = QLabel("Quelle est son envergure? ")
        self.LEenvg = QLineEdit(str(row[2]))
        self.LBLht = QLabel("Quelle est la hauteur de la plante? ")
        self.LEht = QLineEdit(str(row[3]))
        self.LBLexpo = QLabel("A quelle exposition peut on la planter (ombre, mi-ombre, etc): ")
        self.LEexpo = QLineEdit(row[4])
        self.LBLdatesemis = QLabel("Quand peut-on débuter les semis: ")
        self.LEdatesemis = QLineEdit(row[5])
        self.LBLdateplantation = QLabel("Quand peut on les mettre en pleine terre: ")
        self.LEdateplantation = QLineEdit(row[6])
        self.LBLduree = QLabel("combien de temps occupe-t-il l'espace octroyer dans le jardin? ")
        self.LEduree = QLineEdit(str(row[7]))
        self.LBLarrosage = QLabel("Quel est son besoin en eau? ")
        self.LEarrosage = QLineEdit(row[8])
        self.LBLsol = QLabel("Quelle doit être la richesse du sol? ")
        self.LEsol = QLineEdit(row[9])
        self.LBLassoc = QLabel("Avec quelles autres plantes peut-on l'associer? ")
        self.LEassoc = QLineEdit(row[10])
        self.LBLtempgerm = QLabel("Quelle est la température de germination? ")
        self.LEtempgerm = QLineEdit(str(row[11]))
        # ajout caractéristique supplémentaires 8/5/24
        self.LBLtypedeplante = QLabel("Quelle type de plante est-ce ? ")
        self.LEtypedeplante = QLineEdit(row[12])
        self.LBLcouleurdeplante = QLabel("Quelle est la couleur de la plante ?")
        self.LEcouleurdeplante = QLineEdit(row[13])
        self.LBLemplacement = QLabel("Où va-t-on placer cette plante? ")
        self.LEemplacement = QLineEdit(row[14])
        self.LBLfeuillagepersistant = QLabel("Est-ce une plante avec un feuillage persistant ?")
        #row[15] = 1 si oui, 0 si non
        self.CHKBOXfeuillagepersistant = QCheckBox()
        if row[15] == 1:
            self.CHKBOXfeuillagepersistant.setChecked(True)
        else:
            self.CHKBOXfeuillagepersistant.setChecked(False)
        self.LBLmellifere = QLabel("Est-ce un mellifère ?")
        self.CHKBOXmellifere = QCheckBox()
        if row[16] == 1:
            self.CHKBOXmellifere.setChecked(True)
        else:
            self.CHKBOXmellifere.setChecked(False)
        self.LBLmoisdefloraison = QLabel("Quelle est la mois de floraison ?")
        self.LEmoisdefloraison = QLineEdit(row[17])
        self.LBLmoisderecolte = QLabel("Quel est le mois de recolte ?")
        self.LEmoisderecolte = QLineEdit(row[18])
        self.LBLplanteparfumee = QLabel("La plante est-elle parfumée ?")
        self.CHKBOXplanteparfumee = QCheckBox()
        if row[19] == 1:
            self.CHKBOXplanteparfumee.setChecked(True)
        else:
            self.CHKBOXplanteparfumee.setChecked(False)
        self.LBLplantevivace = QLabel("Est-ce une plante vivace ?")
        self.CHKBOXplantevivace = QCheckBox()
        if row[20] == 1:
            self.CHKBOXplantevivace.setChecked(True)
        else:
            self.CHKBOXplantevivace.setChecked(False)
        # partie du code pour traitement des photos
        self.LBLcheminaccesimage = QLabel("chemin d'accès de la photo ?")
        self.LEcheminaccesimage = QLineEdit(row[21])

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
    
    def modifierplante(self):
        # ajouter la plante au tampon avant la sauvegarde dans la BDD
        Plantemodifiee.nom = self.LEnom.text()
        Plantemodifiee.hauteur = self.LEht.text()
        Plantemodifiee.envergure = self.LEenvg.text()
        Plantemodifiee.exposition = self.LEexpo.text()
        Plantemodifiee.datedesemis = self.LEdatesemis.text()
        Plantemodifiee.datedeplantation = self.LEdateplantation.text()
        Plantemodifiee.duree = self.LEduree.text()
        Plantemodifiee.arrosage = self.LEarrosage.text()
        Plantemodifiee.typesol = self.LEsol.text()
        Plantemodifiee.associations = self.LEassoc.text()
        Plantemodifiee.temperaturegermination = self.LEtempgerm.text()
        Plantemodifiee.type = self.LEtypedeplante.text()
        Plantemodifiee.couleur = self.LEcouleurdeplante.text()
        Plantemodifiee.emplacement = self.LEemplacement.text()
        Plantemodifiee.feuillagepersistant = self.CHKBOXfeuillagepersistant.isEnabled()
        Plantemodifiee.mellifere = self.CHKBOXmellifere.isEnabled()
        Plantemodifiee.moisdefloraison = self.LEmoisdefloraison.text()
        Plantemodifiee.moisderecolte = self.LEmoisderecolte.text()
        Plantemodifiee.planteparfumee = self.CHKBOXplanteparfumee.isEnabled()
        Plantemodifiee.plantevivace = self.CHKBOXplantevivace.isEnabled()
        Plantemodifiee.cheminaccesimage = self.LEcheminaccesimage.text()
        id_de_bdd = self.LEid.text()
        # sauvegarde de la plante dans la BDD
        requetesql.modification_fiche(Plantemodifiee.nom, Plantemodifiee.hauteur, Plantemodifiee.envergure, Plantemodifiee.exposition, Plantemodifiee.datedesemis, Plantemodifiee.datedeplantation, Plantemodifiee.duree, Plantemodifiee.arrosage, Plantemodifiee.typesol, Plantemodifiee.associations, Plantemodifiee.temperaturegermination, Plantemodifiee.type, Plantemodifiee.couleur, Plantemodifiee.emplacement, Plantemodifiee.feuillagepersistant, Plantemodifiee.mellifere, Plantemodifiee.moisdefloraison, Plantemodifiee.moisderecolte, Plantemodifiee.planteparfumee, Plantemodifiee.plantevivace, Plantemodifiee.cheminaccesimage, id_de_bdd)
        self.close()

# fonction d'impression
# pour imprimer la fiche plante en pdf
# utiliser la librairie reportlab        
def impressionenpdf():
        # fonction pour imprimer la fiche plante en pdf
        # Chemin du fichier de sortie
        pdf_file = "fiche_plante/testfiche.pdf"

        # Crée le canvas (surface de dessin PDF)
        c = canvas.Canvas(pdf_file, pagesize = A4)
        textLines = "At last, we draw a picture on the pdf using the drawInlineImage function in which the parameters are the path of the image and the x and y coordinates of the image. In this case, the image was in the same directory as the py file, so according to the relative path, we need to write only the name of the file with the extension, if it was in some other directory, a relevant correct relative path should be used."
        p = Paragraph(textLines, style=['Normal'])
        # Déterminer la hauteur du texte
        #hauteur = p.wrap(c.getFilename(), c.getPageWidth() - 200)
        
    
        # Dessiner le paragraphe sur la page
        p.drawOn(c, 100, 750 - hauteur)

        c.save()
        # Finaliser le PDF
        c.showPage()