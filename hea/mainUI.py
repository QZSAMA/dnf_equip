# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdCurrentTime = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdCurrentTime.setGeometry(QtCore.QRect(500, 0, 301, 81))
        self.lcdCurrentTime.setObjectName("lcdCurrentTime")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(490, 200, 311, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.lcdCountDown = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdCountDown.setGeometry(QtCore.QRect(500, 80, 301, 81))
        self.lcdCountDown.setObjectName("lcdCountDown")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 110, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
        self.menubar.setObjectName("menubar")
        self.menuMainMenu = QtWidgets.QMenu(self.menubar)
        self.menuMainMenu.setObjectName("menuMainMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionUpdateYourChar = QtWidgets.QAction(MainWindow)
        self.actionUpdateYourChar.setObjectName("actionUpdateYourChar")
        self.menuMainMenu.addAction(self.actionUpdateYourChar)
        self.menubar.addAction(self.menuMainMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lcdCountDown.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Count Down:"))
        self.label_2.setText(_translate("MainWindow", "Current Time:"))
        self.menuMainMenu.setTitle(_translate("MainWindow", "MainMenu"))
        self.actionUpdateYourChar.setText(_translate("MainWindow", "UpdateYourChar"))

