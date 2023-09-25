
import winsound
import datetime
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PyQt6.QtSql import *
import sys

from connection import Connection


#import pantalla1_rc
class Pantalla(object):


    #Generates a list of new effects of each QObject
    def effectGenerator(self, list: [QObject]): 
        newList = []
        for elem in list:
            act=QGraphicsOpacityEffect(elem) #Create a new QGraphicsOpacityEffect with the Qobject
            act.setOpacity(1)
            elem.setGraphicsEffect(act)  #Set the effect to the object
            newList.append(act)  #Add the effect to the temporal list            
        return newList


    #This functions creates the lists of labels and effect to actualize the display
    def generarDiccionarios(self):

        #List of box
        self.listaCaja=[self.ticket1,self.ticket2,self.ticket3,self.ticket4,self.ticket5,self.ticket6]

        #List of Num
        self.listaNum=[self.caj1,self.caj2,self.caj3,self.caj4,self.caj5,self.caj6]

        #List of boxGraphicEffect
        self.listaEffCaja= self.effectGenerator(self.listaCaja)

        #List of numGraphicEffect
        self.listaEffNum= self.effectGenerator(self.listaNum)

        #Create the animations
        self.createAnimationGroup()

    def createAnimationGroup(self):
        #Create fade animationGroup
        self.groupOn= []     #[ QAG0,QAG1,QAG..]   ON GROUP ANIMATIONS  
        self.groupOff= []    #OFF GROUP ANIMATIONS

        #Create the animations of the effects and add to the group
        for pos in range(6):        #Generates Vector a QAnimiGroup which have NUM1, CAJ1 EFFECT ON ANIM
            act= QParallelAnimationGroup() 
            act.addAnimation(self.generateAnimateOn(self.listaEffCaja[pos]))
            act.addAnimation(self.generateAnimateOn(self.listaEffNum[pos]))
            self.groupOn.append(act)

        for pos in range(6):        #Generates Vector a QAnimiGroup which have NUM1, CAJ1 EFFECT OFF ANIM
            act2= QParallelAnimationGroup()
            act2.addAnimation(self.generateAnimateOff(self.listaEffCaja[pos]))
            act2.addAnimation(self.generateAnimateOff(self.listaEffNum[pos]))
            self.groupOff.append(act2)
  
    #Animation to fadeOff   
    def generateAnimateOff(self, eff: QGraphicsEffect): #Recieves the effect, retrieves animation of the effect
        animOff = QPropertyAnimation(eff, b"opacity")
        animOff.setDuration(300)
        animOff.setStartValue(1)
        animOff.setEndValue(0)
        return animOff

    #Animation to show on
    def generateAnimateOn(self, eff: QGraphicsEffect): #Recieves the effect, retrieves animation of the effect
        animOn = QPropertyAnimation(eff, b"opacity")
        animOn.setDuration(300)
        animOn.setStartValue(0)
        animOn.setEndValue(1)
        return animOn


    #listaCaja,listaNum
    def refreshDisplay(self, num: int, caja: int, pos: int):
        if pos==0:  #If the pos is 0
            self.groupOff[pos].start() #Fade actual label
            QTimer.singleShot(300, lambda: self.listaNum[pos].setText(f'CAJA {caja}'))
            QTimer.singleShot(300, lambda: self.listaCaja[pos].setText(f'NUMERO {num}')) #Set the text of the label
            QTimer.singleShot(300, lambda: self.groupOn[pos].start()) #Start timer to show new number slowly
        else:
            self.groupOff[pos].start() #Fade actual label
            QTimer.singleShot(300, lambda: self.listaNum[pos].setText(self.listaNum[pos-1].text())) #Set the previus num
            QTimer.singleShot(300, lambda: self.listaCaja[pos].setText(self.listaCaja[pos-1].text())) #set the previus box
            QTimer.singleShot(300, lambda: self.groupOn[pos].start()) #Start timer to show new number slowly
            QTimer.singleShot(600, lambda: self.refreshDisplay(num,caja,pos-1))


    def startTimer(self): #llega el tipo de turno

        self.timer = QTimer() #Create a timer
        self.timer.timeout.connect(lambda: self.consultarProximos()) # self.consultarProximos(self.con) Which connects function "ConsultarProximos"
        self.timer.start(3600) #each 3.6s calls consultarProx and start



    def consultarProximos(self): #exececute a query of bring on the last num called by BOX and actualize displa
        
        #sound= PySide6.QtMultimedia.QSoundEffect()
        
        #Get the time now() => time_now.strftime('%Y-%m-%d %H:%M:%S')
        time_now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.000')        

        #Create a query to get the next display
        query= QSqlQuery(self.con)   #SELF.db is the connection QSqlDatabase already created
        query_proximo=QSqlQuery(self.con)    


        #Query to get the new num
        data_query1= \
        '''BEGIN TRANSACTION;
        DECLARE @proximo_turno INT;

        -- Obtener el próximo turno disponible

        SELECT TOP (1) @proximo_turno=num 
        FROM turnos_actual 
        WHERE (status=2) 
        ORDER BY hora

        -- Asignar el turno a una persona específica (supongamos que la persona tiene el ID 1)
                
        

        SELECT @proximo_turno as num
                         
        COMMIT TRANSACTION;
        '''

        data_query2= \
        '''BEGIN TRANSACTION;
        DECLARE @proximo_turno INT;

        -- Obtener el potencial proximo turno disponible

        SELECT TOP (1) @proximo_turno=num 
        FROM turnos_actual 
        WHERE (status=1) 
        ORDER BY hora        
        
        SELECT @proximo_turno as num
                         
        COMMIT TRANSACTION;
        '''


        query.prepare(data_query1) #Query brings on the next

        query_proximo.prepare(data_query2) #Query searchs the potential next call

        if (query.exec()): #If query succeeds (GET THE NEXT NUMBER)

            query.first()   #Get the first row
            next=query.value(0)  #The first value
   
            self.refreshDisplay(next,'cajaGon',5) #Calls the function refresh display with the values to actualize

            if not(query.isNull(0)) & (query_proximo.exec()): #If query haves a value and query_proximo succeeds
                query_proximo.first()  #Get the first row
                proximo=query_proximo.value(0)
                self.prox.setText(f'PROXIMO NUMERO {proximo}')

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 733)
        MainWindow.setStyleSheet(u"#widget{\n"
"	border-image: url(:/imagenes/img/fondoGris.jpg);\n"
"}\n"
"\n"
"#barraProx{\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"titulos{\n"
"border-bottom: 3px solid black;\n"
"}\n"
"#cajas{\n"
"border-right: 1px solid black;\n"
"}\n"
"#prox{\n"
"color:white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titulos = QWidget(self.widget)
        self.titulos.setObjectName(u"titulos")
        self.titulos.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.titulos)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.titulos)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_8)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.titulos)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_3 = QVBoxLayout(self.widget_9)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.widget_9)


        self.verticalLayout_2.addWidget(self.titulos)

        self.centro = QWidget(self.widget)
        self.centro.setObjectName(u"centro")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centro.sizePolicy().hasHeightForWidth())
        self.centro.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centro)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cajas = QWidget(self.centro)
        self.cajas.setObjectName(u"cajas")
        self.horizontalLayout_2 = QHBoxLayout(self.cajas)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.numAtencion = QWidget(self.cajas)
        self.numAtencion.setObjectName(u"numAtencion")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.numAtencion.sizePolicy().hasHeightForWidth())
        self.numAtencion.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.numAtencion)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.slot_ticket1 = QWidget(self.numAtencion)
        self.slot_ticket1.setObjectName(u"slot_ticket1")
        self.verticalLayout_9 = QVBoxLayout(self.slot_ticket1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ticket1 = QLabel(self.slot_ticket1)
        self.ticket1.setObjectName(u"ticket1")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.ticket1.setFont(font1)
        self.ticket1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.ticket1)


        self.verticalLayout_5.addWidget(self.slot_ticket1)

        self.slot_ticket2 = QWidget(self.numAtencion)
        self.slot_ticket2.setObjectName(u"slot_ticket2")
        self.verticalLayout_10 = QVBoxLayout(self.slot_ticket2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.ticket2 = QLabel(self.slot_ticket2)
        self.ticket2.setObjectName(u"ticket2")
        self.ticket2.setFont(font1)

        self.verticalLayout_10.addWidget(self.ticket2, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.slot_ticket2)

        self.slot_ticket3 = QWidget(self.numAtencion)
        self.slot_ticket3.setObjectName(u"slot_ticket3")
        self.verticalLayout_11 = QVBoxLayout(self.slot_ticket3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.ticket3 = QLabel(self.slot_ticket3)
        self.ticket3.setObjectName(u"ticket3")
        self.ticket3.setFont(font1)

        self.verticalLayout_11.addWidget(self.ticket3, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.slot_ticket3)

        self.slot_ticket4 = QWidget(self.numAtencion)
        self.slot_ticket4.setObjectName(u"slot_ticket4")
        self.verticalLayout_12 = QVBoxLayout(self.slot_ticket4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.ticket4 = QLabel(self.slot_ticket4)
        self.ticket4.setObjectName(u"ticket4")
        self.ticket4.setFont(font1)

        self.verticalLayout_12.addWidget(self.ticket4, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.slot_ticket4)

        self.slot_ticket5 = QWidget(self.numAtencion)
        self.slot_ticket5.setObjectName(u"slot_ticket5")
        self.verticalLayout_13 = QVBoxLayout(self.slot_ticket5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.ticket5 = QLabel(self.slot_ticket5)
        self.ticket5.setObjectName(u"ticket5")
        self.ticket5.setFont(font1)

        self.verticalLayout_13.addWidget(self.ticket5, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.slot_ticket5)

        self.slot_ticket6 = QWidget(self.numAtencion)
        self.slot_ticket6.setObjectName(u"slot_ticket6")
        self.verticalLayout_14 = QVBoxLayout(self.slot_ticket6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.ticket6 = QLabel(self.slot_ticket6)
        self.ticket6.setObjectName(u"ticket6")
        self.ticket6.setFont(font1)

        self.verticalLayout_14.addWidget(self.ticket6, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.slot_ticket6)


        self.horizontalLayout_2.addWidget(self.numAtencion)

        self.cajaAtencion = QWidget(self.cajas)
        self.cajaAtencion.setObjectName(u"cajaAtencion")
        self.cajaAtencion.setMinimumSize(QSize(100, 0))
        self.verticalLayout_6 = QVBoxLayout(self.cajaAtencion)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.slotCaja1 = QWidget(self.cajaAtencion)
        self.slotCaja1.setObjectName(u"slotCaja1")
        self.verticalLayout_20 = QVBoxLayout(self.slotCaja1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.caj1 = QLabel(self.slotCaja1)
        self.caj1.setObjectName(u"caj1")
        self.caj1.setFont(font1)

        self.verticalLayout_20.addWidget(self.caj1)


        self.verticalLayout_6.addWidget(self.slotCaja1)

        self.slotCaja2 = QWidget(self.cajaAtencion)
        self.slotCaja2.setObjectName(u"slotCaja2")
        self.verticalLayout_21 = QVBoxLayout(self.slotCaja2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.caj2 = QLabel(self.slotCaja2)
        self.caj2.setObjectName(u"caj2")
        self.caj2.setFont(font1)

        self.verticalLayout_21.addWidget(self.caj2)


        self.verticalLayout_6.addWidget(self.slotCaja2)

        self.slotCaja3 = QWidget(self.cajaAtencion)
        self.slotCaja3.setObjectName(u"slotCaja3")
        self.verticalLayout_22 = QVBoxLayout(self.slotCaja3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.caj3 = QLabel(self.slotCaja3)
        self.caj3.setObjectName(u"caj3")
        self.caj3.setFont(font1)

        self.verticalLayout_22.addWidget(self.caj3)


        self.verticalLayout_6.addWidget(self.slotCaja3)

        self.slotCaja4 = QWidget(self.cajaAtencion)
        self.slotCaja4.setObjectName(u"slotCaja4")
        self.verticalLayout_23 = QVBoxLayout(self.slotCaja4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.caj4 = QLabel(self.slotCaja4)
        self.caj4.setObjectName(u"caj4")
        self.caj4.setFont(font1)

        self.verticalLayout_23.addWidget(self.caj4)


        self.verticalLayout_6.addWidget(self.slotCaja4)

        self.slotCaja5 = QWidget(self.cajaAtencion)
        self.slotCaja5.setObjectName(u"slotCaja5")
        self.verticalLayout_24 = QVBoxLayout(self.slotCaja5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.caj5 = QLabel(self.slotCaja5)
        self.caj5.setObjectName(u"caj5")
        self.caj5.setFont(font1)

        self.verticalLayout_24.addWidget(self.caj5)


        self.verticalLayout_6.addWidget(self.slotCaja5)

        self.slotCaja6 = QWidget(self.cajaAtencion)
        self.slotCaja6.setObjectName(u"slotCaja6")
        self.verticalLayout_25 = QVBoxLayout(self.slotCaja6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.caj6 = QLabel(self.slotCaja6)
        self.caj6.setObjectName(u"caj6")
        self.caj6.setFont(font1)

        self.verticalLayout_25.addWidget(self.caj6)


        self.verticalLayout_6.addWidget(self.slotCaja6)


        self.horizontalLayout_2.addWidget(self.cajaAtencion)


        self.horizontalLayout.addWidget(self.cajas)

        self.c_numAtencion = QWidget(self.centro)
        self.c_numAtencion.setObjectName(u"c_numAtencion")
        self.horizontalLayout_3 = QHBoxLayout(self.c_numAtencion)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.c_persona = QWidget(self.c_numAtencion)
        self.c_persona.setObjectName(u"c_persona")
        sizePolicy1.setHeightForWidth(self.c_persona.sizePolicy().hasHeightForWidth())
        self.c_persona.setSizePolicy(sizePolicy1)
        self.verticalLayout_7 = QVBoxLayout(self.c_persona)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.persona1 = QWidget(self.c_persona)
        self.persona1.setObjectName(u"persona1")
        self.verticalLayout_19 = QVBoxLayout(self.persona1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.nom1 = QLabel(self.persona1)
        self.nom1.setObjectName(u"nom1")
        self.nom1.setFont(font1)

        self.verticalLayout_19.addWidget(self.nom1, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.persona1)

        self.persona2 = QWidget(self.c_persona)
        self.persona2.setObjectName(u"persona2")
        self.verticalLayout_18 = QVBoxLayout(self.persona2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.nom2 = QLabel(self.persona2)
        self.nom2.setObjectName(u"nom2")
        self.nom2.setFont(font1)

        self.verticalLayout_18.addWidget(self.nom2, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.persona2)

        self.persona3 = QWidget(self.c_persona)
        self.persona3.setObjectName(u"persona3")
        self.verticalLayout_17 = QVBoxLayout(self.persona3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.nom3 = QLabel(self.persona3)
        self.nom3.setObjectName(u"nom3")
        self.nom3.setFont(font1)

        self.verticalLayout_17.addWidget(self.nom3, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.persona3)

        self.persona4 = QWidget(self.c_persona)
        self.persona4.setObjectName(u"persona4")
        self.verticalLayout_16 = QVBoxLayout(self.persona4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.nom4 = QLabel(self.persona4)
        self.nom4.setObjectName(u"nom4")
        self.nom4.setFont(font1)

        self.verticalLayout_16.addWidget(self.nom4, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.persona4)

        self.persona5 = QWidget(self.c_persona)
        self.persona5.setObjectName(u"persona5")
        self.verticalLayout_26 = QVBoxLayout(self.persona5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.nom5 = QLabel(self.persona5)
        self.nom5.setObjectName(u"nom5")
        self.nom5.setFont(font1)

        self.verticalLayout_26.addWidget(self.nom5, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.persona5)

        self.persona6 = QWidget(self.c_persona)
        self.persona6.setObjectName(u"persona6")
        self.verticalLayout_15 = QVBoxLayout(self.persona6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.nom6 = QLabel(self.persona6)
        self.nom6.setObjectName(u"nom6")
        self.nom6.setFont(font1)

        self.verticalLayout_15.addWidget(self.nom6, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.persona6)


        self.horizontalLayout_3.addWidget(self.c_persona)

        self.c_consuAtencion = QWidget(self.c_numAtencion)
        self.c_consuAtencion.setObjectName(u"c_consuAtencion")
        self.c_consuAtencion.setMinimumSize(QSize(100, 0))
        self.verticalLayout_8 = QVBoxLayout(self.c_consuAtencion)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.CA_cont1 = QWidget(self.c_consuAtencion)
        self.CA_cont1.setObjectName(u"CA_cont1")
        self.verticalLayout_32 = QVBoxLayout(self.CA_cont1)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.c_llamado1 = QLabel(self.CA_cont1)
        self.c_llamado1.setObjectName(u"c_llamado1")
        self.c_llamado1.setFont(font1)

        self.verticalLayout_32.addWidget(self.c_llamado1)


        self.verticalLayout_8.addWidget(self.CA_cont1)

        self.CA_cont2 = QWidget(self.c_consuAtencion)
        self.CA_cont2.setObjectName(u"CA_cont2")
        self.verticalLayout_31 = QVBoxLayout(self.CA_cont2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.c_llamado2 = QLabel(self.CA_cont2)
        self.c_llamado2.setObjectName(u"c_llamado2")
        self.c_llamado2.setFont(font1)

        self.verticalLayout_31.addWidget(self.c_llamado2)


        self.verticalLayout_8.addWidget(self.CA_cont2)

        self.CA_cont3 = QWidget(self.c_consuAtencion)
        self.CA_cont3.setObjectName(u"CA_cont3")
        self.verticalLayout_30 = QVBoxLayout(self.CA_cont3)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.c_llamado3 = QLabel(self.CA_cont3)
        self.c_llamado3.setObjectName(u"c_llamado3")
        self.c_llamado3.setFont(font1)

        self.verticalLayout_30.addWidget(self.c_llamado3)


        self.verticalLayout_8.addWidget(self.CA_cont3)

        self.CA_cont4 = QWidget(self.c_consuAtencion)
        self.CA_cont4.setObjectName(u"CA_cont4")
        self.verticalLayout_29 = QVBoxLayout(self.CA_cont4)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.c_llamado4 = QLabel(self.CA_cont4)
        self.c_llamado4.setObjectName(u"c_llamado4")
        self.c_llamado4.setFont(font1)

        self.verticalLayout_29.addWidget(self.c_llamado4)


        self.verticalLayout_8.addWidget(self.CA_cont4)

        self.CA_cont5 = QWidget(self.c_consuAtencion)
        self.CA_cont5.setObjectName(u"CA_cont5")
        self.verticalLayout_28 = QVBoxLayout(self.CA_cont5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.c_llamado5 = QLabel(self.CA_cont5)
        self.c_llamado5.setObjectName(u"c_llamado5")
        self.c_llamado5.setFont(font1)

        self.verticalLayout_28.addWidget(self.c_llamado5)


        self.verticalLayout_8.addWidget(self.CA_cont5)

        self.CA_cont6 = QWidget(self.c_consuAtencion)
        self.CA_cont6.setObjectName(u"CA_cont6")
        self.verticalLayout_27 = QVBoxLayout(self.CA_cont6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.c_llamado6 = QLabel(self.CA_cont6)
        self.c_llamado6.setObjectName(u"c_llamado6")
        self.c_llamado6.setFont(font1)

        self.verticalLayout_27.addWidget(self.c_llamado6)


        self.verticalLayout_8.addWidget(self.CA_cont6)


        self.horizontalLayout_3.addWidget(self.c_consuAtencion)


        self.horizontalLayout.addWidget(self.c_numAtencion)


        self.verticalLayout_2.addWidget(self.centro)

        self.barraProx = QWidget(self.widget)
        self.barraProx.setObjectName(u"barraProx")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.barraProx.sizePolicy().hasHeightForWidth())
        self.barraProx.setSizePolicy(sizePolicy2)
        self.barraProx.setMinimumSize(QSize(0, 40))
        self.barraProx.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.barraProx)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.prox = QLabel(self.barraProx)
        self.prox.setObjectName(u"prox")
        self.prox.setFont(font1)
        self.prox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.prox)


        self.verticalLayout_2.addWidget(self.barraProx)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        #Create the list of labels and respective effects
        self.generarDiccionarios()

        #Before set all the template of the window, started the timer and displaying called nums
        self.startTimer()

        #Create a new Connection
        self.db=Connection() 

        #Gets de DB Options from connection
        self.con = self.db.createConnection() 

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ATENCION ENTRADA", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CONSULTORIO", None))
        self.ticket1.setText(QCoreApplication.translate("MainWindow", u"NUMERO X", None))
        self.prox.setText(QCoreApplication.translate("MainWindow", u"PROXIMO EN CAJA", None))
        self.caj1.setText(QCoreApplication.translate("MainWindow", u"CAJA X", None))
        self.ticket2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ticket3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ticket4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ticket5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ticket6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        
        self.caj2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.caj3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.caj4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.caj5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.caj6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nom1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nom2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nom3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nom4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nom5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nom6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.c_llamado1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.c_llamado2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.c_llamado3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.c_llamado4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.c_llamado5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.c_llamado6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))

    # retranslateUi

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vent=QMainWindow()
    ui= Pantalla()
    ui.setupUi(vent)
    vent.show()
    sys.exit(app.exec())


#this is how i can change the LABELS
#Setear textLabel en NUM {db.caja}      CAJA QUE LLAMA
#self.caj{pos}.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))

#Setear textLabel en NUM {db.num}      NUMERO A LLAMAR
#self.ticket1.setText(QCoreApplication.translate("MainWindow", u"NUMERO X", None))

#Setear textLabel en NUM {db.MINnum}      PROX NUM A LLAMAR
# self.prox.setText()

'''#Creo template y seteo el estilo en ventana
        self.pop = Pop()
        self.pop.setupUi(self.window)

        #No frame, no background, show
        self.window.setWindowFlags(Qt.FramelessWindowHint)
        self.window.setAttribute(Qt.WA_TranslucentBackground)

        #Show pop with the opening animation
        self.window.show()
        self.animateOn(self.window)
'''