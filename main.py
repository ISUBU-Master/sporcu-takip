import sys
from config import ui,application
from db import curs,conn
import functions

        

ui.createButton.clicked.connect(functions.CREATE)




sys.exit(application.exec_())
