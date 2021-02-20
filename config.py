import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from HomeLayoutUI import *
from AboutLayoutUI import *


application = QApplication(sys.argv)
mainWindow=QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()


windowAbout=QDialog()
aboutUI=Ui_Dialog()
aboutUI.setupUi(windowAbout)



        



