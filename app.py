from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
import datetime as dt
import threading

from main import *
from utils import *

class Ui_Window(object):
    def setupUi(self, Window):
        self.t = util.time(dt)

        font = QtGui.QFont()
        font.setPointSize(12)

        Window.setFont(font)
        Window.setAutoFillBackground(False)
        Window.setStyleSheet("* { background-color: #151515; color:#fff; }")
        Window.setWindowFilePath("")
        Window.setTabShape(QtWidgets.QTabWidget.Triangular)
        Window.setWindowFlag(Qt.FramelessWindowHint)
        
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        
        self.weatherTodayFrame = QtWidgets.QFrame(self.centralwidget)
        self.weatherTodayFrame.setGeometry(QtCore.QRect(0, 0, 211, 201))
        self.weatherTodayFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.weatherTodayFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.weatherTodayFrame.setLineWidth(0)
        self.weatherTodayFrame.setObjectName("weatherTodayFrame")
        self.weatherToday = QtWidgets.QLabel(self.weatherTodayFrame)
        self.weatherToday.setGeometry(QtCore.QRect(10, 180, 201, 20))
        
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        
        self.weatherToday.setFont(font)
        self.weatherToday.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.weatherToday.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.weatherToday.setFrameShadow(QtWidgets.QFrame.Plain)
        self.weatherToday.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherToday.setObjectName("weatherToday")
        
        try:
            self.data = urllib.request.urlopen(getIconLink(call(), 4)).read()
            self._icon = QPixmap()
            self._icon.loadFromData(self.data)

        except:
            pass
        
        self.weatherTodayIcon = QtWidgets.QLabel(self.weatherTodayFrame)
        self.weatherTodayIcon.setGeometry(QtCore.QRect(0, 0, 211, 161))
        self.weatherTodayIcon.setText("")
        self.weatherTodayIcon.setTextFormat(QtCore.Qt.AutoText)
        #self.weatherTodayIcon.setPixmap(self._icon)
        self.weatherTodayIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherTodayIcon.setObjectName("weatherTodayIcon")
        
        self.informationsFrame = QtWidgets.QFrame(self.centralwidget)
        self.informationsFrame.setGeometry(QtCore.QRect(420, 0, 221, 201))
        self.informationsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.informationsFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.informationsFrame.setLineWidth(0)
        self.informationsFrame.setObjectName("informationsFrame")
        
        self.datetimeFrame = QtWidgets.QFrame(self.centralwidget)
        self.datetimeFrame.setGeometry(QtCore.QRect(220, 0, 191, 201))
        self.datetimeFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.datetimeFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.datetimeFrame.setLineWidth(0)
        self.datetimeFrame.setObjectName("datetimeFrame")
        
        self.label = QtWidgets.QLabel(self.datetimeFrame)
        self.label.setGeometry(QtCore.QRect(8, 10, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.mondayFrame = QtWidgets.QFrame(self.centralwidget)
        self.mondayFrame.setGeometry(QtCore.QRect(0, 210, 121, 161))
        self.mondayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mondayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mondayFrame.setObjectName("mondayFrame")
        
        self.thuesdayFrame = QtWidgets.QFrame(self.centralwidget)
        self.thuesdayFrame.setGeometry(QtCore.QRect(130, 210, 121, 161))
        self.thuesdayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thuesdayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thuesdayFrame.setObjectName("thuesdayFrame")
        
        self.wensdayFrame = QtWidgets.QFrame(self.centralwidget)
        self.wensdayFrame.setGeometry(QtCore.QRect(260, 210, 121, 161))
        self.wensdayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wensdayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wensdayFrame.setObjectName("wensdayFrame")
        
        self.thursdayFrame = QtWidgets.QFrame(self.centralwidget)
        self.thursdayFrame.setGeometry(QtCore.QRect(390, 210, 121, 161))
        self.thursdayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thursdayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thursdayFrame.setObjectName("thursdayFrame")
        
        self.fridayFrame = QtWidgets.QFrame(self.centralwidget)
        self.fridayFrame.setGeometry(QtCore.QRect(520, 210, 121, 161))
        self.fridayFrame.setAutoFillBackground(False)
        self.fridayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fridayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fridayFrame.setObjectName("fridayFrame")

        Window.setCentralWidget(self.centralwidget)

    def retranslateUi(self, Window):
        pass

def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.showMaximized()
    #Window.show()
    sys.exit(app.exec_())

def update(self):
    while True:
        _t = util.time.getSet(self.t)
        self.label.setText(_t)
        time.sleep(1)

if __name__ == "__main__":
    workerThread = threading.Thread(target=update)
    mainThread = threading.Thread(target=run)
    
    #workerThread.start()
    mainThread.start()
