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

    def sauvegardeplantes(self, repertoire):
        pass

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
            "1. Allium cepa - Oignon",
            "2. Solanum lycopersicum - Tomate",
            "3. Cucumis sativus - Concombre",
            "4. Daucus carota - Carotte",
            "5. Brassica oleracea var. capitata - Chou",
            "6. Lactuca sativa - Laitue",
            "7. Phaseolus vulgaris - Haricot vert",
            "8. Pisum sativum - Pois",
            "9. Capsicum annuum - Poivron",
            "10. Cucurbita pepo - Courgette",
            "11. Raphanus sativus - Radis",
            "12. Spinacia oleracea - Épinard",
            "13. Solanum melongena - Aubergine",
            "14. Beta vulgaris - Betterave",
            "15. Zea mays - Maïs",
            "16. Brassica oleracea var. italica - Brocoli",
            "17. Allium sativum - Ail",
            "18. Brassica rapa - Navet",
            "19. Apium graveolens - Céleri",
            "20. Brassica napus - Rutabaga",
            "21. Cichorium intybus - Chicorée",
            "22. Brassica oleracea var. gemmifera - Chou de Bruxelles",
            "23. Brassica oleracea var. botrytis - Chou-fleur",
            "24. Rheum rhabarbarum - Rhubarbe",
            "25. Fragaria × ananassa - Fraise",
            "26. Rubus idaeus - Framboise",
            "27. Ribes nigrum - Cassis",
            "28. Ribes uva-crispa - Groseille",
            "29. Vaccinium corymbosum - Myrtille",
            "30. Rubus fruticosus - Mûre",
            "31. Asparagus officinalis - Asperge",
            "32. Cynara scolymus - Artichaut",
            "33. Solanum tuberosum - Pomme de terre",
            "34. Ipomoea batatas - Patate douce",
            "35. Cichorium endivia - Endive",
            "36. Vigna unguiculata - Pois à vache",
            "37. Brassica juncea - Moutarde brune",
            "38. Petroselinum crispum - Persil",
            "39. Anethum graveolens - Aneth",
            "40. Thymus vulgaris - Thym",
            "41. Rosmarinus officinalis - Romarin",
            "42. Ocimum basilicum - Basilic",
            "43. Origanum vulgare - Origan",
            "44. Salvia officinalis - Sauge",
            "45. Mentha spicata - Menthe",
            "46. Coriandrum sativum - Coriandre",
            "47. Lavandula angustifolia - Lavande",
            "48. Foeniculum vulgare - Fenouil",
            "49. Nasturtium officinale - Cresson",
            "50. Taraxacum officinale - Pissenlit",
            "51. Armoracia rusticana - Raifort",
            "52. Levisticum officinale - Livèche",
            "53. Hyssopus officinalis - Hysope",
            "54. Melissa officinalis - Mélisse",
            "55. Valeriana officinalis - Valériane",
            "56. Ruta graveolens - Rue",
            "57. Satureja hortensis - Sarriette",
            "58. Allium ampeloprasum - Poireau",
            "59. Brassica oleracea var. acephala - Chou frisé",
            "60. Helianthus tuberosus - Topinambour",
            "61. Pastinaca sativa - Panais",
            "62. Scorzonera hispanica - Salsifis",
            "63. Foeniculum vulgare - Fenouil",
            "64. Allium fistulosum - Ciboule",
            "65. Allium schoenoprasum - Ciboulette",
            "66. Rumex acetosa - Oseille",
            "67. Portulaca oleracea - Pourpier",
            "68. Tetragonia tetragonioides - Tétragone",
            "69. Chenopodium quinoa - Quinoa",
            "70. Eruca vesicaria - Roquette",
            "71. Brassica oleracea var. gongylodes - Chou-rave",
            "72. Crambe maritima - Chou marin",
            "73. Lepidium sativum - Cresson alénois",
            "74. Brassica rapa subsp. chinensis - Pak-choï",
            "75. Brassica rapa subsp. pekinensis - Chou chinois",
            "76. Brassica oleracea var. viridis - Collard",
            "77. Brassica oleracea var. alboglabra - Chou kale",
            "78. Lactuca sativa var. longifolia - Romaine",
            "79. Lactuca sativa var. crispa - Laitue frisée",
            "80. Cucumis melo - Melon",
            "81. Citrullus lanatus - Pastèque",
            "82. Fragaria vesca - Fraisier des bois",
            "83. Rubus idaeus strigosus - Framboisier rouge",
            "84. Ribes rubrum - Groseillier rouge",
            "85. Ribes uva-crispa var. reclinatum - Groseillier à maquereau",
            "86. Vaccinium macrocarpon - Canneberge",
            "87. Rubus occidentalis - Framboisier noir",
            "88. Juglans regia - Noyer",
            "89. Corylus avellana - Noisetier",
            "90. Prunus armeniaca - Abricotier",
            "91. Prunus domestica - Prunier",
            "92. Prunus persica - Pêcher",
            "93. Pyrus communis - Poirier",
            "94. Malus domestica - Pommier",
            "95. Carya ovata - Noyer blanc",
            "96. Diospyros kaki - Plaqueminier",
            "97. Punica granatum - Grenadier",
            "98. Ficus carica - Figuier",
            "99. Vitis vinifera - Vigne",
            "100. Olea europaea - Olivier",
            "101. Cydonia oblonga - Cognassier",
            "102. Fragaria × ananassa 'Albion' - Fraisier 'Albion'",
            "103. Fragaria × ananassa 'Mara des bois' - Fraisier 'Mara des bois'",
            "104. Vaccinium corymbosum 'Bluecrop' - Myrtillier 'Bluecrop'",
            "105. Vaccinium corymbosum 'Patriot' - Myrtillier 'Patriot'",
            "106. Rubus fruticosus 'Chester Thornless' - Mûrier 'Chester Thornless'",
            "107. Rubus fruticosus 'Loch Ness' - Mûrier 'Loch Ness'",
            "108. Rubus idaeus 'Autumn Bliss' - Framboisier 'Autumn Bliss'",
            "109. Rubus idaeus 'Glen Ample' - Framboisier 'Glen Ample'",
            "110. Ribes nigrum 'Ben Lomond' - Cassissier 'Ben Lomond'",
            "111. Ribes nigrum 'Titania' - Cassissier 'Titania'",
            "112. Ribes uva-crispa 'Invicta' - Groseillier 'Invicta'",
            "113. Ribes uva-crispa 'Hinnonmäki Röd' - Groseillier 'Hinnonmäki Röd'",
            "114. Vaccinium corymbosum 'Duke' - Myrtillier 'Duke'",
            "115. Vaccinium corymbosum 'Elliott' - Myrtillier 'Elliott'",
            "116. Rubus idaeus 'Tulameen' - Framboisier 'Tulameen'",
            "117. Rubus idaeus 'Heritage' - Framboisier 'Heritage'",
            "118. Prunus cerasus - Cerisier",
            "119. Prunus avium - Merisier",
            "120. Vaccinium myrtillus - Myrtille sauvage",
            "121. Rubus idaeus var. strigosus - Framboisier sauvage",
            "122. Rubus fruticosus var. inermis - Mûrier sauvage",
            "123. Ribes nigrum var. pungens - Cassissier sauvage",
            "124. Fragaria vesca var. semperflorens - Fraisier des bois",
            "125. Prunus spinosa - Prunellier",
            "126. Rubus caesius - Ronce bleue",
            "127. Fragaria chiloensis - Fraisier du Chili",
            "128. Fragaria virginiana - Fraisier de Virginie",
            "129. Vaccinium angustifolium - Myrtille basse",
            "130. Vaccinium myrtilloides - Myrtille fausse-airelle",
            "131. Vaccinium uliginosum - Myrtille des marais",
            "132. Vaccinium vitis-idaea - Airelle rouge",
            "133. Ribes oxyacanthoides - Groseillier épineux",
            "134. Ribes hirtellum - Groseillier hispidule",
            "135. Rubus allegheniensis - Mûrier Allegheny",
            "136. Rubus occidentalis var. strigosus - Framboisier occidental",
            "137. Rubus leucodermis - Framboisier blanc",
            "138. Rubus phoenicolasius - Framboisier rouge",
            "139. Rubus ursinus - Mûrier des montagnes",
            "140. Rubus armeniacus - Mûrier de l'Himalaya",
            "141. Rubus laciniatus - Mûrier à feuilles laciniées",
            "142. Rubus canadensis - Mûrier canadien",
            "143. Fragaria × ananassa 'Elsanta' - Fraisier 'Elsanta'",
            "144. Fragaria × ananassa 'Gariguette' - Fraisier 'Gariguette'",
            "145. Vaccinium corymbosum 'Bluejay' - Myrtillier 'Bluejay'",
            "146. Vaccinium corymbosum 'Brigitta' - Myrtillier 'Brigitta'",
            "147. Rubus fruticosus 'Navaho' - Mûrier 'Navaho'",
            "148. Rubus fruticosus 'Triple Crown' - Mûrier 'Triple Crown'",
            "149. Rubus idaeus 'Polka' - Framboisier 'Polka'",
            "150. Rubus idaeus 'Meeker' - Framboisier 'Meeker'",
            "151. Ribes nigrum 'Baldwin' - Cassissier 'Baldwin'",
            "152. Ribes nigrum 'Black Reward' - Cassissier 'Black Reward'",
            "153. Ribes uva-crispa 'Captivator' - Groseillier 'Captivator'",
            "154. Ribes uva-crispa 'Pixwell' - Groseillier 'Pixwell'",
            "155. Vaccinium corymbosum 'Legacy' - Myrtillier 'Legacy'",
            "156. Vaccinium corymbosum 'Bluegold' - Myrtillier 'Bluegold'",
            "157. Rubus idaeus 'Cascade Delight' - Framboisier 'Cascade Delight'",
            "158. Rubus idaeus 'Willamette' - Framboisier 'Willamette'",
            "159. Prunus armeniaca 'Moorpark' - Abricotier 'Moorpark'",
            "160. Prunus armeniaca 'Royal' - Abricotier 'Royal'",
            "161. Prunus domestica 'Stanley' - Prunier 'Stanley'",
            "162. Prunus domestica 'President' - Prunier 'President'",
            "163. Prunus persica 'Redhaven' - Pêcher 'Redhaven'",
            "164. Prunus persica 'Elberta' - Pêcher 'Elberta'",
            "165. Pyrus communis 'Bartlett' - Poirier 'Bartlett'",
            "166. Pyrus communis 'Bosc' - Poirier 'Bosc'",
            "167. Malus domestica 'Golden Delicious' - Pommier 'Golden Delicious'",
            "168. Malus domestica 'Granny Smith' - Pommier 'Granny Smith'",
            "169. Carya illinoinensis - Pacanier",
            "170. Carya ovata - Noyer cendré",
            "171. Diospyros virginiana - Plaqueminier d'Amérique",
            "172. Diospyros kaki 'Fuyu' - Plaqueminier 'Fuyu'",
            "173. Diospyros kaki 'Hachiya' - Plaqueminier 'Hachiya'",
            "174. Punica granatum 'Wonderful' - Grenadier 'Wonderful'",
            "175. Punica granatum 'Angel Red' - Grenadier 'Angel Red'",
            "176. Ficus carica 'Brown Turkey' - Figuier 'Brown Turkey'",
            "177. Ficus carica 'Black Mission' - Figuier 'Black Mission'",
            "178. Vitis vinifera 'Thompson Seedless' - Vigne 'Thompson Seedless'",
            "179. Vitis vinifera 'Concord' - Vigne 'Concord'",
            "180. Olea europaea 'Arbequina' - Olivier 'Arbequina'",
            "181. Olea europaea 'Manzanilla' - Olivier 'Manzanilla'",
            "182. Cydonia oblonga 'Smyrna' - Cognassier 'Smyrna'",
            "183. Cydonia oblonga 'Champion' - Cognassier 'Champion'",
            "184. Fragaria × ananassa 'Sweet Charlie' - Fraisier 'Sweet Charlie'",
            "185. Fragaria × ananassa 'Seascape' - Fraisier 'Seascape'",
            "186. Vaccinium corymbosum 'Chandler' - Myrtillier 'Chandler'",
            "187. Vaccinium corymbosum 'Reka' - Myrtillier 'Reka'",
            "188. Rubus fruticosus 'Apache' - Mûrier 'Apache'",
            "189. Rubus fruticosus 'Ouachita' - Mûrier 'Ouachita'",
            "190. Rubus idaeus 'Boyne' - Framboisier 'Boyne'",
            "191. Rubus idaeus 'Nova' - Framboisier 'Nova'",
            "192. Ribes nigrum 'Consort' - Cassissier 'Consort'",
            "193. Ribes nigrum 'Minaj Smyriou' - Cassissier 'Minaj Smyriou'",
            "194. Ribes uva-crispa 'Poorman' - Groseillier 'Poorman'",
            "195. Ribes uva-crispa 'Welcome' - Groseillier 'Welcome'",
            "196. Vaccinium corymbosum 'Northland' - Myrtillier 'Northland'",
            "197. Vaccinium corymbosum 'Bluetta' - Myrtillier 'Bluetta'",
            "198. Rubus idaeus 'Encore' - Framboisier 'Encore'",
            "199. Rubus idaeus 'Killarney' - Framboisier 'Killarney'",
            "200. Prunus cerasus 'Montmorency' - Cerisier 'Montmorency'"
        ]

        # Sauvegarde dans un fichier texte
        with open("Liste_de_plantes_de_potager.txt", "w") as file:
            for plante in plantes_de_potager:
                file.write(plante + "\n")

    def sourcedeplantesornementales(self):
        plantes_ornementales = [
            "1. Rosa 'Peace' - Rose 'Peace'",
            "2. Hydrangea macrophylla - Hortensia",
            "3. Lilium 'Stargazer' - Lis 'Stargazer'",
            "4. Tulipa 'Queen of Night' - Tulipe 'Queen of Night'",
            "5. Narcissus 'Tête-à-Tête' - Jonquille 'Tête-à-Tête'",
            "6. Helianthus annuus - Tournesol",
            "7. Petunia x hybrida - Pétunia",
            "8. Viola tricolor - Pensée",
            "9. Begonia semperflorens - Bégonia",
            "10. Pelargonium hortorum - Géranium",
            "11. Impatiens walleriana - Impatiente",
            "12. Fuchsia magellanica - Fuchsia",
            "13. Salvia splendens - Sauge",
            "14. Zinnia elegans - Zinnia",
            "15. Dahlia pinnata - Dahlia",
            "16. Chrysanthemum morifolium - Chrysanthème",
            "17. Canna indica - Canna",
            "18. Alstroemeria aurea - Alstroemeria",
            "19. Calla palustris - Calla",
            "20. Gladiolus hortulanus - Glaïeul",
            "21. Hosta 'Sum and Substance' - Hosta",
            "22. Iris germanica - Iris",
            "23. Papaver orientale - Pavot oriental",
            "24. Delphinium elatum - Pied d'alouette",
            "25. Phlox paniculata - Phlox",
            "26. Echinacea purpurea - Échinacée",
            "27. Rudbeckia hirta - Rudbeckia",
            "28. Lavandula angustifolia - Lavande",
            "29. Hibiscus syriacus - Hibiscus",
            "30. Camellia japonica - Camélia",
            "31. Rhododendron 'Nova Zembla' - Rhododendron",
            "32. Azalea 'Kurume' - Azalée",
            "33. Magnolia grandiflora - Magnolia",
            "34. Wisteria sinensis - Glycine",
            "35. Clematis 'Jackmanii' - Clématite",
            "36. Bougainvillea spectabilis - Bougainvillée",
            "37. Jacaranda mimosifolia - Jacaranda",
            "38. Plumeria rubra - Frangipanier",
            "39. Olea europaea - Olivier",
            "40. Ficus benjamina - Ficus",
            "41. Dracaena marginata - Dracaena",
            "42. Yucca filamentosa - Yucca",
            "43. Agapanthus africanus - Agapanthe",
            "44. Cordyline australis - Cordyline",
            "45. Strelitzia reginae - Oiseau de paradis",
            "46. Cycas revoluta - Cycas",
            "47. Phoenix roebelenii - Palmier nain",
            "48. Chamaerops humilis - Palmier nain",
            "49. Bambusa vulgaris - Bambou",
            "50. Acer palmatum - Érable japonais",
            "51. Betula pendula - Bouleau",
            "52. Quercus robur - Chêne",
            "53. Ginkgo biloba - Ginkgo",
            "54. Cercis siliquastrum - Arbre de Judée",
            "55. Prunus serrulata - Cerisier du Japon",
            "56. Malus domestica - Pommier",
            "57. Citrus sinensis - Oranger",
            "58. Oleander nerium - Laurier-rose",
            "59. Viburnum tinus - Viorne",
            "60. Buxus sempervirens - Buis",
            "61. Ilex aquifolium - Houx",
            "62. Juniperus communis - Genévrier",
            "63. Taxus baccata - If",
            "64. Thuja occidentalis - Thuya",
            "65. Cupressus sempervirens - Cyprès",
            "66. Sequoiadendron giganteum - Séquoia géant",
            "67. Pinus pinea - Pin parasol",
            "68. Cedrus atlantica - Cèdre",
            "69. Eucalyptus globulus - Eucalyptus",
            "70. Callistemon citrinus - Rince-bouteille",
            "71. Grevillea robusta - Grevillea",
            "72. Protea cynaroides - Protea",
            "73. Banksia integrifolia - Banksia",
            "74. Leptospermum scoparium - Manuka",
            "75. Melaleuca alternifolia - Melaleuca",
            "76. Acacia dealbata - Mimosa",
            "77. Aechmea fasciata - Aechmea",
            "78. Tillandsia cyanea - Tillandsia",
            "79. Guzmania lingulata - Guzmania",
            "80. Neoregelia carolinae - Néorégélia",
            "81. Vriesea splendens - Vriesea",
            "82. Ananas comosus - Ananas",
            "83. Cactaceae - Cactus",
            "84. Euphorbia pulcherrima - Poinsettia",
            "85. Kalanchoe blossfeldiana - Kalanchoe",
            "86. Aloe vera - Aloès",
            "87. Crassula ovata - Crassula",
            "88. Echeveria elegans - Échévérie",
            "89. Sedum morganianum - Sédum",
            "90. Haworthia fasciata - Haworthia",
            "91. Lithops - Lithops",
            "92. Sansevieria trifasciata - Sansevière",
            "93. Chlorophytum comosum - Plante-araignée",
            "94. Spathiphyllum wallisii - Spathiphyllum",
            "95. Monstera deliciosa - Monstera",
            "96. Philodendron hederaceum - Philodendron",
            "97. Ficus lyrata - Figuier lyre",
            "98. Pothos aurea - Pothos",
            "99. Dieffenbachia seguine - Dieffenbachia",
            "100. Calathea orbifolia - Calathea"
        ]

        # Sauvegarde dans un fichier texte
        with open("Liste_de_plantes_ornementales.txt", "w") as file:
            for plante in plantes_ornementales:
                file.write(plante + "\n")
    def sourcearbresfruitiers(self):
        arbres_fruitiers = [
            "1. Malus domestica - Pommier",
            "2. Pyrus communis - Poirier",
            "3. Prunus armeniaca - Abricotier",
            "4. Prunus persica - Pêcher",
            "5. Prunus domestica - Prunier",
            "6. Prunus avium - Cerisier",
            "7. Prunus cerasus - Cerisier acide",
            "8. Prunus mume - Abricotier japonais",
            "9. Citrus sinensis - Oranger",
            "10. Citrus limon - Citronnier",
            "11. Citrus aurantiifolia - Limettier",
            "12. Citrus paradisi - Pamplemoussier",
            "13. Citrus reticulata - Mandariner",
            "14. Citrus medica - Cédratier",
            "15. Citrus japonica - Kumquat",
            "16. Ficus carica - Figuier",
            "17. Punica granatum - Grenadier",
            "18. Olea europaea - Olivier",
            "19. Diospyros kaki - Plaqueminier",
            "20. Cydonia oblonga - Cognassier",
            "21. Pyrus pyrifolia - Nashi",
            "22. Ziziphus jujuba - Jujubier",
            "23. Mespilus germanica - Néflier",
            "24. Sorbus domestica - Cormier",
            "25. Morus alba - Mûrier blanc",
            "26. Morus nigra - Mûrier noir",
            "27. Castanea sativa - Châtaignier",
            "28. Juglans regia - Noyer commun",
            "29. Carya illinoinensis - Pacanier",
            "30. Corylus avellana - Noisetier",
            "31. Pistacia vera - Pistachier",
            "32. Annona cherimola - Cherimoya",
            "33. Annona squamosa - Pomme cannelle",
            "34. Passiflora edulis - Passiflore",
            "35. Carica papaya - Papayer",
            "36. Musa acuminata - Bananier",
            "37. Mangifera indica - Manguier",
            "38. Psidium guajava - Goyavier",
            "39. Persea americana - Avocatier",
            "40. Litchi chinensis - Litchi",
            "41. Nephelium lappaceum - Ramboutan",
            "42. Durio zibethinus - Durian",
            "43. Eugenia uniflora - Cerisier de Cayenne",
            "44. Syzygium aqueum - Pomme d'eau",
            "45. Syzygium malaccense - Jambosier rouge",
            "46. Eriobotrya japonica - Néflier du Japon",
            "47. Garcinia mangostana - Mangoustanier",
            "48. Vitis vinifera - Vigne",
            "49. Vaccinium corymbosum - Myrtillier",
            "50. Rubus idaeus - Framboisier",
            "51. Rubus fruticosus - Mûrier",
            "52. Ribes nigrum - Cassissier",
            "53. Ribes rubrum - Groseillier rouge",
            "54. Ribes uva-crispa - Groseillier à maquereau",
            "55. Fragaria × ananassa - Fraisier",
            "56. Actinidia deliciosa - Kiwi",
            "57. Diospyros lotus - Plaqueminier du Lotus",
            "58. Diospyros texana - Plaqueminier du Texas",
            "59. Syzygium cumini - Jamun",
            "60. Elaeagnus umbellata - Goumi du Japon",
            "61. Elaeagnus multiflora - Goumi",
            "62. Hippophae rhamnoides - Argousier",
            "63. Feijoa sellowiana - Goyavier du Brésil",
            "64. Myrciaria cauliflora - Jaboticaba",
            "65. Hylocereus undatus - Pitaya",
            "66. Arbutus unedo - Arbousier",
            "67. Berberis vulgaris - Épine-vinette",
            "68. Chaenomeles speciosa - Cognassier du Japon",
            "69. Crataegus monogyna - Aubépine",
            "70. Amelanchier alnifolia - Amélanchier",
            "71. Mammea americana - Mamey",
            "72. Bunchosia argentea - Bunchosia",
            "73. Tamarindus indica - Tamarinier",
            "74. Phyllanthus emblica - Amla",
            "75. Carissa macrocarpa - Carissa",
            "76. Syzygium samarangense - Pomme rose",
            "77. Terminalia catappa - Badamier",
            "78. Chrysophyllum cainito - Caimito",
            "79. Rollinia deliciosa - Biriba",
            "80. Campomanesia xanthocarpa - Gabiroba",
            "81. Euterpe oleracea - Açaï",
            "82. Inga edulis - Inga",
            "83. Spondias dulcis - Pommecythère",
            "84. Spondias mombin - Mombin",
            "85. Eugenia brasiliensis - Cerisier du Brésil",
            "86. Canarium indicum - Pili",
            "87. Artocarpus heterophyllus - Jacquier",
            "88. Artocarpus altilis - Arbre à pain",
            "89. Anacardium occidentale - Anacardier",
            "90. Borassus flabellifer - Palmier sucrier",
            "91. Phoenix dactylifera - Palmier dattier",
            "92. Bactris gasipaes - Pêche palmiste",
            "93. Durio graveolens - Durian sauvage",
            "94. Durio oxleyanus - Durian oxleyanus",
            "95. Nephelium mutabile - Pulasan",
            "96. Aegle marmelos - Bael",
            "97. Pouteria campechiana - Sapotille",
            "98. Pouteria sapota - Sapote mamey",
            "99. Dovyalis caffra - Kei apple",
            "100. Solanum muricatum - Pepino"
        ]

        # Sauvegarde dans un fichier texte
        with open("Liste_de_arbres_fruitiers.txt", "w") as file:
            for arbre in arbres_fruitiers:
                file.write(arbre + "\n")

