# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 641, 441))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(310, 30, 314, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.birthday = QtWidgets.QCalendarWidget(self.widget)
        self.birthday.setObjectName("birthday")
        self.verticalLayout_4.addWidget(self.birthday)
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(30, 30, 271, 401))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tcId = QtWidgets.QLineEdit(self.widget1)
        self.tcId.setMaximumSize(QtCore.QSize(120, 16777215))
        self.tcId.setMaxLength(11)
        self.tcId.setObjectName("tcId")
        self.horizontalLayout.addWidget(self.tcId)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.firstName = QtWidgets.QLineEdit(self.widget1)
        self.firstName.setMaximumSize(QtCore.QSize(120, 16777215))
        self.firstName.setObjectName("firstName")
        self.horizontalLayout_2.addWidget(self.firstName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lastName = QtWidgets.QLineEdit(self.widget1)
        self.lastName.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lastName.setObjectName("lastName")
        self.horizontalLayout_3.addWidget(self.lastName)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.sportClub = QtWidgets.QComboBox(self.widget1)
        self.sportClub.setMaximumSize(QtCore.QSize(100, 16777215))
        self.sportClub.setObjectName("sportClub")
        self.sportClub.addItem("")
        self.sportClub.addItem("")
        self.sportClub.addItem("")
        self.sportClub.addItem("")
        self.sportClub.addItem("")
        self.sportClub.addItem("")
        self.sportClub.addItem("")
        self.sportClub.addItem("")
        self.sportClub.addItem("")
        self.sportClub.addItem("")
        self.horizontalLayout_7.addWidget(self.sportClub)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.athleteWeight = QtWidgets.QSpinBox(self.widget1)
        self.athleteWeight.setMinimum(50)
        self.athleteWeight.setMaximum(135)
        self.athleteWeight.setObjectName("athleteWeight")
        self.horizontalLayout_4.addWidget(self.athleteWeight)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.athleteGender = QtWidgets.QComboBox(self.widget1)
        self.athleteGender.setObjectName("athleteGender")
        self.athleteGender.addItem("")
        self.athleteGender.addItem("")
        self.athleteGender.addItem("")
        self.horizontalLayout_5.addWidget(self.athleteGender)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.maritalStatus = QtWidgets.QCheckBox(self.widget1)
        self.maritalStatus.setObjectName("maritalStatus")
        self.horizontalLayout_6.addWidget(self.maritalStatus)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 19))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.branchOfSport = QtWidgets.QListWidget(self.widget1)
        self.branchOfSport.setMaximumSize(QtCore.QSize(16777215, 110))
        self.branchOfSport.setObjectName("branchOfSport")
        item = QtWidgets.QListWidgetItem()
        self.branchOfSport.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.branchOfSport.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.branchOfSport.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.branchOfSport.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.branchOfSport.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.branchOfSport.addItem(item)
        self.verticalLayout_3.addWidget(self.branchOfSport)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.athleteData = QtWidgets.QTableWidget(self.centralwidget)
        self.athleteData.setGeometry(QtCore.QRect(10, 470, 821, 261))
        self.athleteData.setRowCount(10)
        self.athleteData.setColumnCount(92)
        self.athleteData.setObjectName("athleteData")
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(660, 40, 181, 241))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.createButton = QtWidgets.QPushButton(self.widget2)
        self.createButton.setObjectName("createButton")
        self.verticalLayout_2.addWidget(self.createButton)
        self.updateButton = QtWidgets.QPushButton(self.widget2)
        self.updateButton.setObjectName("updateButton")
        self.verticalLayout_2.addWidget(self.updateButton)
        self.fetchButton = QtWidgets.QPushButton(self.widget2)
        self.fetchButton.setObjectName("fetchButton")
        self.verticalLayout_2.addWidget(self.fetchButton)
        self.searchButton = QtWidgets.QPushButton(self.widget2)
        self.searchButton.setObjectName("searchButton")
        self.verticalLayout_2.addWidget(self.searchButton)
        self.deleteButton = QtWidgets.QPushButton(self.widget2)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout_2.addWidget(self.deleteButton)
        self.exitButton = QtWidgets.QPushButton(self.widget2)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_2.addWidget(self.exitButton)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(20, 740, 187, 21))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.dataSize = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dataSize.setFont(font)
        self.dataSize.setTextFormat(QtCore.Qt.AutoText)
        self.dataSize.setObjectName("dataSize")
        self.horizontalLayout_8.addWidget(self.dataSize)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 24))
        self.menubar.setObjectName("menubar")
        self.menuYar_m = QtWidgets.QMenu(self.menubar)
        self.menuYar_m.setObjectName("menuYar_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.infoMenu = QtWidgets.QAction(MainWindow)
        self.infoMenu.setObjectName("infoMenu")
        self.menuYar_m.addAction(self.infoMenu)
        self.menubar.addAction(self.menuYar_m.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Sporcu Bilgileri"))
        self.label_9.setText(_translate("MainWindow", "Doğum Tarihi:"))
        self.label.setText(_translate("MainWindow", "TC Kimlik No:"))
        self.label_2.setText(_translate("MainWindow", "Sporcu Adı:"))
        self.label_3.setText(_translate("MainWindow", "Sporcu Soyadı:"))
        self.label_4.setText(_translate("MainWindow", "Spor Klübü:"))
        self.sportClub.setItemText(0, _translate("MainWindow", "--SEÇİNİZ--"))
        self.sportClub.setItemText(1, _translate("MainWindow", "Fenerbahçe"))
        self.sportClub.setItemText(2, _translate("MainWindow", "Galatasaray"))
        self.sportClub.setItemText(3, _translate("MainWindow", "Beşiktaş"))
        self.sportClub.setItemText(4, _translate("MainWindow", "Trabzonspor"))
        self.sportClub.setItemText(5, _translate("MainWindow", "İstanbul Başakşehir SK"))
        self.sportClub.setItemText(6, _translate("MainWindow", "Bursaspor"))
        self.sportClub.setItemText(7, _translate("MainWindow", "Orduspor"))
        self.sportClub.setItemText(8, _translate("MainWindow", "Gençlerbirliği"))
        self.sportClub.setItemText(9, _translate("MainWindow", "MKE Ankaragücü"))
        self.label_5.setText(_translate("MainWindow", "Sporcu Kilosu:"))
        self.label_6.setText(_translate("MainWindow", "Sporcu Cinsiyeti:"))
        self.athleteGender.setItemText(0, _translate("MainWindow", "--SEÇİNİZ--"))
        self.athleteGender.setItemText(1, _translate("MainWindow", "Erkek"))
        self.athleteGender.setItemText(2, _translate("MainWindow", "Kadın"))
        self.label_7.setText(_translate("MainWindow", "Medeni Hal:"))
        self.maritalStatus.setText(_translate("MainWindow", "Evli"))
        self.label_8.setText(_translate("MainWindow", "Branşı:"))
        __sortingEnabled = self.branchOfSport.isSortingEnabled()
        self.branchOfSport.setSortingEnabled(False)
        item = self.branchOfSport.item(0)
        item.setText(_translate("MainWindow", "Futbol"))
        item = self.branchOfSport.item(1)
        item.setText(_translate("MainWindow", "Atletizm"))
        item = self.branchOfSport.item(2)
        item.setText(_translate("MainWindow", "Basketbol"))
        item = self.branchOfSport.item(3)
        item.setText(_translate("MainWindow", "Boks"))
        item = self.branchOfSport.item(4)
        item.setText(_translate("MainWindow", "Güreş"))
        item = self.branchOfSport.item(5)
        item.setText(_translate("MainWindow", "Hentbol"))
        self.branchOfSport.setSortingEnabled(__sortingEnabled)
        self.createButton.setText(_translate("MainWindow", "Kayıt Ekle"))
        self.updateButton.setText(_translate("MainWindow", "Güncelle"))
        self.fetchButton.setText(_translate("MainWindow", "Kayıt Listele"))
        self.searchButton.setText(_translate("MainWindow", "Kayıt Ara"))
        self.deleteButton.setText(_translate("MainWindow", "Kayıt Sil"))
        self.exitButton.setText(_translate("MainWindow", "Çıkış"))
        self.label_10.setText(_translate("MainWindow", "Kayıt Sayısı:"))
        self.dataSize.setText(_translate("MainWindow", "Yükleniyor..."))
        self.menuYar_m.setTitle(_translate("MainWindow", "Yarım"))
        self.infoMenu.setText(_translate("MainWindow", "Hakkında"))

