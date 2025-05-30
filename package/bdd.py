import sqlite3

#ordre des champs dans bdd à modifier!!!
"""champs à ajouter pour mise à jour bdd
    nom = models.CharField(max_length=200)
    envergure = models.IntegerField(default=0)
    hauteur = models.IntegerField(default=0)
    exposition = models.CharField(max_length=300)
    datedesemis = models.DateField()
    datedeplantation = models.DateField()
    dureedevie = models.IntegerField(default=0)
    typearrosage = models.CharField(max_length=200)
    typedesol = models.CharField(max_length=300)
    association = models.CharField(max_length=300)
    temperaturegermination = models.IntegerField()
    typedeplante = models.CharField(max_length=200)
    couleur = models.CharField(max_length=200)
    emplacement = models.CharField(max_length=300)
    feuillagepersistant = models.BooleanField(default=False)
    mellifere = models.BooleanField(default=False)
    moisdefloraison = models.CharField(max_length=50)
    moisderecolte = models.CharField(max_length=50)
    planteparfumee = models.BooleanField(default=False)
    plantevivace = models.BooleanField(default=False)
"""
def creationBDD():
    # connexion à la base de données
    connection = sqlite3.connect("plantes.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS plantes
              ([id] INTEGER PRIMARY KEY AUTOINCREMENT,
              [nom] TEXT,
              [envergure] INTEGER,
              [hauteur] INTEGER,
              [exposition] TEXT,
              [datedesemi] TEXT,
              [datedeplantation] TEXT,
              [dureedevie] INTEGER,
              [typearrosage] TEXT,
              [typedesol] TEXT,
              [association] TEXT,
              [temperaturegermination] INTEGER,
              [typedeplante] TEXT,
              [couleur] TEXT,
              [emplacement] TEXT,
              [feuillagepersistant] INTEGER,
              [mellifere] INTEGER,
              [moisdefloraison] TEXT,
              [moisderecolte] TEXT,
              [planteparfumee] INTEGER,
              [plantevivace] INTEGER,
              [cheminaccesimage] TEXT 
              )
              ''')
    connection.commit()
    connection.close()

def creationbddtaches():
    # connexion à la base de données
    connection = sqlite3.connect("taches.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS taches
              ([id] INTEGER PRIMARY KEY AUTOINCREMENT,
              [nom] TEXT,
              [date] TEXT,
              [heure] TEXT,
              [description] TEXT,
              [priorite] INTEGER
              )
              ''')
    connection.commit()
    connection.close()
def creationbdddiagnostic():
    # connexion à la base de données
    connection = sqlite3.connect("diagnostic.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS diagnostic
              ([id] INTEGER PRIMARY KEY AUTOINCREMENT,
              [nom] TEXT,
              [symptome] TEXT,
              [solution] TEXT
              )
              ''')
    connection.commit()
    connection.close()
def creationbddcalendrier():
    # connexion à la base de données
    connection = sqlite3.connect("calendrier.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS calendrier
              ([id] INTEGER PRIMARY KEY AUTOINCREMENT,
              [nom] TEXT,
              [date] TEXT,
              [description] TEXT
              )
              ''')
    connection.commit()
    connection.close()
def creationbddhistorique():
    # connexion à la base de données
    connection = sqlite3.connect("historique.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS historique
              ([id] INTEGER PRIMARY KEY AUTOINCREMENT,
              [nom] TEXT,
              [date] TEXT,
              [description] TEXT
              )
              ''')
    connection.commit()
    connection.close()