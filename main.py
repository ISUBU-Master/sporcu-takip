import sys
from config import ui,application
from db import curs,conn
import functions

        
functions.FETCH()
ui.createButton.clicked.connect(functions.CREATE)
ui.fetchButton.clicked.connect(functions.FETCH)
ui.exitButton.clicked.connect(functions.EXIT)
ui.deleteButton.clicked.connect(functions.DELETE)
ui.searchButton.clicked.connect(functions.SEARCH)
ui.athleteData.itemSelectionChanged.connect(functions.SET_FORM)
ui.updateButton.clicked.connect(functions.UPDATE)



sys.exit(application.exec_())
