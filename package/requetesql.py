import sqlite3

def maj_bdd(tampon):
    """ajout à la bdd"""
    connection = sqlite3.connect("./plantes.db")
    cursor = connection.cursor()
    cursor.executemany("""
    INSERT INTO plantes (nom, taille, typedesol) VALUES (?, ?, ?)""", tampon)
    connection.commit()
    connection.close()

def affichercontenubdd():
    connection = sqlite3.connect("./plantes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plantes")
    plantedelabdd = cursor.fetchall()
    #return plantedelabdd[0][1], plantedelabdd[1][1], plantedelabdd[2][1]
    for indexNom in range(len(plantedelabdd)):
        print("le nom de la plante est ", plantedelabdd[indexNom][1], " et sa taille est de ", str(plantedelabdd[indexNom][2]), ' cm\n')
        print("le type de sol pour cette plante est le suivant : ", plantedelabdd[indexNom][3], '\n')
    connection.close()
