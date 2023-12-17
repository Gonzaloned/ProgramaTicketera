from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from ui_NewLogin import Login
from ui_selector import Selector
import os

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vent=QMainWindow()
    login= Login() #Creo la ventana login
    login.setupUi(vent) #Paso la ventana para configuraciones
    vent.show() #Show
    sys.exit(app.exec())
