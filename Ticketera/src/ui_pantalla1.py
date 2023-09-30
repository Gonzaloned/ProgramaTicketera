
from typing import Optional
from PySide6.QtCore import *
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *
import pantalla1_rc

from ui_calculadora import Calculadora
from ui_pantalla3 import Pantalla3

class Pantalla1(object):    


    def animateOn(self, win: QMainWindow):
        self.eff = QGraphicsOpacityEffect(win)
        self.eff.setOpacity(0.3)
        win.setGraphicsEffect(self.eff)

        self.anim = QPropertyAnimation(self.eff, b"opacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(0.2)
        self.anim.setEndValue(1)
        self.anim.start()   

    def crearVentanaSinDni(self):
        self.window3= QMainWindow()
        self.ui_screen3 = Pantalla3()

        #Create win3 sending the dni and the new MainWindow object
        self.ui_screen3.setupUi(self.window3,'null', self.window3)

        #Create a new Graphic effect in window 3
        self.eff = QGraphicsOpacityEffect(self.window3)
        #Set the opacity in the effect
        self.eff.setOpacity(0.0)
        #Set the graphics effect in the window
        self.window3.setGraphicsEffect(self.eff)

        #Create a timer to close calc
        QTimer.singleShot(2000, lambda: self.calc_Win.close())

        #Display fs w3 and start animation
        self.window3.showFullScreen()
        #self.animateOn(self.window3)

    def mostrar2(self):
        self.calc= Calculadora()
        self.calc_Win= QMainWindow()
        self.calc.setupUi(self.calc_Win)
        self.calc_Win.setWindowFlags(Qt.FramelessWindowHint)
        self.calc_Win.setAttribute(Qt.WA_TranslucentBackground)
        self.calc_Win.show()
        self.animateOn(self.calc_Win)

    def setupUi(self, main):
        self.ventana=main

        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(1155, 946)
        main.setStyleSheet(u"\n"
"#wMain{\n"
"	background-image: url(:/imagenes/img/fondo.jpg);\n"
"}\n"
"\n"
"#center{\n"
"	border-image: url(:/imagenes/img/fondo_sin.jpg);\n"
"	background-attachment: fixed;\n"
"	border-radius: 45px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#pushButton{\n"
"	border-radius:15px;\n"
"  	border-style: solid;\n"
"    border-width: 1.5px;\n"
"	border-color: rgba(0, 73, 113,30);\n"
"	color: rgb(0, 73, 113);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.wMain = QWidget(main)
        self.wMain.setObjectName(u"wMain")
        self.wMain.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.wMain)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.wMain)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.center = QWidget(self.widget)
        self.center.setObjectName(u"center")
        self.center.setMinimumSize(QSize(600, 400))
        self.center.setMaximumSize(QSize(600, 400))
        self.verticalLayout_3 = QVBoxLayout(self.center)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titulo = QWidget(self.center)
        self.titulo.setObjectName(u"titulo")
        self.horizontalLayout = QHBoxLayout(self.titulo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.titulo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.titulo)

        self.sin_dni = QWidget(self.center)
        self.sin_dni.setObjectName(u"sin_dni")
        self.verticalLayout_4 = QVBoxLayout(self.sin_dni)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.sin_dni)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setItalic(False)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_3.addWidget(self.sin_dni)

        self.buttonDni = QWidget(self.center)
        self.buttonDni.setObjectName(u"buttonDni")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDni.sizePolicy().hasHeightForWidth())
        self.buttonDni.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.buttonDni)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.buttonDni, clicked = lambda: self.mostrar2())
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(300, 75))
        self.pushButton.setMaximumSize(QSize(600, 150))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.pushButton.setFont(font2)

        self.verticalLayout_6.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.buttonDni)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setUnderline(True)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.buttonDni)


        self.verticalLayout_2.addWidget(self.center)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        main.setCentralWidget(self.wMain)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)

    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("main", u"BIENVENIDOS", None))
        self.label_4.setText(QCoreApplication.translate("main", u"Para comenzar ingrese su DNI", None))
        self.pushButton.setText(QCoreApplication.translate("main", u"Ingresar DNI", None))
        #self.label_3.setText(QCoreApplication.translate("main", u"NO TENGO DNI", None))
    # retranslateUi

