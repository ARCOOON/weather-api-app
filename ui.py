import sys
import threading
import time
import urllib.request

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from main import *
from utils import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.url = getIconLink(call(), 4)
        self.mymap = QPixmap()
        self.data = urllib.request.urlopen(self.url).read()
        
        self.I = QLabel(self)
        self.mymap.loadFromData(self.data)
        self.I.setPixmap(self.mymap)
        
        self.rBTN = QPushButton()
        self.rBTN

        #self.cw = QWidget(self)
        self.setCentralWidget(self.I)
        self.mainlay = QVBoxLayout()
        self.mainlay.addWidget(self.I)
        self.mainlay.addWidget(self.rBTN)
        
        def refresh():
            print("function: refreshUI")
    
def run():
    app = QApplication(sys.argv)
    app.setStyle('Breeze')
    app.setStyleSheet("QMainWindow { background-color: #101010 }")
    win = Window()
    win.show()
    app.exit(app.exec_())

if __name__ == "__main__":
    run()
    # time.sleep(1800)