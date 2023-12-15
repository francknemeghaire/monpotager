import sqlite3

def maj_bdd(tampon):
    """ajout à la bdd"""
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    cursor.executemany("""
    INSERT INTO plantes (
    nom,
    envergure,
    exposition,
    datesemis,
    dateplantation,
    duree,
    arrosage,
    sol,
    association,
    tempgermination,
    type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", tampon)
    connection.commit()
    connection.close()

def affichercontenubdd():
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plantes")
    plantedelabdd = cursor.fetchall()
    for indexNom in range(len(plantedelabdd)):
        return plantedelabdd[indexNom]
    connection.close()

def tailledelabdd():
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plantes")
    plantedelabdd = cursor.fetchall()
    return len(plantedelabdd)
    connection.close()


