from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import *
from package import requetesql


class Plante:
    """création structure pour bdd de plantes"""

    def __init__(self):
        self.nom = ""
        self.envergure = 0
        self.hauteur = 0
        self.exposition = ""
        self.datedesemis = ""
        self.datedeplantation = ""
        self.duree = ""
        self.arrosage = ""
        self.typesol = ""
        self.associations = ""
        self.temperaturegermination = 0
        self.type = ""
        self.couleur = ""
        self.emplacement = ""
        self.feuillagepersistant = 0
        self.mellifere = 0
        self.moisdefloraison = ""
        self.moisderecolte = ""
        self.planteparfumee = 0
        self.plantevivace = 0

    "création méthode d'ajout d'un nom de plante"


Planteajoutee = Plante()
tamponplantes = []


class Fenetreajoutplante(QWidget):
    def __init__(self):
        super().__init__()
        layoutPrincipal = QHBoxLayout(self)
        layoutGauche = QGridLayout(self)
        layoutDroit = QVBoxLayout(self)
        layoutDroitHaut = QGridLayout(self)
        layoutDroitBas = QVBoxLayout(self)
        layoutPrincipal.addLayout(layoutGauche)
        layoutPrincipal.addLayout(layoutDroit)
        layoutDroit.addLayout(layoutDroitHaut)
        layoutDroit.addLayout(layoutDroitBas)
        barrededefilement = QScrollArea()
        barrededefilement.setAlignment(Qt.AlignRight)
        barrededefilement.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        barrededefilement.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        barrededefilement.setWidgetResizable(True)


        self.setWindowTitle("fenêtre d'ajout de plante")
        self.LBLnom = QLabel("Quel est le nom de la plante? ")
        self.LEnom = QLineEdit()
        self.LBLenvergure = QLabel("Quelle est son envergure? ")
        self.LEenvg = QLineEdit()
        self.LBLht = QLabel("Quelle est la hauteur de la plante? ")
        self.LEht = QLineEdit()
        self.LBLexpo = QLabel("A quelle exposition peut on la planter (ombre, mi-ombre, etc): ")
        self.LEexpo = QLineEdit()
        self.LBLdatesemis = QLabel("Quand peut-on débuter les semis: ")
        self.LEdatesemis = QLineEdit()
        self.LBLdateplantation = QLabel("Quand peut on les mettre en pleine terre: ")
        self.LEdateplantation = QLineEdit()
        self.LBLduree = QLabel("combien de temps occupe-t-il l'espace octroyer dans le jardin? ")
        self.LEduree = QLineEdit()
        self.LBLarrosage = QLabel("Quel est son besoin en eau? ")
        self.LEarrosage = QLineEdit()
        self.LBLsol = QLabel("Quelle doit être la richesse du sol? ")
        self.LEsol = QLineEdit()
        self.LBLassoc = QLabel("Avec quelles autres plantes peut-on l'associer? ")
        self.LEassoc = QLineEdit()
        self.LBLtempgerm = QLabel("Quelle est la température de germination? ")
        self.LEtempgerm = QLineEdit()
        #ajout caractéristique supplémentaires 8/5/24
        self.LBLtypedeplante = QLabel("Quelle type de plante est-ce ? ")
        self.LEtypedeplante = QLineEdit()
        self.LBLcouleurdeplante = QLabel("Quelle est la couleur de la plante ?")
        self.LEcouleurdeplante = QLineEdit()
        self.LBLemplacement = QLabel("Où va-t-on placer cette plante? ")
        self.LEemplacement = QLineEdit()
        self.LBLfeuillagepersistant = QLabel("Est-ce une plante avec un feuillage persistant ?")
        self.CHKBOXfeuillagepersistant = QCheckBox()
        self.CHKBOXfeuillagepersistant.setChecked(False)
        self.LBLmellifere = QLabel("Est-ce un mellifère ?")
        self.CHKBOXmellifere = QCheckBox()
        self.CHKBOXmellifere.setChecked(False)
        self.LBLmoisdefloraison = QLabel("Quelle est la mois de floraison ?")
        self.LEmoisdefloraison = QLineEdit()
        self.LBLmoisderecolte = QLabel("Quel est le mois de recolte ?")
        self.LEmoisderecolte = QLineEdit()
        self.LBLplanteparfumee = QLabel("La plante est-elle parfumée ?")
        self.CHKBOXplanteparfumee = QCheckBox()
        self.CHKBOXplanteparfumee.setChecked(False)
        self.LBLplantevivace = QLabel("Est-ce une plante vivace ?")
        self.CHKBOXplantevivace = QCheckBox()
        self.CHKBOXplantevivace.setChecked(False)

        # ajout widget layout gauche
        layoutGauche.addWidget(self.LBLnom, 0, 0)
        layoutGauche.addWidget(self.LEnom, 0, 1)
        layoutGauche.addWidget(self.LBLenvergure, 1, 0)
        layoutGauche.addWidget(self.LEenvg, 1, 1)
        layoutGauche.addWidget(self.LBLht, 2, 0)
        layoutGauche.addWidget(self.LEht, 2, 1)
        layoutGauche.addWidget(self.LBLexpo, 3, 0)
        layoutGauche.addWidget(self.LEexpo, 3, 1)
        layoutGauche.addWidget(self.LBLdatesemis, 4, 0)
        layoutGauche.addWidget(self.LEdatesemis, 4, 1)
        layoutGauche.addWidget(self.LBLdateplantation, 5, 0)
        layoutGauche.addWidget(self.LEdateplantation, 5, 1)
        layoutGauche.addWidget(self.LBLduree, 6, 0)
        layoutGauche.addWidget(self.LEduree, 6, 1)
        layoutGauche.addWidget(self.LBLarrosage, 7, 0)
        layoutGauche.addWidget(self.LEarrosage, 7, 1)
        layoutGauche.addWidget(self.LBLsol, 8, 0)
        layoutGauche.addWidget(self.LEsol, 8, 1)
        layoutGauche.addWidget(self.LBLassoc, 9, 0)
        layoutGauche.addWidget(self.LEassoc, 9, 1)
        layoutGauche.addWidget(self.LBLtempgerm, 10, 0)
        layoutGauche.addWidget(self.LEtempgerm, 10, 1)
        layoutGauche.addWidget(self.LBLtypedeplante, 11, 0)
        layoutGauche.addWidget(self.LEtypedeplante, 11, 1)
        layoutGauche.addWidget(self.LBLcouleurdeplante, 12, 0)
        layoutGauche.addWidget(self.LEcouleurdeplante, 12, 1)
        layoutGauche.addWidget(self.LBLemplacement, 13, 0)
        layoutGauche.addWidget(self.LEemplacement, 13, 1)
        layoutGauche.addWidget(self.LBLfeuillagepersistant, 14, 0)
        layoutGauche.addWidget(self.CHKBOXfeuillagepersistant, 14, 1)
        layoutGauche.addWidget(self.LBLmellifere, 15, 0)
        layoutGauche.addWidget(self.CHKBOXmellifere, 15, 1)
        layoutGauche.addWidget(self.LBLmoisdefloraison, 16, 0)
        layoutGauche.addWidget(self.LEmoisdefloraison, 16, 1)
        layoutGauche.addWidget(self.LBLmoisderecolte, 17, 0)
        layoutGauche.addWidget(self.LEmoisderecolte, 17, 1)
        layoutGauche.addWidget(self.LBLplanteparfumee, 18, 0)
        layoutGauche.addWidget(self.CHKBOXplanteparfumee, 18, 1)
        layoutGauche.addWidget(self.LBLplantevivace, 19, 0)
        layoutGauche.addWidget(self.CHKBOXplantevivace, 19, 1)
        layoutGauche.addWidget(barrededefilement)


        # bouton de commande layout droit
        btnSauvegarde = QPushButton("Sauvegarde", self)
        btnRecherche = QPushButton("Rechercher", self)
        btnAjouter = QPushButton("Ajouter", self)
        btnSupprimer = QPushButton("Supprimer", self)
        btnQuitter = QPushButton("Quitter", self)
        btnQuitter.clicked.connect(self.quitterajoutplante)
        btnSauvegarde.clicked.connect(self.sauvegardeplantes)
        btnRecherche.clicked.connect(self.rechercherplante)
        btnAjouter.clicked.connect(self.ajouterplante)
        btnSupprimer.clicked.connect(self.supprimerplante)

        # ajout boutons au layout droit
        layoutDroitBas.addWidget(btnAjouter)
        layoutDroitBas.addWidget(btnRecherche)
        layoutDroitBas.addWidget(btnSauvegarde)
        layoutDroitBas.addWidget(btnSupprimer)
        layoutDroitBas.addWidget(btnQuitter)
        layoutDroitBas.setAlignment(Qt.AlignLeft)
        layoutDroitBas.setAlignment(Qt.AlignBottom)
        self.setLayout(layoutPrincipal)
        self.resize(800, 400)

    def quitterajoutplante(self):
        self.close()

    def sauvegardeplantes(self):
        self.sourcesdeplantesdepotager()

    def rechercherplante(self):
        pass

    def ajouterplante(self):
        # ajouter la plante au tampon avant la sauvegarde dans la BDD
        Planteajoutee.nom = self.LEnom.text()
        Planteajoutee.hauteur = self.LEht.text()
        Planteajoutee.envergure = self.LEenvg.text()
        Planteajoutee.exposition = self.LEexpo.text()
        Planteajoutee.datedesemis = self.LEdatesemis.text()
        Planteajoutee.datedeplantation = self.LEdateplantation.text()
        Planteajoutee.duree = self.LEduree.text()
        Planteajoutee.arrosage = self.LEarrosage.text()
        Planteajoutee.typesol = self.LEsol.text()
        Planteajoutee.associations = self.LEassoc.text()
        Planteajoutee.temperaturegermination = self.LEtempgerm.text()
        Planteajoutee.type = self.LEtypedeplante.text()
        Planteajoutee.couleur = self.LEcouleurdeplante.text()
        Planteajoutee.emplacement = self.LEemplacement.text()
        Planteajoutee.feuillagepersistant = self.CHKBOXfeuillagepersistant.isEnabled()
        Planteajoutee.mellifere = self.CHKBOXmellifere.isEnabled()
        Planteajoutee.moisdefloraison = self.LEmoisdefloraison.text()
        Planteajoutee.moisderecolte = self.LEmoisderecolte.text()
        Planteajoutee.planteparfumee = self.CHKBOXplanteparfumee.isEnabled()
        Planteajoutee.plantevivace = self.CHKBOXplantevivace.isEnabled()
        tamponplantes.append((Planteajoutee.nom, Planteajoutee.hauteur, Planteajoutee.envergure, Planteajoutee.exposition, Planteajoutee.datedesemis, Planteajoutee.datedeplantation, Planteajoutee.duree, Planteajoutee.arrosage, Planteajoutee.typesol, Planteajoutee.associations, Planteajoutee.temperaturegermination, Planteajoutee.type, Planteajoutee.couleur, Planteajoutee.emplacement, Planteajoutee.feuillagepersistant, Planteajoutee.mellifere, Planteajoutee.moisdefloraison, Planteajoutee.moisderecolte, Planteajoutee.planteparfumee, Planteajoutee.plantevivace))
        requetesql.maj_bdd(tamponplantes)
        tamponplantes.clear()

    def supprimerplante(self):
        pass
    def parcourirlabasededonnee(self):
        connection = sqlite3.connect("plantes.db")
        cursor = connection.cursor()
        sqlstr = 'SELECT * FROM plantes'
        plantedelabdd = cursor.execute(sqlstr)
        donnees = plantedelabdd.fetchall()
        for plante in donnees:
            print(plante)

        #en cours de création
    def sourcesdeplantesdepotager(self):
        plantes_de_potager = [
            "Allium cepa - Oignon",
            "Solanum lycopersicum - Tomate",
            "Cucumis sativus - Concombre",
            "Daucus carota - Carotte",
            "Brassica oleracea var. capitata - Chou",
            "Lactuca sativa - Laitue",
            "Phaseolus vulgaris - Haricot vert",
            "Pisum sativum - Pois",
            "Capsicum annuum - Poivron",
            "Cucurbita pepo - Courgette",
            "Raphanus sativus - Radis",
            "Spinacia oleracea - Épinard",
            "Solanum melongena - Aubergine",
            "Beta vulgaris - Betterave",
            "Zea mays - Maïs",
            "Brassica oleracea var. italica - Brocoli",
            "Allium sativum - Ail",
            "Brassica rapa - Navet",
            "Apium graveolens - Céleri",
            "Brassica napus - Rutabaga",
            "Cichorium intybus - Chicorée",
            "rassica oleracea var. gemmifera - Chou de Bruxelles",
            "Brassica oleracea var. botrytis - Chou-fleur",
            "Rheum rhabarbarum - Rhubarbe",
            "Fragaria × ananassa - Fraise",
            "Rubus idaeus - Framboise",
            "Ribes nigrum - Cassis",
            "Ribes uva-crispa - Groseille",
            "Vaccinium corymbosum - Myrtille",
            "Rubus fruticosus - Mûre",
            "Asparagus officinalis - Asperge",
            "Cynara scolymus - Artichaut",
            "Solanum tuberosum - Pomme de terre",
            "Ipomoea batatas - Patate douce",
            "Cichorium endivia - Endive",
            "Vigna unguiculata - Pois à vache",
            "Brassica juncea - Moutarde brune",
            "Petroselinum crispum - Persil",
            "Anethum graveolens - Aneth",
            "Thymus vulgaris - Thym",
            "Rosmarinus officinalis - Romarin",
            "Ocimum basilicum - Basilic",
            "Origanum vulgare - Origan",
            "Salvia officinalis - Sauge",
            "Mentha spicata - Menthe",
            "Coriandrum sativum - Coriandre",
            "Lavandula angustifolia - Lavande",
            "Foeniculum vulgare - Fenouil",
            "Nasturtium officinale - Cresson",
            "Taraxacum officinale - Pissenlit",
            "Armoracia rusticana - Raifort",
            "Levisticum officinale - Livèche",
            "Hyssopus officinalis - Hysope",
            "Melissa officinalis - Mélisse",
            "Valeriana officinalis - Valériane",
            "Ruta graveolens - Rue",
            "Satureja hortensis - Sarriette",
            "Allium ampeloprasum - Poireau",
            "Brassica oleracea var. acephala - Chou frisé",
            "Helianthus tuberosus - Topinambour",
            "Pastinaca sativa - Panais",
            "Scorzonera hispanica - Salsifis",
            "Foeniculum vulgare - Fenouil",
            "Allium fistulosum - Ciboule",
            "Allium schoenoprasum - Ciboulette",
            "Rumex acetosa - Oseille",
            "Portulaca oleracea - Pourpier",
            "Tetragonia tetragonioides - Tétragone",
            "Chenopodium quinoa - Quinoa",
            "Eruca vesicaria - Roquette",
            "Brassica oleracea var. gongylodes - Chou-rave",
            "Crambe maritima - Chou marin",
            "Lepidium sativum - Cresson alénois",
            "Brassica rapa subsp. chinensis - Pak-choï",
            "Brassica rapa subsp. pekinensis - Chou chinois",
            "Brassica oleracea var. viridis - Collard",
            "Brassica oleracea var. alboglabra - Chou kale",
            "Lactuca sativa var. longifolia - Romaine",
            "Lactuca sativa var. crispa - Laitue frisée",
            "Cucumis melo - Melon",
            "Citrullus lanatus - Pastèque",
            "Fragaria vesca - Fraisier des bois",
            "Rubus idaeus strigosus - Framboisier rouge",
            "Ribes rubrum - Groseillier rouge",
            "Ribes uva-crispa var. reclinatum - Groseillier à maquereau",
            "Vaccinium macrocarpon - Canneberge",
            "Rubus occidentalis - Framboisier noir",
            "Juglans regia - Noyer",
            "Corylus avellana - Noisetier",
            "Prunus armeniaca - Abricotier",
            "Prunus domestica - Prunier",
            "Prunus persica - Pêcher",
            "Pyrus communis - Poirier",
            "Malus domestica - Pommier",
            "Carya ovata - Noyer blanc",
            "Diospyros kaki - Plaqueminier",
            "Punica granatum - Grenadier",
            "Ficus carica - Figuier",
            "Vitis vinifera - Vigne",
            "Olea europaea - Olivier",
            "Cydonia oblonga - Cognassier",
            "Fragaria × ananassa 'Albion' - Fraisier 'Albion'",
            "Fragaria × ananassa 'Mara des bois' - Fraisier 'Mara des bois'",
            "Vaccinium corymbosum 'Bluecrop' - Myrtillier 'Bluecrop'",
            "Vaccinium corymbosum 'Patriot' - Myrtillier 'Patriot'",
            "Rubus fruticosus 'Chester Thornless' - Mûrier 'Chester Thornless'",
            "Rubus fruticosus 'Loch Ness' - Mûrier 'Loch Ness'",
            "Rubus idaeus 'Autumn Bliss' - Framboisier 'Autumn Bliss'",
            "Rubus idaeus 'Glen Ample' - Framboisier 'Glen Ample'",
            "Ribes nigrum 'Ben Lomond' - Cassissier 'Ben Lomond'",
            "Ribes nigrum 'Titania' - Cassissier 'Titania'",
            "Ribes uva-crispa 'Invicta' - Groseillier 'Invicta'",
            "Ribes uva-crispa 'Hinnonmäki Röd' - Groseillier 'Hinnonmäki Röd'",
            "Vaccinium corymbosum 'Duke' - Myrtillier 'Duke'",
            "Vaccinium corymbosum 'Elliott' - Myrtillier 'Elliott'",
            "Rubus idaeus 'Tulameen' - Framboisier 'Tulameen'",
            "Rubus idaeus 'Heritage' - Framboisier 'Heritage'",
            "Prunus cerasus - Cerisier",
            "Prunus avium - Merisier",
            "Vaccinium myrtillus - Myrtille sauvage",
            "Rubus idaeus var. strigosus - Framboisier sauvage",
            "Rubus fruticosus var. inermis - Mûrier sauvage",
            "Ribes nigrum var. pungens - Cassissier sauvage",
            "Fragaria vesca var. semperflorens - Fraisier des bois",
            "Prunus spinosa - Prunellier",
            "Rubus caesius - Ronce bleue",
            "Fragaria chiloensis - Fraisier du Chili",
            "Fragaria virginiana - Fraisier de Virginie",
            "Vaccinium angustifolium - Myrtille basse",
            "Vaccinium myrtilloides - Myrtille fausse-airelle",
            "Vaccinium uliginosum - Myrtille des marais",
            "Vaccinium vitis-idaea - Airelle rouge",
            "Ribes oxyacanthoides - Groseillier épineux",
            "Ribes hirtellum - Groseillier hispidule",
            "Rubus allegheniensis - Mûrier Allegheny",
            "Rubus occidentalis var. strigosus - Framboisier occidental",
            "Rubus leucodermis - Framboisier blanc",
            "Rubus phoenicolasius - Framboisier rouge",
            "Rubus ursinus - Mûrier des montagnes",
            "Rubus armeniacus - Mûrier de l'Himalaya",
            "Rubus laciniatus - Mûrier à feuilles laciniées",
            "Rubus canadensis - Mûrier canadien",
            "Fragaria × ananassa 'Elsanta' - Fraisier 'Elsanta'",
            "Fragaria × ananassa 'Gariguette' - Fraisier 'Gariguette'",
            "Vaccinium corymbosum 'Bluejay' - Myrtillier 'Bluejay'",
            "Vaccinium corymbosum 'Brigitta' - Myrtillier 'Brigitta'",
            "Rubus fruticosus 'Navaho' - Mûrier 'Navaho'",
            "Rubus fruticosus 'Triple Crown' - Mûrier 'Triple Crown'",
            "Rubus idaeus 'Polka' - Framboisier 'Polka'",
            "Rubus idaeus 'Meeker' - Framboisier 'Meeker'",
            "Ribes nigrum 'Baldwin' - Cassissier 'Baldwin'",
            "Ribes nigrum 'Black Reward' - Cassissier 'Black Reward'",
            "Ribes uva-crispa 'Captivator' - Groseillier 'Captivator'",
            "Ribes uva-crispa 'Pixwell' - Groseillier 'Pixwell'",
            "Vaccinium corymbosum 'Legacy' - Myrtillier 'Legacy'",
            "Vaccinium corymbosum 'Bluegold' - Myrtillier 'Bluegold'",
            "Rubus idaeus 'Cascade Delight' - Framboisier 'Cascade Delight'",
            "Rubus idaeus 'Willamette' - Framboisier 'Willamette'",
            "Prunus armeniaca 'Moorpark' - Abricotier 'Moorpark'",
            "Prunus armeniaca 'Royal' - Abricotier 'Royal'",
            "Prunus domestica 'Stanley' - Prunier 'Stanley'",
            "Prunus domestica 'President' - Prunier 'President'",
            "Prunus persica 'Redhaven' - Pêcher 'Redhaven'",
            "Prunus persica 'Elberta' - Pêcher 'Elberta'",
            "Pyrus communis 'Bartlett' - Poirier 'Bartlett'",
            "Pyrus communis 'Bosc' - Poirier 'Bosc'",
            "Malus domestica 'Golden Delicious' - Pommier 'Golden Delicious'",
            "Malus domestica 'Granny Smith' - Pommier 'Granny Smith'",
            "Carya illinoinensis - Pacanier",
            "Carya ovata - Noyer cendré",
            "Diospyros virginiana - Plaqueminier d'Amérique",
            "Diospyros kaki 'Fuyu' - Plaqueminier 'Fuyu'",
            "Diospyros kaki 'Hachiya' - Plaqueminier 'Hachiya'",
            "Punica granatum 'Wonderful' - Grenadier 'Wonderful'",
            "Punica granatum 'Angel Red' - Grenadier 'Angel Red'",
            "Ficus carica 'Brown Turkey' - Figuier 'Brown Turkey'",
            "Ficus carica 'Black Mission' - Figuier 'Black Mission'",
            "Vitis vinifera 'Thompson Seedless' - Vigne 'Thompson Seedless'",
            "Vitis vinifera 'Concord' - Vigne 'Concord'",
            "Olea europaea 'Arbequina' - Olivier 'Arbequina'",
            "Olea europaea 'Manzanilla' - Olivier 'Manzanilla'",
            "Cydonia oblonga 'Smyrna' - Cognassier 'Smyrna'",
            "Cydonia oblonga 'Champion' - Cognassier 'Champion'",
            "Fragaria × ananassa 'Sweet Charlie' - Fraisier 'Sweet Charlie'",
            "Fragaria × ananassa 'Seascape' - Fraisier 'Seascape'",
            "Vaccinium corymbosum 'Chandler' - Myrtillier 'Chandler'",
            "Vaccinium corymbosum 'Reka' - Myrtillier 'Reka'",
            "Rubus fruticosus 'Apache' - Mûrier 'Apache'",
            "Rubus fruticosus 'Ouachita' - Mûrier 'Ouachita'",
            "Rubus idaeus 'Boyne' - Framboisier 'Boyne'",
            "Rubus idaeus 'Nova' - Framboisier 'Nova'",
            "Ribes nigrum 'Consort' - Cassissier 'Consort'",
            "Ribes nigrum 'Minaj Smyriou' - Cassissier 'Minaj Smyriou'",
            "Ribes uva-crispa 'Poorman' - Groseillier 'Poorman'",
            "Ribes uva-crispa 'Welcome' - Groseillier 'Welcome'",
            "Vaccinium corymbosum 'Northland' - Myrtillier 'Northland'",
            "Vaccinium corymbosum 'Bluetta' - Myrtillier 'Bluetta'",
            "Rubus idaeus 'Encore' - Framboisier 'Encore'",
            "Rubus idaeus 'Killarney' - Framboisier 'Killarney'",
            "Prunus cerasus 'Montmorency' - Cerisier 'Montmorency'",
            "Rosa 'Peace' - Rose 'Peace'",
            "Hydrangea macrophylla - Hortensia",
            "Lilium 'Stargazer' - Lis 'Stargazer'",
            "Tulipa 'Queen of Night' - Tulipe 'Queen of Night'",
            "Narcissus 'Tête-à-Tête' - Jonquille 'Tête-à-Tête'",
            "Helianthus annuus - Tournesol",
            "Petunia x hybrida - Pétunia",
            "Viola tricolor - Pensée",
            "Begonia semperflorens - Bégonia",
            "Pelargonium hortorum - Géranium",
            "Impatiens walleriana - Impatiente",
            "Fuchsia magellanica - Fuchsia",
            "Salvia splendens - Sauge",
            "Zinnia elegans - Zinnia",
            "Dahlia pinnata - Dahlia",
            "Chrysanthemum morifolium - Chrysanthème",
            "Canna indica - Canna",
            "Alstroemeria aurea - Alstroemeria",
            "Calla palustris - Calla",
            "Gladiolus hortulanus - Glaïeul",
            "Hosta 'Sum and Substance' - Hosta",
            "Iris germanica - Iris",
            "Papaver orientale - Pavot oriental",
            "Delphinium elatum - Pied d'alouette",
            "Phlox paniculata - Phlox",
            "Echinacea purpurea - Échinacée",
            "Rudbeckia hirta - Rudbeckia",
            "Lavandula angustifolia - Lavande",
            "Hibiscus syriacus - Hibiscus",
            "Camellia japonica - Camélia",
            "Rhododendron 'Nova Zembla' - Rhododendron",
            "Azalea 'Kurume' - Azalée",
            "Magnolia grandiflora - Magnolia",
            "Wisteria sinensis - Glycine",
            "Clematis 'Jackmanii' - Clématite",
            "Bougainvillea spectabilis - Bougainvillée",
            "Jacaranda mimosifolia - Jacaranda",
            "Plumeria rubra - Frangipanier",
            "Olea europaea - Olivier",
            "Ficus benjamina - Ficus",
            "Dracaena marginata - Dracaena",
            "Yucca filamentosa - Yucca",
            "Agapanthus africanus - Agapanthe",
            "Cordyline australis - Cordyline",
            "Strelitzia reginae - Oiseau de paradis",
            "Cycas revoluta - Cycas",
            "Phoenix roebelenii - Palmier nain",
            "Chamaerops humilis - Palmier nain",
            "Bambusa vulgaris - Bambou",
            "Acer palmatum - Érable japonais",
            "Betula pendula - Bouleau",
            "Quercus robur - Chêne",
            "Ginkgo biloba - Ginkgo",
            "Cercis siliquastrum - Arbre de Judée",
            "Prunus serrulata - Cerisier du Japon",
            "Malus domestica - Pommier",
            "Citrus sinensis - Oranger",
            "Oleander nerium - Laurier-rose",
            "Viburnum tinus - Viorne",
            "Buxus sempervirens - Buis",
            "Ilex aquifolium - Houx",
            "Juniperus communis - Genévrier",
            "Taxus baccata - If",
            "Thuja occidentalis - Thuya",
            "Cupressus sempervirens - Cyprès",
            "Sequoiadendron giganteum - Séquoia géant",
            "Pinus pinea - Pin parasol",
            "Cedrus atlantica - Cèdre",
            "Eucalyptus globulus - Eucalyptus",
            "Callistemon citrinus - Rince-bouteille",
            "Grevillea robusta - Grevillea",
            "Protea cynaroides - Protea",
            "Banksia integrifolia - Banksia",
            "Leptospermum scoparium - Manuka",
            "Melaleuca alternifolia - Melaleuca",
            "Acacia dealbata - Mimosa",
            "Aechmea fasciata - Aechmea",
            "Tillandsia cyanea - Tillandsia",
            "Guzmania lingulata - Guzmania",
            "Neoregelia carolinae - Néorégélia",
            "Vriesea splendens - Vriesea",
            "Ananas comosus - Ananas",
            "Cactaceae - Cactus",
            "Euphorbia pulcherrima - Poinsettia",
            "Kalanchoe blossfeldiana - Kalanchoe",
            "Aloe vera - Aloès",
            "Crassula ovata - Crassula",
            "Echeveria elegans - Échévérie",
            "Sedum morganianum - Sédum",
            "Haworthia fasciata - Haworthia",
            "Lithops - Lithops",
            "Sansevieria trifasciata - Sansevière",
            "Chlorophytum comosum - Plante-araignée",
            "Spathiphyllum wallisii - Spathiphyllum",
            "Monstera deliciosa - Monstera",
            "Philodendron hederaceum - Philodendron",
            "Ficus lyrata - Figuier lyre",
            "Pothos aurea - Pothos",
            "Dieffenbachia seguine - Dieffenbachia",
            "Calathea orbifolia - Calathea",
            "Malus domestica - Pommier",
            "Pyrus communis - Poirier",
            "Prunus armeniaca - Abricotier",
            "Prunus persica - Pêcher",
            "Prunus domestica - Prunier",
            "Prunus avium - Cerisier",
            "Prunus cerasus - Cerisier acide",
            "Prunus mume - Abricotier japonais",
            "Citrus sinensis - Oranger",
            "Citrus limon - Citronnier",
            "Citrus aurantiifolia - Limettier",
            "Citrus paradisi - Pamplemoussier",
            "Citrus reticulata - Mandariner",
            "Citrus medica - Cédratier",
            "Citrus japonica - Kumquat",
            "Ficus carica - Figuier",
            "Punica granatum - Grenadier",
            "Olea europaea - Olivier",
            "Diospyros kaki - Plaqueminier",
            "Cydonia oblonga - Cognassier",
            "Pyrus pyrifolia - Nashi",
            "Ziziphus jujuba - Jujubier",
            "Mespilus germanica - Néflier",
            "Sorbus domestica - Cormier",
            "Morus alba - Mûrier blanc",
            "Morus nigra - Mûrier noir",
            "Castanea sativa - Châtaignier",
            "Juglans regia - Noyer commun",
            "Carya illinoinensis - Pacanier",
            "Corylus avellana - Noisetier",
            "Pistacia vera - Pistachier",
            "Annona cherimola - Cherimoya",
            "Annona squamosa - Pomme cannelle",
            "Passiflora edulis - Passiflore",
            "Carica papaya - Papayer",
            "Musa acuminata - Bananier",
            "Mangifera indica - Manguier",
            "Psidium guajava - Goyavier",
            "Persea americana - Avocatier",
            "Litchi chinensis - Litchi",
            "Nephelium lappaceum - Ramboutan",
            "Durio zibethinus - Durian",
            "Eugenia uniflora - Cerisier de Cayenne",
            "Syzygium aqueum - Pomme d'eau",
            "Syzygium malaccense - Jambosier rouge",
            "Eriobotrya japonica - Néflier du Japon",
            "Garcinia mangostana - Mangoustanier",
            "Vitis vinifera - Vigne",
            "Vaccinium corymbosum - Myrtillier",
            "Rubus idaeus - Framboisier",
            "Rubus fruticosus - Mûrier",
            "Ribes nigrum - Cassissier",
            "Ribes rubrum - Groseillier rouge",
            "Ribes uva-crispa - Groseillier à maquereau",
            "Fragaria × ananassa - Fraisier",
            "Actinidia deliciosa - Kiwi",
            "Diospyros lotus - Plaqueminier du Lotus",
            "Diospyros texana - Plaqueminier du Texas",
            "Syzygium cumini - Jamun",
            "Elaeagnus umbellata - Goumi du Japon",
            "Elaeagnus multiflora - Goumi",
            "Hippophae rhamnoides - Argousier",
            "Feijoa sellowiana - Goyavier du Brésil",
            "Myrciaria cauliflora - Jaboticaba",
            "Hylocereus undatus - Pitaya",
            "Arbutus unedo - Arbousier",
            "Berberis vulgaris - Épine-vinette",
            "Chaenomeles speciosa - Cognassier du Japon",
            "Crataegus monogyna - Aubépine",
            "Amelanchier alnifolia - Amélanchier",
            "Mammea americana - Mamey",
            "Bunchosia argentea - Bunchosia",
            "Tamarindus indica - Tamarinier",
            "Phyllanthus emblica - Amla",
            "Carissa macrocarpa - Carissa",
            "Syzygium samarangense - Pomme rose",
            "Terminalia catappa - Badamier",
            "Chrysophyllum cainito - Caimito",
            "Rollinia deliciosa - Biriba",
            "Campomanesia xanthocarpa - Gabiroba",
            "Euterpe oleracea - Açaï",
            "Inga edulis - Inga",
            "Spondias dulcis - Pommecythère",
            "Spondias mombin - Mombin",
            "Eugenia brasiliensis - Cerisier du Brésil",
            "Canarium indicum - Pili",
            "Artocarpus heterophyllus - Jacquier",
            "Artocarpus altilis - Arbre à pain",
            "Anacardium occidentale - Anacardier",
            "Borassus flabellifer - Palmier sucrier",
            "Phoenix dactylifera - Palmier dattier",
            "Bactris gasipaes - Pêche palmiste",
            "Durio graveolens - Durian sauvage",
            "Durio oxleyanus - Durian oxleyanus",
            "Nephelium mutabile - Pulasan",
            "Aegle marmelos - Bael",
            "Pouteria campechiana - Sapotille",
            "Pouteria sapota - Sapote mamey",
            "Dovyalis caffra - Kei apple",
            "Solanum muricatum - Pepino"
        ]
        for nomajouter in plantes_de_potager:
            Planteajoutee.nom = nomajouter
            Planteajoutee.hauteur = ""
            Planteajoutee.envergure = ""
            Planteajoutee.exposition = ""
            Planteajoutee.datedesemis = ""
            Planteajoutee.datedeplantation = ""
            Planteajoutee.duree = ""
            Planteajoutee.arrosage = ""
            Planteajoutee.typesol = ""
            Planteajoutee.associations = ""
            Planteajoutee.temperaturegermination = ""
            Planteajoutee.type = ""
            Planteajoutee.couleur = ""
            Planteajoutee.emplacement = ""
            Planteajoutee.feuillagepersistant = 0
            Planteajoutee.mellifere = 0
            Planteajoutee.moisdefloraison = ""
            Planteajoutee.moisderecolte = ""
            Planteajoutee.planteparfumee = 0
            Planteajoutee.plantevivace = 0
            tamponplantes.append((Planteajoutee.nom, Planteajoutee.hauteur, Planteajoutee.envergure,
                                  Planteajoutee.exposition, Planteajoutee.datedesemis, Planteajoutee.datedeplantation,
                                  Planteajoutee.duree, Planteajoutee.arrosage, Planteajoutee.typesol,
                                  Planteajoutee.associations, Planteajoutee.temperaturegermination, Planteajoutee.type,
                                  Planteajoutee.couleur, Planteajoutee.emplacement, Planteajoutee.feuillagepersistant,
                                  Planteajoutee.mellifere, Planteajoutee.moisdefloraison, Planteajoutee.moisderecolte,
                                  Planteajoutee.planteparfumee, Planteajoutee.plantevivace))
        requetesql.maj_bdd(tamponplantes)
        tamponplantes.clear()

