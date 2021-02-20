import sys
from config import ui,mainWindow,application
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


def EXIT():
    answer=QMessageBox.question(mainWindow,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",QMessageBox.Yes|QMessageBox.No)
    if answer==QMessageBox.Yes:
        conn.close()
        sys.exit(application.exec_())
    else:
        mainWindow.show()
     
    
def DELETE():
    answer=QMessageBox.question(mainWindow,"KAYIT SİL","Kaydı silmek istediğinize emin misiniz?",QMessageBox.Yes|QMessageBox.No)
    if answer==QMessageBox.Yes:
        selectItemTcId = ui.athleteData.selectedItems()[1].text()
        try:
            curs.execute("DELETE FROM athletes WHERE tcId='%s'" %(selectItemTcId))
            conn.commit()
            FETCH()
            ui.statusbar.showMessage("Kayıt Silme İşlemi Başarıyla Gerçekleşti...",10000)
        except Exception as error:
            ui.statusbar.showMessage("Beklenmedik bir hata meydana geldi:"+str(error),10000)
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi...",10000)
