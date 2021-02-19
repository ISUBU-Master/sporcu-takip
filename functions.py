from config import ui
from db import curs,conn
from PyQt5 import QtCore


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
        
