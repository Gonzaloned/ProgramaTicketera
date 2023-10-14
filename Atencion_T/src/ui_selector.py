import datetime
import json
import os
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel
from connection import Connection
import fondos_rc
from ui_options import SettingsWindow

import manejar_datos

class Selector(object):

###########################################################################################
###         FUNCTIONS CALLED BY THE BUTTONS
###########################################################################################


    #This method sends to db a indicator of recall last num
    def callLastNumAgain(self):

        #Get the last num info
        last_num = manejar_datos.getLastNum()
        last_time = manejar_datos.getLastTime()

        #Insert the last num info in the db
        notify_query=f'''
        BEGIN TRANSACTION;
        INSERT INTO advice(num, hora) VALUES('{last_num}','{last_time}');
        COMMIT TRANSACTION; 
        '''
        self.db.queryExecution(notify_query) #Executes the query

    #Calls next shift
    def llamarProximo(self, tipo:int):
        
        #This methods calls "Manejar_datos.py" to get box_num and caller name
        box_num= manejar_datos.getBoxNum()
        name= manejar_datos.getName()

        #Status 1: created, 2: called, 3: displayed
        #Select first turn in the table and change status to called
        transaction=f'''BEGIN TRANSACTION;

        DECLARE @proximo_turno INT;

        -- Obtener el próximo turno disponible

        SELECT TOP (1) @proximo_turno=num 
        FROM turnos_actual 
        WHERE (status=1 and tipo={tipo}) 
        ORDER BY hora

        -- Asignar el turno cambiando status y caja llamadora
                
        UPDATE turnos_actual 
        SET status = 2, atiende_usuario='{name}', atiende_caja='{box_num}'
        WHERE num = @proximo_turno;

        -- Guardar el ultimo turno para notificar
        SELECT @proximo_turno

        COMMIT TRANSACTION;
        '''
        #Execute the transaction
        self.db.queryExecution(transaction)

        #this final method code
        #writes the json file last_num and save the info just in case to need a notification

        #Get the first value of a result query
        query:QSqlQuery= self.db.getQuery()
        query.first()
        last_num = query.value(0) 

        # 1. Read last turn file
        with open(os.path.join(os.getcwd(), "src", "data", "last_num.json"), "r", encoding='utf-8') as archivo:
            data = json.load(archivo)

        # 2. Set the last num and time
        data['num']=last_num
        data['hour']= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.000')

        # 3. Rewrite the json file
        with open(os.path.join(os.getcwd(), "src", "data", "last_num.json"), "w", encoding='utf-8') as archivo:
            json.dump(data, archivo)    

    #Opens the options    
    def abrirOpciones(self):
        self.options_window= QMainWindow()
        self.ui= SettingsWindow()
        self.ui.setupUi(self.options_window,self.db) #Paso la ventana para configuraciones
        self.options_window.setAttribute(Qt.WA_TranslucentBackground) #set translucent background
        self.options_window.show() #Show

    #Close program
    def cerrarSelectora(self):
        self.ventana.close()


    #This function calculates the position in the screen
    def location_on_the_screen(self):    
        screen = QGuiApplication.primaryScreen().availableGeometry()
        #print(f' screen: {screen.width()}  {screen.height()}')
        
        widget = self.ventana.geometry()
        #print(f' widget: {widget.width()}  {widget.height()}')

        x = screen.width() - widget.width()
        y = screen.height() - widget.height()

        #print(f' X: {x} Y: {y}')
        self.ventana.move(x, y)


    def setupUi(self, MainWindow):
        self.ventana=MainWindow

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(94, 405)
        MainWindow.setStyleSheet(u"\n"
"#frame{\n"
"	border-image: url(:/fondos/img/fondos/fondo_sin.jpg);\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton{\n"
"	border-radius:30px;\n"
"	border: 0.1px solid white;\n"
"	background-color: rgba(255, 255, 255, 160);\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgba(66, 66, 66, 150);\n"
"	border: 0.5px solid white;\n"
"}")
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.main)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cont1 = QWidget(self.frame)
        self.cont1.setObjectName(u"cont1")
        self.cont1.setMinimumSize(QSize(92, 81))
        self.horizontalLayout_6 = QHBoxLayout(self.cont1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.llamar = QPushButton(self.cont1)
        self.llamar.setObjectName(u"llamar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.llamar.sizePolicy().hasHeightForWidth())
        self.llamar.setSizePolicy(sizePolicy)
        self.llamar.setMinimumSize(QSize(60, 60))
        self.llamar.setMaximumSize(QSize(60, 60))
        icon = QIcon()
        icon.addFile(u":/iconosWhite/img/iconsAtencion/bell-2-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.llamar.setIcon(icon)
        self.llamar.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.llamar)


        self.verticalLayout.addWidget(self.cont1)

        self.cont2 = QWidget(self.frame)
        self.cont2.setObjectName(u"cont2")
        self.cont2.setMinimumSize(QSize(92, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.cont2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sinTurno = QPushButton(self.cont2)
        self.sinTurno.setObjectName(u"sinTurno")
        sizePolicy.setHeightForWidth(self.sinTurno.sizePolicy().hasHeightForWidth())
        self.sinTurno.setSizePolicy(sizePolicy)
        self.sinTurno.setMinimumSize(QSize(60, 60))
        self.sinTurno.setMaximumSize(QSize(60, 60))
        icon1 = QIcon()
        icon1.addFile(u":/iconosWhite/img/iconsAtencion/letter-s-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.sinTurno.setIcon(icon1)
        self.sinTurno.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.sinTurno)


        self.verticalLayout.addWidget(self.cont2, 0, Qt.AlignVCenter)

        self.cont3 = QWidget(self.frame)
        self.cont3.setObjectName(u"cont3")
        self.cont3.setMinimumSize(QSize(92, 81))
        self.horizontalLayout_3 = QHBoxLayout(self.cont3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.conTurno = QPushButton(self.cont3)
        self.conTurno.setObjectName(u"conTurno")
        sizePolicy.setHeightForWidth(self.conTurno.sizePolicy().hasHeightForWidth())
        self.conTurno.setSizePolicy(sizePolicy)
        self.conTurno.setMinimumSize(QSize(60, 60))
        self.conTurno.setMaximumSize(QSize(60, 60))
        icon2 = QIcon()
        icon2.addFile(u":/iconosWhite/img/iconsAtencion/letter-t-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.conTurno.setIcon(icon2)
        self.conTurno.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.conTurno)


        self.verticalLayout.addWidget(self.cont3)

        self.cont4 = QWidget(self.frame)
        self.cont4.setObjectName(u"cont4")
        self.cont4.setMinimumSize(QSize(92, 81))
        self.horizontalLayout_4 = QHBoxLayout(self.cont4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.settings = QPushButton(self.cont4)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(60, 60))
        self.settings.setMaximumSize(QSize(60, 60))
        icon3 = QIcon()
        icon3.addFile(u":/iconosWhite/img/iconsAtencion/settings-5-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon3)
        self.settings.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.settings)


        self.verticalLayout.addWidget(self.cont4)

        self.cont5 = QWidget(self.frame)
        self.cont5.setObjectName(u"cont5")
        self.cont5.setMinimumSize(QSize(92, 81))
        self.horizontalLayout_5 = QHBoxLayout(self.cont5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.exit = QPushButton(self.cont5)
        self.exit.setObjectName(u"exit")
        self.exit.setMinimumSize(QSize(60, 60))
        self.exit.setMaximumSize(QSize(60, 60))
        icon4 = QIcon()
        icon4.addFile(u":/iconosWhite/img/iconsAtencion/x-mark-3-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit.setIcon(icon4)
        self.exit.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.exit)


        self.verticalLayout.addWidget(self.cont5)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        #INITIAL WINDOW CONFIG
        self.db= Connection() #Create the db object

        self.ventana.setWindowFlags(Qt.FramelessWindowHint)   #Not show windows bar
        self.ventana.setAttribute(Qt.WA_TranslucentBackground) #set translucent background
        self.location_on_the_screen() #position of the panel

        ##EVENTS
        self.llamar.clicked.connect(lambda: self.callLastNumAgain())
        self.sinTurno.clicked.connect(lambda: self.llamarProximo(1))
        self.conTurno.clicked.connect(lambda: self.llamarProximo(2))
        self.settings.clicked.connect(lambda: self.abrirOpciones())
        self.exit.clicked.connect(lambda: self.cerrarSelectora())
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.llamar.setText("")
        self.sinTurno.setText("")
        self.conTurno.setText("")
        self.settings.setText("")
        self.exit.setText("")
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vent=QMainWindow()
    login= Selector() #Creo la ventana login
    login.setupUi(vent) #Paso la ventana para configuraciones
    vent.show() #Show
    sys.exit(app.exec())
