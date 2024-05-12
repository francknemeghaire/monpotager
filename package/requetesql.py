import sqlite3

def maj_bdd(tampon):
    """ajout à la bdd"""
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    requetesql = "insert into plantes (nom, envergure, hauteur, exposition, datedesemi, datedeplantation, dureedevie, typearrosage, typedesol, association, temperaturegermination, typedeplante, couleur, emplacement, feuillagepersistant, mellifere, moisdefloraison, moisderecolte, planteparfumee, plantevivace) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?)"
    cursor.executemany(requetesql, tampon)
    # cursor.executemany("""
    # INSERT INTO plantes (
    # id,
    # nom,
    # envergure,
    # hauteur,
    # exposition,
    # datedesemis,
    # datedeplantation,
    # dureedevie,
    # typearrosage,
    # typedesol,
    # association,
    # temperaturegermination,
    # typedeplante,
    # couleur,
    # emplacement,
    # feuillagepersistant,
    # mellifere,
    # moisdefloraison,`
    # moisderecolte,
    # planteparfumee,
    # plantevivace) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?)""", tampon)"""
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


