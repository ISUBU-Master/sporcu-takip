import sys
from config import ui,application
from db import curs,conn
import functions

        
functions.FETCH()
ui.createButton.clicked.connect(functions.CREATE)
ui.fetchButton.clicked.connect(functions.FETCH)
ui.exitButton.clicked.connect(functions.EXIT)
ui.deleteButton.clicked.connect(functions.DELETE)




sys.exit(application.exec_())
