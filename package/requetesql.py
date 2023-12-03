import sqlite3
# chermin d'accès à la bdd?' à corriger?

"""champs à ajouter pour mise à jour bdd
Planteajoutee.nom
Planteajoutee.envergure
Planteajoutee.exposition
Planteajoutee.datedesemis
Planteajoutee.datedeplantation
Planteajoutee.duree
Planteajoutee.arrosage
Planteajoutee.typesol
Planteajoutee.associations
Planteajoutee.temperaturegermination
Planteajoutee.type))"""
def maj_bdd(tampon, repertoire):
    """ajout à la bdd"""
    connection = sqlite3.connect("./plantes.db")
    cursor = connection.cursor()
    cursor.executemany("""
    INSERT INTO plantes (
    nom,
    envergure,
    exposition,
    datedesemis,
    datedeplantation,
    duree,
    arrosage,
    typedesol,
    associations,
    temperaturegermination,
    type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", tampon)
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
