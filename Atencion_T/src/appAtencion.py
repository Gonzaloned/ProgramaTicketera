from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from ui_NewLogin import Login
from ui_selector import Selector


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vent=QMainWindow()
    login= Login() #Creo la ventana login
    login.setupUi(vent) #Paso la ventana para configuraciones
    vent.show() #Show
    sys.exit(app.exec())
