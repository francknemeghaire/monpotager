from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
import sys

app2 = QApplication(sys.argv)
root = QWidget()
root.setGeometry(100, 100, 800, 600)

# create a QPixmap object
qpixmap = QPixmap("./lavande.jpeg")
# creat a QLabel for image
lbl_img = QLabel(root)
lbl_img.setGeometry(0, 0, 500, 300)
lbl_img.setPixmap(qpixmap)
# resizing the image
lbl_img.setScaledContents(True)
lbl_img.resize(400, 400)
root.show()
sys.exit(app2.exec())