from config import ui
from db import curs,conn
from PyQt5 import QtCore
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


def CREATE():
    tcId = ui.tcId.text()
    firstName = ui.firstName.text()
    lastName = ui.lastName.text()
    sportClub = ui.sportClub.currentText()
    athleteWeight = ui.athleteWeight.value()
    athleteGender = ui.athleteGender.currentText()
    if ui.maritalStatus.isChecked() :
        maritalStatus="Evli"
    else:
        maritalStatus="Bekar"
    branchOfSport = ui.branchOfSport.currentItem().text()
    birthday = ui.birthday.selectedDate().toString(QtCore.Qt.ISODate)
    
    curs.execute("INSERT INTO athletes (tcId,firstName,lastName,sportClub,athleteWeight,athleteGender,maritalStatus,branchOfSport,birthday) VALUES (?,?,?,?,?,?,?,?,?)",(tcId,firstName,lastName,sportClub,athleteWeight,athleteGender,maritalStatus,branchOfSport,birthday))
  
    conn.commit()
    FETCH()
        

def FETCH():
    ui.athleteData.clear()
    ui.athleteData.setHorizontalHeaderLabels(("#","Tc Kimlik No","Sporcu Adı","Sporcu Soyadı",\
    "Klüp Adı","Branş","Cinsiyet","Doğum Tarihi","Medeni Hal","Sporcu Kilosu"))
    
    ui.athleteData.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT * FROM athletes")
    
    for rowIndex,rowItem in enumerate(curs):
        for columnIndex,columnItem in enumerate(rowItem):
            ui.athleteData.setItem(rowIndex,columnIndex,QTableWidgetItem(str(columnItem)))

