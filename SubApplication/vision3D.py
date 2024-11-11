# test de script avec panda3D
from panda3d.core import Point3, Vec4, AmbientLight, DirectionalLight
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from math import pi, sin, cos


class GardenApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Charger le modèle de base (sol) en herbe
        self.ground = self.loader.loadModel("models/environment")
        self.ground.setScale(0.1, 0.1, 0.1)
        self.ground.reparentTo(self.render)

        # # # Appliquer une texture d'herbe
        # # grass_texture = self.loader.loadTexture("model3D/rostlinka12_2k_difuse.jpeg")
        # # self.ground.setTexture(grass_texture, 1)
        #
        # # Ajouter quelques arbres
        # self.tree = self.loader.loadModel("model3D/tree.fbx")
        # for i in range(5):
        #     x = -5 + i * 2
        #     tree_instance = self.tree.copyTo(self.render)
        #     tree_instance.setPos(x, 0, 0)
        #     tree_instance.setScale(0.5, 0.5, 0.5)
        #
        # # Ajouter le ciel
        # self.sky = self.loader.loadModel("model3D/basic_skybox3d.fbx")
        # self.sky.setScale(100)
        # self.sky.reparentTo(self.render)
        #
        # Créer une lumière ambiante
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(0.8, 0.8, 0.8, 1))
        ambientLightNP = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientLightNP)

        # Créer une lumière directionnelle (simule le soleil)
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Point3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 0.8, 1))
        directionalLightNP = self.render.attachNewNode(directionalLight)
        self.render.setLight(directionalLightNP)

        # Animation pour faire tourner la caméra autour du jardin
        self.taskMgr.add(self.spinCameraTask, "spinCameraTask")

    # Rotation de la caméra autour du jardin
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.lookAt(Point3(0, 0, 0))
        return Task.cont