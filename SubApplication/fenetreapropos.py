from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PySide6.QtGui import Qt


class Apropos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A propos")
        self.setGeometry(0, 0, 400, 400)
        self.pixmap = QPixmap('image/lavande.jpeg')
        self.lbl_img = QLabel(self)
        self.lbl_img.setScaledContents(True)
        self.lbl_img.setPixmap(self.pixmap)
        self.lbl_img.resize(300, 300)
        self.show()



