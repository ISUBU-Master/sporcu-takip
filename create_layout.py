

from PyQt5 import uic

with open("HomeLayoutUI.py","w",encoding="utf-8") as fout:
    uic.compileUi("Home.ui",fout)


with open("AboutLayoutUI.py","w",encoding="utf-8") as fout:
    uic.compileUi("About.ui",fout)
