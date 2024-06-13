import sqlite3

def maj_bdd(tampon):
    """ajout à la bdd"""
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    requetesql = "insert into plantes (nom, envergure, hauteur, exposition, datedesemi, datedeplantation, dureedevie, typearrosage, typedesol, association, temperaturegermination, typedeplante, couleur, emplacement, feuillagepersistant, mellifere, moisdefloraison, moisderecolte, planteparfumee, plantevivace) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?)"
    cursor.executemany(requetesql, tampon)
    connection.commit()
    connection.close()

def tailledelabdd():
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM plantes")
    record_count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return record_count



