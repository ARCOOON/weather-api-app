# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(643, 374)
        font = QtGui.QFont()
        font.setPointSize(12)
        Window.setFont(font)
        Window.setAutoFillBackground(False)
        Window.setStyleSheet("* { background-color: #151515; color:#fff; }")
        Window.setWindowFilePath("")
        Window.setTabShape(QtWidgets.QTabWidget.Triangular)
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
        self.weatherToday.setAutoFillBackground(False)
        self.weatherToday.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.weatherToday.setFrameShadow(QtWidgets.QFrame.Plain)
        self.weatherToday.setScaledContents(False)
        self.weatherToday.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherToday.setWordWrap(False)
        self.weatherToday.setObjectName("weatherToday")
        self.weatherTodayIcon = QtWidgets.QLabel(self.weatherTodayFrame)
        self.weatherTodayIcon.setGeometry(QtCore.QRect(0, 0, 211, 161))
        self.weatherTodayIcon.setText("")
        self.weatherTodayIcon.setTextFormat(QtCore.Qt.AutoText)
        self.weatherTodayIcon.setPixmap(QtGui.QPixmap(":/pixmap/02d@2x.png"))
        self.weatherTodayIcon.setScaledContents(False)
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
        self.datetimeFrame.setTabletTracking(False)
        self.datetimeFrame.setAutoFillBackground(False)
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
        self.label.setScaledContents(False)
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
        self.thuesdayFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.thuesdayFrame_2.setGeometry(QtCore.QRect(390, 210, 121, 161))
        self.thuesdayFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thuesdayFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thuesdayFrame_2.setObjectName("thuesdayFrame_2")
        self.fridayFrame = QtWidgets.QFrame(self.centralwidget)
        self.fridayFrame.setGeometry(QtCore.QRect(520, 210, 121, 161))
        self.fridayFrame.setAutoFillBackground(False)
        self.fridayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fridayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fridayFrame.setObjectName("fridayFrame")
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MainWindow"))
        self.weatherToday.setText(_translate("Window", "Sunny"))
        self.label.setText(_translate("Window", "00:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())