# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\QZhao\Desktop\hea\app.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import datetime
import main
from functools import partial
class Ui_MainWindow(object):
        startTime=0
        complete=0
        characterId=''
        dungeon=''
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(782, 362)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")

                
                font = QtGui.QFont()
                font.setPointSize(12)
                
                self.BattleMage = QtWidgets.QPushButton(self.centralwidget)
                self.BattleMage.setGeometry(QtCore.QRect(40, 30, 71, 61))
                self.BattleMage.setFont(font)
                self.BattleMage.setObjectName("BattleMage")
                self.M_Crusader = QtWidgets.QPushButton(self.centralwidget)
                self.M_Crusader.setGeometry(QtCore.QRect(40, 120, 71, 61))
                self.M_Crusader.setFont(font)
                self.M_Crusader.setObjectName("M_Crusader")
                self.F_Laucher = QtWidgets.QPushButton(self.centralwidget)
                self.F_Laucher.setGeometry(QtCore.QRect(140, 30, 71, 61))
                self.F_Laucher.setFont(font)
                self.F_Laucher.setObjectName("F_Laucher")
                self.F_Crusader = QtWidgets.QPushButton(self.centralwidget)
                self.F_Crusader.setGeometry(QtCore.QRect(140, 120, 71, 61))
                self.F_Crusader.setFont(font)
                self.F_Crusader.setObjectName("FM_Crusader")
                self.SwiftMaster = QtWidgets.QPushButton(self.centralwidget)
                self.SwiftMaster.setGeometry(QtCore.QRect(140, 220, 71, 61))
                self.SwiftMaster.setFont(font)
                self.SwiftMaster.setObjectName("SwiftMaster")
                self.SoulBender = QtWidgets.QPushButton(self.centralwidget)
                self.SoulBender.setGeometry(QtCore.QRect(40, 220, 71, 61))
                self.SoulBender.setFont(font)
                self.SoulBender.setAutoRepeatInterval(98)
                self.SoulBender.setObjectName("SoulBender")

                
                self.Anton = QtWidgets.QPushButton(self.centralwidget)
                self.Anton.setGeometry(QtCore.QRect(580, 30, 71, 61))
                self.Anton.setFont(font)
                self.Anton.setObjectName("Anton")
                self.Luke = QtWidgets.QPushButton(self.centralwidget)
                self.Luke.setGeometry(QtCore.QRect(680, 30, 71, 61))
                self.Luke.setFont(font)
                self.Luke.setObjectName("Luke")
                self.DC = QtWidgets.QPushButton(self.centralwidget)
                self.DC.setGeometry(QtCore.QRect(680, 120, 71, 61))
                self.DC.setFont(font)
                self.DC.setObjectName("DC")
                self.Assult = QtWidgets.QPushButton(self.centralwidget)
                self.Assult.setGeometry(QtCore.QRect(580, 120, 71, 61))
                self.Assult.setFont(font)
                self.Assult.setObjectName("Assult")
                self.Beast = QtWidgets.QPushButton(self.centralwidget)
                self.Beast.setGeometry(QtCore.QRect(580, 220, 71, 61))
                self.Beast.setFont(font)
                self.Beast.setObjectName("Beast")                
                self.Tayberrs = QtWidgets.QPushButton(self.centralwidget)
                self.Tayberrs.setGeometry(QtCore.QRect(680, 220, 71, 61))
                self.Tayberrs.setFont(font)
                self.Tayberrs.setObjectName("Tayberrs")

                self.Start = QtWidgets.QPushButton(self.centralwidget)
                self.Start.setGeometry(QtCore.QRect(240, 90, 131, 131))
                self.Start.setFont(font)
                self.Start.setObjectName("Start")
                self.Complete = QtWidgets.QPushButton(self.centralwidget)
                self.Complete.setGeometry(QtCore.QRect(370, 90, 131, 131))
                self.Complete.setFont(font)
                self.Complete.setObjectName("Complete")


                self.CurrentTimeLCD = QtWidgets.QLCDNumber(self.centralwidget)
                self.CurrentTimeLCD.setGeometry(QtCore.QRect(240, 30, 261, 61))
                self.CurrentTimeLCD.setObjectName("CurrentTimeLCD")
                self.CurrentTimeLCD.setDigitCount(8)
                self.StopWatchLCD = QtWidgets.QLCDNumber(self.centralwidget)
                self.StopWatchLCD.setGeometry(QtCore.QRect(240, 220, 261, 61))
                self.StopWatchLCD.setObjectName("StopWatchLCD")
                self.StopWatchLCD.setDigitCount(11)


                
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
                self.menubar.setObjectName("menubar")
                self.menuNothinMenu = QtWidgets.QMenu(self.menubar)
                self.menuNothinMenu.setObjectName("menuNothinMenu")
                self.menu = QtWidgets.QMenu(self.menuNothinMenu)
                self.menu.setObjectName("menu")
                self.menuI_SAID_NOTHING = QtWidgets.QMenu(self.menu)
                self.menuI_SAID_NOTHING.setObjectName("menuI_SAID_NOTHING")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.actionEXIT = QtWidgets.QAction(MainWindow)
                self.actionEXIT.setObjectName("actionEXIT")
                self.menuI_SAID_NOTHING.addAction(self.actionEXIT)
                self.menu.addAction(self.menuI_SAID_NOTHING.menuAction())
                self.menuNothinMenu.addAction(self.menu.menuAction())
                self.menubar.addAction(self.menuNothinMenu.menuAction())

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                self.showTime()
                self.clockInitial()

                # setup ui connect
                self.Start.clicked.connect(self.startClicked)
                self.Complete.clicked.connect(self.completeClicked)
                self.BattleMage.clicked.connect(partial(self.characterSwitch,characterId='Index'))
                self.F_Laucher.clicked.connect(partial(self.characterSwitch,characterId='MisakaMikoto'))
                self.F_Crusader.clicked.connect(partial(self.characterSwitch,characterId='RoraSuchuato'))
                self.M_Crusader.clicked.connect(partial(self.characterSwitch,characterId='DadKirei'))
                self.SoulBender.clicked.connect(partial(self.characterSwitch,characterId='HevenKensera'))
                self.SwiftMaster.clicked.connect(partial(self.characterSwitch,characterId='VentoDeFront'))
                self.Anton.clicked.connect(partial(self.dungeonSwitch,dungeonName='Anton'))
                self.Luke.clicked.connect(partial(self.dungeonSwitch,dungeonName='Luke'))
                self.Assult.clicked.connect(partial(self.dungeonSwitch,dungeonName='Assult'))
                self.DC.clicked.connect(partial(self.dungeonSwitch,dungeonName='DC'))
                self.Beast.clicked.connect(partial(self.dungeonSwitch,dungeonName='Beast'))
                self.Tayberrs.clicked.connect(partial(self.dungeonSwitch,dungeonName='Tayberrs'))


        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                # self.BattleMage.setText(_translate("MainWindow", "Index"))
                # self.M_Crusader.setText(_translate("MainWindow", "Dad\nKirei"))
                # self.F_Laucher.setText(_translate("MainWindow", "Misaka\nMikoto"))
                # self.F_Crusader.setText(_translate("MainWindow", "Rora\nSuchuato"))
                # self.SwiftMaster.setText(_translate("MainWindow", "Vento\nDeFront"))
                # self.SoulBender.setText(_translate("MainWindow", "Heven\nKensera"))
                # self.Luke.setText(_translate("MainWindow", "卢克"))
                # self.Tayberrs.setText(_translate("MainWindow", "泰波\n""尔斯"))
                # self.DC.setText(_translate("MainWindow", "黎明"))
                # self.Assult.setText(_translate("MainWindow", "强袭"))
                # self.Anton.setText(_translate("MainWindow", "安图恩"))
                # self.Beast.setText(_translate("MainWindow", "魔兽"))
                self.Complete.setText(_translate("MainWindow", "Complete"))
                self.Start.setText(_translate("MainWindow", "Start"))
                self.menuNothinMenu.setTitle(_translate("MainWindow", "NothinMenu"))
                self.menu.setTitle(_translate("MainWindow", "????"))
                self.menuI_SAID_NOTHING.setTitle(_translate("MainWindow", "I SAID NOTHING"))
                self.actionEXIT.setText(_translate("MainWindow", "EXIT"))

        def characterSwitch(self,characterId):
                if main.isIdExisted(characterId):
                        self.characterId=characterId
                        print('You has selected ',self.characterId)
                else:
                        pass
        def dungeonSwitch(self,dungeonName):
                if main.isDungeonExisted(dungeonName):
                        self.dungeon=dungeonName
                        print('You has selected ',self.dungeon)
                else:
                        pass      

        def clockInitial(self):
                self.timer=Qt.QTimer(self.CurrentTimeLCD)
                self.timer.start(1000)
                self.timer.timeout.connect(self.showTime)
        def showTime(self):
                #更新时间的显示
                time = Qt.QTime.currentTime()  #获取当前时间
                time_text = time.toString(QtCore.Qt.ISODate) #获取HH:MM:SS格式的时间
                
                self.CurrentTimeLCD.display(time_text) #显示时间
        def startClicked(self):
                if self.timer:
                        self.timer.stop()
                self.complete=0
                self.startTime=datetime.datetime.now()
                self.timer=Qt.QTimer(self.StopWatchLCD)
                # self.timer.setInterval()
                self.timer.start(10)
                self.timer.timeout.connect(self.completeNotClicked)
        def completeNotClicked(self):
                #更新时间的显示
                time = datetime.datetime.now() - self.startTime #获取当前时间与开始时间的差别
                # print(time)
                time_text = str(time)[:-4] #获取HH:MM:SS格式的时间
                
                self.StopWatchLCD.display(time_text) #显示时间
        def completeClicked(self):
                self.timer.stop()
                if self.complete:
                        self.Complete.setText("Complete")
                        if not (self.characterId=='' or self.dungeon==''):
                                main.signed(self.characterId,self.dungeon)
                        self.complete=0
                else:
                        self.complete = self.complete +1                        
                        self.Complete.setText("Update")
                print(self.characterId,self.dungeon,self.complete)
if __name__=='__main__':
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())