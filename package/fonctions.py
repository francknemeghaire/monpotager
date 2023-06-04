class Plante:
    """création structure pour bdd de plantes"""

    def __init__(self):
        self.nom = ""
        self.taille = 0
        self.typesol = ""
        self.arrosage = ""
        self.associations = ""
        self.Datesemis = ""
        self.Temperaturegermination = ""

    "création méthode d'ajout d'un nom de plante"


Planteajoutee = Plante()
tamponplantes = []

def ajoutplante():
    reponse = "O"
    while reponse == "O":
        Planteajoutee.nom = input("Quel est le nom de la plante ? ")
        Planteajoutee.taille = input("Quelle est sa taille ? ")
        Planteajoutee.typesol = input("Dans quel type de sol peut-on la planter ? ")
        tamponplantes.append((Planteajoutee.nom, Planteajoutee.taille, Planteajoutee.typesol))
        reponse = input("Faut-il ajouter des plantes (O/N) ? ")


def affichageplante():
    # print("le nom de la plante est ", Planteajoutee.nom, " et sa taille est de ", str(Planteajoutee.taille), '\n')
    # print("le type de sol pour cette plante est le suivant : ", Planteajoutee.typesol, '\n')
    print("Les plantes encodées jusqu'à présent sont les suivantes :\n")
    for indexNom in range(len(tamponplantes)):
        print("le nom de la plante est ", tamponplantes[indexNom][0], " et sa taille est de ",
              str(tamponplantes[indexNom][1]), ' cm\n')
        print("le type de sol pour cette plante est le suivant : ", tamponplantes[indexNom][2], '\n')


def testchoixmenu(s):
    addplante = moteur.AjoutPlante()
    addplante.show()
