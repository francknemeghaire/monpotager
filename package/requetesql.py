import sqlite3

def maj_bdd(tampon):
    """ajout à la bdd"""
    connection = sqlite3.connect("plantes.db")
    cursor = connection.cursor()
    requetesql = "insert into plantes (nom, envergure, hauteur, exposition, datedesemi, datedeplantation, dureedevie, typearrosage, typedesol, association, temperaturegermination, typedeplante, couleur, emplacement, feuillagepersistant, mellifere, moisdefloraison, moisderecolte, planteparfumee, plantevivace, cheminaccesimage) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?)"
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

def modification_fiche(nom, envergure, hauteur, exposition, datedesemi, datedeplantation, dureedevie, typearrosage, typedesol, association, temperaturegermination, typedeplante, couleur, emplacement, feuillagepersistant, mellifere, moisdefloraison, moisderecolte, planteparfumee, plantevivace, cheminaccesimage, id_de_bdd):
    # 21 champs
    id = id_de_bdd
    nom = nom
    envergure = envergure
    hauteur = hauteur
    exposition = exposition
    datedesemi = datedesemi
    datedeplantation = datedeplantation
    dureedevie = dureedevie
    typearrosage = typearrosage
    typedesol = typedesol
    association = association
    temperaturegermination = temperaturegermination
    typedeplante = typedeplante
    couleur = couleur
    emplacement = emplacement
    feuillagepersistant = feuillagepersistant
    mellifere = mellifere
    moisdefloraison = moisdefloraison
    moisderecolte = moisderecolte
    planteparfumee = planteparfumee
    plantevivace = plantevivace
    cheminaccesimage = cheminaccesimage

    sql = ('UPDATE plantes SET colonne1=?, colonne2=?, colonne3=?, colonne4=?, colonne5=?, colonne7=?, colonne8=?, colonne9=?, colonne10=?, colonne11=?, colonne12=?, colonne13=?, colonne14=?, colonne15=?, colonne16=?, colonne17=?, colonne18=?, colonne19=?, colonne20=?, colonne21=?  WHERE id = ?')

    try:
        with sqlite3.connect(database) as conn:
            cur = conn.cursor()
            cur.execute(sql, (nom, envergure, hauteur, exposition, datedesemi, datedeplantation, dureedevie, typearrosage, typedesol, association, temperaturegermination, typedeplante, couleur, emplacement, feuillagepersistant, mellifere, moisdefloraison, moisderecolte, planteparfumee, plantevivace, cheminaccesimage, id))
            conn.commit()
    except sqlite3.OperationalError as e:
        print(e)


