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
              ([id] LONG NOT NULL PRIMARY KEY,
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
              [moisdefloraison] INTEGER,
              [moisderecolte] INTEGER,
              [planteparfumee] INTEGER,
              [plantevivace] INTEGER  
              )
              ''')
    connection.commit()
    connection.close()
