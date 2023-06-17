import sqlite3


def creationBDD():
    # connexion à la base de données
    connection = sqlite3.connect("plantes")
    c = connection.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS products
              ([plante_id] INTEGER PRIMARY KEY,
                [nom] TEXT,
                [hauteur] INTEGER)
              ''')
    connection.commit()
