from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLineEdit
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout
from PySide6.QtWidgets import QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView


class rechercheinternet(QMainWindow):
    def __init__(self, critere):
        QMainWindow.__init__(self)
        self.critere = critere
        self.setWindowTitle("Recherche Internet")
        self.widget = QWidget(self)
        self.FNTWEB = QWebEngineView()
        self.FNTWEB.load(QUrl("https://www.google.be/search?q="+self.critere+"&hl=fr"))
        self.FNTWEB.urlChanged.connect(self.url_changed)
        self.setGeometry(0,0,1024,768)
        self.show()
        #bouton de navigation
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.FNTWEB.back)
        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.FNTWEB.forward)
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.FNTWEB.reload)
        # adresse URL
        self.url_text = QLineEdit()
        # bouton de chargement de page.
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.url_set)

        self.toplayout = QHBoxLayout()
        self.toplayout.addWidget(self.back_button)
        self.toplayout.addWidget(self.forward_button)
        self.toplayout.addWidget(self.refresh_button)
        self.toplayout.addWidget(self.url_text)
        self.toplayout.addWidget(self.go_button)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.toplayout)
        self.layout.addWidget(self.FNTWEB)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
    def url_changed(self, url):
        """Refresh the address bar"""
        self.url_text.setText(url.toString())

    def url_set(self):
        """Load the new URL"""
        self.FNTWEB.setUrl(QUrl(self.url_text.text()))
