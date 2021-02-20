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
    
    try:
        curs.execute("INSERT INTO athletes (tcId,firstName,lastName,sportClub,athleteWeight,athleteGender,maritalStatus,branchOfSport,birthday) VALUES (?,?,?,?,?,?,?,?,?)",(tcId,firstName,lastName,sportClub,athleteWeight,athleteGender,maritalStatus,branchOfSport,birthday))
        conn.commit()
        FETCH()
        ui.statusbar.showMessage("Yeni kayıt başarıyla eklendi",10000)
    except Exception as error:
        ui.statusbar.showMessage("Beklenmedik bir hata meydana geldi: "+str(error),10000)
        

def FETCH():
    ui.athleteData.clear()
    ui.athleteData.setHorizontalHeaderLabels(("#","Tc Kimlik No","Sporcu Adı","Sporcu Soyadı",\
    "Klüp Adı","Kilosu","Cinsiyet","Medeni Hal","Branş","Doğum Tarihi"))
    
    ui.athleteData.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    try:
        curs.execute("SELECT * FROM athletes")
    except Exception as error:
        ui.statusbar.showMessage("Beklenmedik bir hata meydana geldi: "+str(error),10000)
        
    
    for rowIndex,rowItem in enumerate(curs):
        for columnIndex,columnItem in enumerate(rowItem):
            ui.athleteData.setItem(rowIndex,columnIndex,QTableWidgetItem(str(columnItem)))
    ui.tcId.clear()
    ui.firstName.clear()
    ui.lastName.clear()
    ui.sportClub.setCurrentIndex(0)
    ui.athleteWeight.setValue(55)
    ui.athleteGender.currentText()
    
    curs.execute("SELECT COUNT(*) FROM athletes")
    
    ui.dataSize.setText(str(curs.fetchone()[0]))

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
            ui.statusbar.showMessage("Beklenmedik bir hata meydana geldi: "+str(error),10000)
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi...",10000)

def SEARCH():
    tcId = ui.tcId.text()
    firstName = ui.firstName.text()
    lastName = ui.lastName.text()
    try:
        curs.execute("SELECT * FROM athletes WHERE tcId=? OR firstName=? OR lastName=? OR (firstName=? AND lastName=?)",(tcId,firstName,lastName,firstName,lastName))
        conn.commit()
        ui.athleteData.clear()
        for rowIndex,rowItem in enumerate(curs):
            for columnIndex,columnItem in enumerate(rowItem):
                ui.athleteData.setItem(rowIndex,columnIndex,QTableWidgetItem(str(columnItem)))
                
    except Exception as error:
        ui.statusbar.showMessage("Beklenmedik bir hata meydana geldi: "+str(error),10000)
    


def SET_FORM():
    item = ui.athleteData.selectedItems()
    ui.tcId.setText(item[1].text())
    ui.firstName.setText(item[2].text())
    ui.lastName.setText(item[3].text())
    ui.sportClub.setCurrentText(item[4].text())
    if (item[8].text()=="Futbol"):
        ui.branchOfSport.item(0).setSelected(True)
        ui.branchOfSport.setCurrentItem(ui.branchOfSport.item(0))
    if (item[8].text()=="Atletizm"):
        ui.branchOfSport.item(1).setSelected(True)
        ui.branchOfSport.setCurrentItem(ui.branchOfSport.item(1))
    if (item[8].text()=="Basketbol"):
        ui.branchOfSport.item(2).setSelected(True)
        ui.branchOfSport.setCurrentItem(ui.branchOfSport.item(2))
    if (item[8].text()=="Boks"):
        ui.branchOfSport.item(3).setSelected(True)
        ui.branchOfSport.setCurrentItem(ui.branchOfSport.item(3))
    if (item[8].text()=="Güreş"):
        ui.branchOfSport.item(4).setSelected(True)
        ui.branchOfSport.setCurrentItem(ui.branchOfSport.item(4))
    if (item[8].text()=="Hentbol"):
        ui.branchOfSport.item(5).setSelected(True)
        ui.branchOfSport.setCurrentItem(ui.branchOfSport.item(5))
    
    
    ui.athleteGender.setCurrentText(item[6].text())
    y=int(item[9].text()[0:4])
    m=int(item[9].text()[5:7])
    d=int(item[9].text()[8:10])
    ui.birthday.setSelectedDate(QtCore.QDate(y,m,d))
    
    if item[7].text()=="Evli":
        ui.maritalStatus.setChecked(True)
    else:
        ui.maritalStatus.setChecked(False)
    
    ui.athleteWeight.setValue(int(item[5].text()))
    

def UPDATE():
    answer=QMessageBox.question(mainWindow,"KAYIT GÜNCELLE","Kaydı güncellemek istediğinize emin misiniz?",QMessageBox.Yes|QMessageBox.No)
    
    if answer==QMessageBox.Yes:
        try:
            item = ui.athleteData.selectedItems()
            _id=int(item[0].text())
            _tcId = ui.tcId.text()
            _firstName = ui.firstName.text()
            _lastName = ui.lastName.text()
            _sportClub = ui.sportClub.currentText()
            _athleteWeight = ui.athleteWeight.value()
            _athleteGender = ui.athleteGender.currentText()
            if ui.maritalStatus.isChecked() :
                _maritalStatus="Evli"
            else:
                _maritalStatus="Bekar"
            _branchOfSport = ui.branchOfSport.currentItem().text()
            _birthday = ui.birthday.selectedDate().toString(QtCore.Qt.ISODate)
            
            curs.execute("UPDATE athletes SET \
             tcId=?,\
             firstName=?,\
             lastName=?,\
             sportClub=?,\
             athleteWeight=?,\
             athleteGender=?,\
             maritalStatus=?,\
             branchOfSport=?,\
             birthday=? WHERE id=?",(_tcId,_firstName,_lastName,_sportClub,_athleteWeight,_athleteGender,_maritalStatus,_branchOfSport,_birthday,_id))
            conn.commit()
            FETCH()
        except Exception as error:
            ui.statusbar.showMessage("Beklenmedik bir hata meydana geldi: "+str(error))
    else:
        ui.statusbar.showMessage("Güncelleme iptal edildi.",10000)
    
    
