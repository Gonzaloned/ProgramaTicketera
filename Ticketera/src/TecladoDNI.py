from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from SeleccionTurno import Pantalla3

class TecladoDNI(object):

    def animateOn(self):
        
        self.anim = QPropertyAnimation(self.eff, b"opacity")
        self.anim.setDuration(2000)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1)
        self.anim.start()


    def agregarDig(self,dig):
        self.dni= self.dni + dig
        self.texto.setText(self.dni)
    
    def eliminarDig(self):
        if self.dni == "":
            self.ventanaActualDni.close()
        else:
            self.dni = ""
            self.texto.setText(self.dni)

    def centrarVentana(self):
        # Obtiene el tamaño de la pantalla
        screen = QGuiApplication.primaryScreen().availableGeometry()

        relative_width=int(screen.width()*0.9)
        relative_height=int(screen.height()*0.9)

        # Calcula las coordenadas para centrar la calc
        x = (screen.width() - relative_width) // 2
        y = (screen.height() - relative_height) // 2

        #Seteo el tamaño de la calculadora segun el tamaño de la pantalla
        self.ventanaActualDni.setFixedSize(relative_width,relative_height)

        # Mueve la calc a las coordenadas centradas
        self.ventanaActualDni.move(x, y)

    def checkDNI(self):
        self.ventanaSeleccionTurno= QMainWindow()
        self.botonesUI = Pantalla3()

        #Create win3 sending the dni and the new MainWindow object
        self.botonesUI.setupUi(self.ventanaSeleccionTurno,self.dni, self.db)

        #Create a new Graphic effect in window 3
        self.eff = QGraphicsOpacityEffect(self.ventanaSeleccionTurno)
        #Set the opacity in the effect
        self.eff.setOpacity(0.0)
        #Set the graphics effect in the window
        self.ventanaSeleccionTurno.setGraphicsEffect(self.eff)

        #Create a timer to close calc
        QTimer.singleShot(1000, lambda: self.ventanaActualDni.close())

        #Display fs w3 and start animation
        #self.window3.showFullScreen()
        self.ventanaSeleccionTurno.show()
        self.ventanaSeleccionTurno.setWindowModality(Qt.ApplicationModal)
        self.ventanaSeleccionTurno.setWindowTitle("Seleccionador turno")
        self.ventanaSeleccionTurno.setWindowIcon(QIcon(r"C:\Ticketera\img\logo_sinFondo.png"))
        self.ventanaSeleccionTurno.raise_()
        self.animateOn()
        

    def setupUi(self, main:QMainWindow, database):
        self.ventanaActualDni= main
        self.db = database

        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(915, 798)
        main.setStyleSheet(u"#main{\n"
"background:transparent;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#frame{\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(157, 19, 45);\n"
"	color: rgba(255, 255, 255,200);\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: 50px Arial Black;\n"
"    border-width: 2px;\n"
"	border-color: rgba(148, 75, 77,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(106, 13, 32);\n"
"	color: rgba(255, 255, 255,100);\n"
"	border-color: rgba(148, 75, 77,255);\n"
"}\n"
"\n"
"#texto{\n"
"	background-color: rgb(203, 203, 203);\n"
"\n"
"}")
        self.base = QWidget(main)
        self.base.setObjectName(u"base")
        self.base.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.base)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.base)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.c_texto = QWidget(self.frame)
        self.c_texto.setObjectName(u"c_texto")
        self.c_texto.setMinimumSize(QSize(0, 100))
        self.c_texto.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_6 = QHBoxLayout(self.c_texto)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.texto = QLabel(self.c_texto)
        self.texto.setObjectName(u"texto")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texto.sizePolicy().hasHeightForWidth())
        self.texto.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.texto.setFont(font)
        self.texto.setStyleSheet(u"#QPushButton{\n"
"	background-color: rgb(170, 170, 127);\n"
"}")
        self.texto.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.texto)


        self.verticalLayout_2.addWidget(self.c_texto)

        self.text = QWidget(self.frame)
        self.text.setObjectName(u"text")
        self.text.setStyleSheet(u"#QPushButton{\n"
"size:100x100\n"
"}")
        self.gridLayout = QGridLayout(self.text)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.B1 = QWidget(self.text)
        self.B1.setObjectName(u"B1")
        self.horizontalLayout = QHBoxLayout(self.B1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn1 = QPushButton(self.B1)
        self.btn1.setObjectName(u"btn1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setBold(False)
        font1.setItalic(False)
        self.btn1.setFont(font1)

        self.horizontalLayout.addWidget(self.btn1)


        self.gridLayout.addWidget(self.B1, 0, 0, 1, 1)

        self.B2 = QWidget(self.text)
        self.B2.setObjectName(u"B2")
        self.verticalLayout_3 = QVBoxLayout(self.B2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn2 = QPushButton(self.B2)
        self.btn2.setObjectName(u"btn2")
        sizePolicy1.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy1)
        self.btn2.setFont(font1)

        self.verticalLayout_3.addWidget(self.btn2)


        self.gridLayout.addWidget(self.B2, 0, 1, 1, 1)

        self.B3 = QWidget(self.text)
        self.B3.setObjectName(u"B3")
        self.horizontalLayout_2 = QHBoxLayout(self.B3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn3 = QPushButton(self.B3)
        self.btn3.setObjectName(u"btn3")
        sizePolicy1.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy1)
        self.btn3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn3)


        self.gridLayout.addWidget(self.B3, 0, 2, 1, 1)

        self.B4 = QWidget(self.text)
        self.B4.setObjectName(u"B4")
        self.horizontalLayout_3 = QHBoxLayout(self.B4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn4 = QPushButton(self.B4)
        self.btn4.setObjectName(u"btn4")
        sizePolicy1.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy1)
        self.btn4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.btn4)


        self.gridLayout.addWidget(self.B4, 1, 0, 1, 1)

        self.B5 = QWidget(self.text)
        self.B5.setObjectName(u"B5")
        self.horizontalLayout_4 = QHBoxLayout(self.B5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn5 = QPushButton(self.B5)
        self.btn5.setObjectName(u"btn5")
        sizePolicy1.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy1)
        self.btn5.setFont(font1)

        self.horizontalLayout_4.addWidget(self.btn5)


        self.gridLayout.addWidget(self.B5, 1, 1, 1, 1)

        self.B6 = QWidget(self.text)
        self.B6.setObjectName(u"B6")
        self.horizontalLayout_5 = QHBoxLayout(self.B6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn6 = QPushButton(self.B6)
        self.btn6.setObjectName(u"btn6")
        sizePolicy1.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy1)
        self.btn6.setFont(font1)

        self.horizontalLayout_5.addWidget(self.btn6)


        self.gridLayout.addWidget(self.B6, 1, 2, 1, 1)

        self.B7 = QWidget(self.text)
        self.B7.setObjectName(u"B7")
        self.horizontalLayout_8 = QHBoxLayout(self.B7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn7 = QPushButton(self.B7)
        self.btn7.setObjectName(u"btn7")
        sizePolicy1.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy1)
        self.btn7.setFont(font1)

        self.horizontalLayout_8.addWidget(self.btn7)


        self.gridLayout.addWidget(self.B7, 2, 0, 1, 1)

        self.B8 = QWidget(self.text)
        self.B8.setObjectName(u"B8")
        self.horizontalLayout_9 = QHBoxLayout(self.B8)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn8 = QPushButton(self.B8)
        self.btn8.setObjectName(u"btn8")
        sizePolicy1.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy1)
        self.btn8.setFont(font1)

        self.horizontalLayout_9.addWidget(self.btn8)


        self.gridLayout.addWidget(self.B8, 2, 1, 1, 1)

        self.B9 = QWidget(self.text)
        self.B9.setObjectName(u"B9")
        self.horizontalLayout_10 = QHBoxLayout(self.B9)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn9 = QPushButton(self.B9)
        self.btn9.setObjectName(u"btn9")
        sizePolicy1.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy1)
        self.btn9.setFont(font1)

        self.horizontalLayout_10.addWidget(self.btn9)


        self.gridLayout.addWidget(self.B9, 2, 2, 1, 1)

        self.DEL = QWidget(self.text)
        self.DEL.setObjectName(u"DEL")
        self.horizontalLayout_11 = QHBoxLayout(self.DEL)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btnDel = QPushButton(self.DEL)
        self.btnDel.setObjectName(u"btnDel")
        sizePolicy1.setHeightForWidth(self.btnDel.sizePolicy().hasHeightForWidth())
        self.btnDel.setSizePolicy(sizePolicy1)
        self.btnDel.setFont(font1)

        self.horizontalLayout_11.addWidget(self.btnDel)


        self.gridLayout.addWidget(self.DEL, 3, 0, 1, 1)

        self.B0 = QWidget(self.text)
        self.B0.setObjectName(u"B0")
        self.horizontalLayout_7 = QHBoxLayout(self.B0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn0 = QPushButton(self.B0)
        self.btn0.setObjectName(u"btn0")
        sizePolicy1.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy1)
        self.btn0.setFont(font1)

        self.horizontalLayout_7.addWidget(self.btn0)


        self.gridLayout.addWidget(self.B0, 3, 1, 1, 1)

        self.OK = QWidget(self.text)
        self.OK.setObjectName(u"OK")
        self.horizontalLayout_12 = QHBoxLayout(self.OK)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btnOK = QPushButton(self.OK)
        self.btnOK.setObjectName(u"btnOK")
        sizePolicy1.setHeightForWidth(self.btnOK.sizePolicy().hasHeightForWidth())
        self.btnOK.setSizePolicy(sizePolicy1)
        self.btnOK.setFont(font1)

        self.horizontalLayout_12.addWidget(self.btnOK)


        self.gridLayout.addWidget(self.OK, 3, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.text)


        self.verticalLayout.addWidget(self.frame)

        main.setCentralWidget(self.base)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)

        #Vars
        #Save this wind
        self.centrarVentana()

        #Create DNI label
        self.dni=''


        #EVENTS
        self.btn0.clicked.connect(lambda: self.agregarDig("0"))
        self.btn1.clicked.connect(lambda: self.agregarDig("1"))
        self.btn2.clicked.connect(lambda: self.agregarDig("2"))
        self.btn3.clicked.connect(lambda: self.agregarDig("3"))
        self.btn4.clicked.connect(lambda: self.agregarDig("4"))
        self.btn5.clicked.connect(lambda: self.agregarDig("5"))
        self.btn6.clicked.connect(lambda: self.agregarDig("6"))
        self.btn7.clicked.connect(lambda: self.agregarDig("7"))
        self.btn8.clicked.connect(lambda: self.agregarDig("8"))
        self.btn9.clicked.connect(lambda: self.agregarDig("9"))
        self.btnDel.clicked.connect(lambda: self.eliminarDig())
        self.btnOK.clicked.connect(lambda: self.checkDNI())  

    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"MainWindow", None))
        self.texto.setText("")
        self.btn1.setText(QCoreApplication.translate("main", u"1", None))
        self.btn2.setText(QCoreApplication.translate("main", u"2", None))
        self.btn3.setText(QCoreApplication.translate("main", u"3", None))
        self.btn4.setText(QCoreApplication.translate("main", u"4", None))
        self.btn5.setText(QCoreApplication.translate("main", u"5", None))
        self.btn6.setText(QCoreApplication.translate("main", u"6", None))
        self.btn7.setText(QCoreApplication.translate("main", u"7", None))
        self.btn8.setText(QCoreApplication.translate("main", u"8", None))
        self.btn9.setText(QCoreApplication.translate("main", u"9", None))
        self.btnDel.setText(QCoreApplication.translate("main", u"DEL", None))
        self.btn0.setText(QCoreApplication.translate("main", u"0", None))
        self.btnOK.setText(QCoreApplication.translate("main", u"OK", None))
    # retranslateUi

