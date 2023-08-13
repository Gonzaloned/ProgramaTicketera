import sys
import typing
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from connection import Connection

from ui_pantalla3 import Seleccion
from ui_pantalla1 import Pantalla1
from ui_calculadora import Calculadora

class VentanaVacia(QMainWindow):
    def __init__(self):

        #Start init of QMainWindow
        super().__init__()

        #Making a Pantalla1 object to load the skin on QMainWindow
        self.ui= Pantalla1()
        self.ui.setupUi(self)

        #to not show Windows border
        self.setWindowFlags(Qt.FramelessWindowHint)

        #Show window of class VentanaVacia -> QMainWindow
        self.showFullScreen()

        #Defining events
        self.ui.pushButton.clicked.connect(self.mostrarVentana2)

        #Var
        self.dni=''
        
    def mostrarVentana2(self):

        #Making a new window
        self.ventana2 = QMainWindow()

        #Making a Calculadora object to load the skin on ventana2
        self.calc= Calculadora()
        self.calc.setupUi(self.ventana2)

        #to not show Windows border
        self.ventana2.setWindowFlags(Qt.FramelessWindowHint)
    
        #Show new window
        self.ventana2.show()

        #defining events of Calculadora (Numbers display)
        self.calc.btn0.clicked.connect(lambda: self.agregarDig("0"))
        self.calc.btn1.clicked.connect(lambda: self.agregarDig("1"))
        self.calc.btn2.clicked.connect(lambda: self.agregarDig("2"))
        self.calc.btn3.clicked.connect(lambda: self.agregarDig("3"))
        self.calc.btn4.clicked.connect(lambda: self.agregarDig("4"))
        self.calc.btn5.clicked.connect(lambda: self.agregarDig("5"))
        self.calc.btn6.clicked.connect(lambda: self.agregarDig("6"))
        self.calc.btn7.clicked.connect(lambda: self.agregarDig("7"))
        self.calc.btn8.clicked.connect(lambda: self.agregarDig("8"))
        self.calc.btn9.clicked.connect(lambda: self.agregarDig("9"))
        self.calc.btnDel.clicked.connect(lambda: self.eliminarDig())
        self.calc.btnOK.clicked.connect(lambda: self.checkDNI())

    def agregarDig(self,dig):
        self.dni= self.dni + dig
        self.calc.texto.setText(self.dni)
    
    def eliminarDig(self):
        self.dni = self.dni[:-1]
        self.calc.texto.setText(self.dni)

    def checkDNI(self):
        #Solicitud servidor
        print(self.dni)
        self.mostrarVentana3()
        self.ventana2.close()

    #####################################################################
    #####################################################################

    def mostrarVentana3(self):

        #Making a new window
        self.ventana3 = QMainWindow()

        #Making a Calculadora object to load the skin on ventana2
        self.ui3=Seleccion()
        self.ui3.setupUi(self.ventana3)

        #to not show Windows border
        self.ventana3.setWindowFlags(Qt.FramelessWindowHint)
    
        #Show new window
        self.ventana3.showFullScreen()

        db=Connection()
        self.ui3.btn1.clicked.connect(lambda: db.executeQuery('''INSERT INTO dbo.turnos_cajas(dni,hora) VALUES (111,'2014-03-25 15:30:00')'''))
        self.ui3.btn2.clicked.connect(lambda: db.executeQuery('''INSERT INTO dbo.turnos_cajas(dni,hora) VALUES (222,'2014-03-25 15:30:00')'''))
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana= VentanaVacia()
    sys.exit(app.exec())

#Connect to database
