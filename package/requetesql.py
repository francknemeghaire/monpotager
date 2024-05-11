import sqlite3
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
def maj_bdd(tampon):
    """ajout à la bdd"""
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    cursor.executemany("""
    INSERT INTO plantes (
    id,
    nom,
    envergure,
    hauteur,
    exposition,
    datedesemis,
    datedeplantation,
    dureedevie,
    typearrosage,
    typedesol,
    association,
    temperaturegermination,
    typedeplante,
    couleur,
    emplacement,
    feuillagepersistant,
    mellifere,
    moisdefloraison,`
    moisderecolte,
    planteparfumee,
    plantevivace) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?)""", tampon)
    connection.commit()
    connection.close()

def affichercontenubdd():
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    sqlstr = 'SELECT * FROM plantes LIMIT 40'
    plantedelabdd = cursor.execute(sqlstr)
    for indexNom in range(20):
        print(plantedelabdd)
    connection.close()

def tailledelabdd():
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plantes")
    plantedelabdd = cursor.fetchall()
    return len(plantedelabdd)
    connection.close()


