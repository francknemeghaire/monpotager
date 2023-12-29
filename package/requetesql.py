import sqlite3

def maj_bdd(tampon):
    """ajout à la bdd"""
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    cursor.executemany("""
    INSERT INTO plantes (
    nom,
    taille,
    envergure,
    exposition,
    datesemis,
    dateplantation,
    duree,
    arrosage,
    sol,
    association,
    tempgermination,
    type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", tampon)
    connection.commit()
    connection.close()

def affichercontenubdd():
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    sqlstr = 'SELECT * FROM plantes LIMIT 40'
    plantedelabdd = cursor.execute(sqlstr)
    for indexNom in range(12):
        print(plantedelabdd)
    connection.close()

def tailledelabdd():
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plantes")
    plantedelabdd = cursor.fetchall()
    return len(plantedelabdd)
    connection.close()


