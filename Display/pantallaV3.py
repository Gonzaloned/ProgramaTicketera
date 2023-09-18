import datetime
from PySide6.QtCore import *
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)
from PyQt6.QtSql import *

from PyQt6.QtMultimediaWidgets import *
from PyQt6.QtMultimedia import *

import pantalla1_rc
import pantalla1_rc
import sys


from multiprocessing import Process

import requests

from soundplayer import SoundPlayer

#Global f to delete layout widget
def deleteItemsOfLayout(layout:QVBoxLayout):
    if layout is not None:
        while layout.count():        
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())


class Pantalla(object):

    def databaseNext(self): #exececute a query of bring on the last num called by BOX and actualize displa
        
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

    def refreshTime(self):
        #Get the actual time in HH:MM
        time_now=datetime.datetime.now().strftime('%H:%M')

        #Put the time in the label
        self.time.setText(time_now)


    def refreshWeather(self):
        #Uses an api to get the temp in kelvin, using a connector with lat, lon and account key
        #That request retrieves a json with all the data
        lat= "-34.90407623790362"
        lon= "-57.94973360159151"
        key= 'b8674863bb11fe6782c8e7b8183a3a47'

        #URL To request the data
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'

        #Request -> gets a json
        res= requests.get(url)

        #Open the json
        data= res.json()
        
        #Save the temp data of the json (In kelvin)
        temp=data['main']['temp']

        #Pass Kelvin to Celsius
        tempC=temp-273.15

        #Put temp in label
        self.temp.setText(f'{str(round(tempC))}C')

    def setupVideo(self):
        self.videoOutput= self.makeVideoWidget()
        self.mediaPlayer= self.makeMediaPlayer()

    def makeMediaPlayer(self):
        mediaPlayer= QMediaPlayer()
        mediaPlayer.setVideoOutput(self.videoOutput)
        return mediaPlayer
    
    def makeVideoWidget(self):
        videoOutput= QVideoWidget()
        vbox =QVBoxLayout()
        vbox.addWidget(videoOutput)
        self.videoWidget.setLayout(vbox)
        return videoOutput
        #layout4

    def iniciarVideo(self):
        self.mediaPlayer.set

        
    def animationColor(self, elem:QWidget):
        #Change the color between blue and white
        elem.setStyleSheet(u"QLabel{background-color: rgb(4, 42, 79);color:white;border-radius:2px;}")
        #blue	background-color: rgb(4, 42, 79);color:white;
        #white 	background-color: rgb(204, 204, 204); color:rgb(4, 42, 79);
        QTimer.singleShot(1000, lambda: elem.setStyleSheet(u"QLabel{background-color: rgb(204, 204, 204); color:rgb(4, 42, 79);;border-radius:2px;}"))

        QTimer.singleShot(2000, lambda: elem.setStyleSheet(u"QLabel{background-color: rgb(4, 42, 79);color:white;border-radius:2px;}"))

        QTimer.singleShot(3000,lambda: elem.setStyleSheet(u"QLabel{background-color: rgb(204, 204, 204); color:rgb(4, 42, 79);;border-radius:2px;}"))

        QTimer.singleShot(4000, lambda:elem.setStyleSheet(u"QLabel{background-color: rgb(4, 42, 79);color:white;border-radius:2px;}"))

        QTimer.singleShot(5000, lambda: elem.setStyleSheet(u"QLabel{background-color: rgb(204, 204, 204); color:rgb(4, 42, 79);;border-radius:2px;}"))

        QTimer.singleShot(6000, lambda:elem.setStyleSheet(u"QLabel{background-color: rgb(4, 42, 79);color:white;border-radius:2px;}"))

        QTimer.singleShot(7000, lambda: elem.setStyleSheet(u"QLabel{background-color: rgb(204, 204, 204); color:rgb(4, 42, 79);;border-radius:2px;}"))

        QTimer.singleShot(8000, lambda:elem.setStyleSheet(u"QLabel{background-color: rgb(4, 42, 79);color:white;border-radius:2px;}"))

        QTimer.singleShot(9000, lambda: elem.setStyleSheet(u"QLabel{background-color: rgb(204, 204, 204); color:rgb(4, 42, 79);;border-radius:2px;}"))

        QTimer.singleShot(10000, lambda:elem.setStyleSheet(u"QLabel{background-color: rgb(4, 42, 79);color:white;border-radius:2px;}"))

        QTimer.singleShot(11000, lambda: elem.setStyleSheet(u"QLabel{background-color: rgb(204, 204, 204); color:rgb(4, 42, 79);;border-radius:2px;}"))

    def createNewLayout(self, num: int, caja: int):
        #This method actualizes the box list order to the actual
        ultima=self.list_box[4]

        #Get the childs of the Box QWidget [QHLayout,Qlabel(num),QLabel(caja)]
        childs= ultima.children()
        childs[1].setText('gon') #Set the num in the QLabel
        childs[2].setText('DATABASE') #the the caja in the QLabel
        for i in range(1,5):
            self.list_box[i] = self.list_box[i-1]
        self.list_box[0] = ultima 
        self.animationColor(ultima)



    def showNew(self):

        #Create a new layout
        
        #Add all the boxes to the layout

        ''''''
            
        #delete actual layout
        '''childs = self.nums.children()
        print('tipos antes')
        for e in childs:
            print(type(e))'''

        #childs[0].deleteLater()
        #deleteItemsOfLayout(childs[0])
        

        '''childs2:[QObject] = self.nums.children()
        print('tipos despues')
        for e in childs2:
            print(type(e))'''


        
        
        newLayout= QVBoxLayout(self.nums)
        for i in range(0,5):     
            self.list_box[i].setParent(self.nums)
            newLayout.addWidget(self.list_box[i])


        

        #self.refreshLayout()


        #self.updateBoxList()

        #numbersNext=(0,0)
        #self.databaseNext(numbersNext)

        

        #Set new layout
        #self.verticalLayout_7.addLayout(newLayout)



        #Play mp3 file (Search how to play parallel)
        #mp3_player.play(path_mp3)

        #Execute color animation on new number
        

        #Refresh the order of boxes in list
        #QTimer.singleShot(500, lambda: self.updateBoxList())





                    
    '''def playVideo(self):
        #QMediaPlayer
        #https://doc.qt.io/qtforpython-6/PySide6/QtMultimedia/QMediaPlayer.html
        filename = "src/2.mp3"
        player = QMediaPlayer()
        audio_output = QAudioOutput()
        player.setAudioOutput(audio_output)
        player.setSource(QUrl.fromLocalFile(filename))
        audio_output.setVolume(50)
        player.play()'''

    def footerBarAnimation(self):
        print('footer starts')
        self.animation = QPropertyAnimation(self.labelDesplazable,b'geometry')
        self.animation.setDuration(10000)

        self.labelDesplazable.setGeometry(-330, 9, 327, 44) #Initial Position
        rect = self.labelDesplazable.geometry() #Get the geometry
        self.animation.setStartValue(rect) #Set the geometry animation value
        rect.translate(2260,0) #Transpose X to right
        self.animation.setEndValue(rect) #Set the end geo value
        self.animation.start()  #Start


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 678)
        MainWindow.setStyleSheet(u"#borde_top {\n"
"	background-color: qlineargradient(spread:pad, x1:0.977, y1:0.636409, x2:0.125, y2:0.636636, stop:0 rgba(4, 42, 79,255), stop:1 rgba(0, 73, 113,255));\n"
"	border-radius:2px;\n"
"}\n"
"#borde_top QLabel{\n"
"	color:white;\n"
"}\n"
"\n"
"#widget{\n"
"	background-image: url(:/img/src/img/grisSinFondo.jpg);\n"
"}\n"
"\n"
"\n"
"\n"
"#borde_video{\n"
"	border-image: url(:/img/src/img/fondo_sin.jpg);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"#videoWidget{\n"
"	\n"
"	border-image: url(:/img/src/img/logo.jpeg);\n"
"	\n"
"}\n"
"#titulo_llamado{\n"
"	background-color: rgb(4, 42, 79);\n"
"	color:white;\n"
"	border-radius:2px;\n"
"}\n"
"#borde_turnos{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	\n"
"}\n"
"\n"
"#box_titulo QLabel{\n"
"	background-color: rgb(204, 204, 204);\n"
"\n"
"	color:	rgb(4, 42, 79);\n"
"	border-radius:2px;\n"
"\n"
"}\n"
"\n"
"#nums QLabel{\n"
"	background-color: rgb(204, 204, 204);\n"
"\n"
"	color:	rgb(4, 42, 79);\n"
"	border-radius:2px;\n"
"\n"
"}\n"
"\n"
"#borde_bottom{\n"
"	background-colo"
                        "r: rgb(4, 42, 79);\n"
"	color:white;\n"
"}\n"
"#borde_bottom QLabel{\n"
"	background-color: rgb(4, 42, 79);\n"
"	color:white;\n"
"}\n"
"\n"
"")
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
        self.top_box = QWidget(self.widget)
        self.top_box.setObjectName(u"top_box")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_box.sizePolicy().hasHeightForWidth())
        self.top_box.setSizePolicy(sizePolicy)
        self.top_box.setMinimumSize(QSize(0, 50))
        self.verticalLayout_12 = QVBoxLayout(self.top_box)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(40, 30, 600, 10)
        self.borde_top = QWidget(self.top_box)
        self.borde_top.setObjectName(u"borde_top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.borde_top.sizePolicy().hasHeightForWidth())
        self.borde_top.setSizePolicy(sizePolicy1)
        self.borde_top.setMinimumSize(QSize(300, 40))
        self.borde_top.setMaximumSize(QSize(400, 16777215))
        self.horizontalLayout_10 = QHBoxLayout(self.borde_top)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 0, 10, 0)
        self.label_3 = QLabel(self.borde_top)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.time = QLabel(self.borde_top)
        self.time.setObjectName(u"time")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.time.setFont(font1)
        self.time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.time)

        self.temp = QLabel(self.borde_top)
        self.temp.setObjectName(u"temp")
        self.temp.setFont(font1)
        self.temp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.temp)


        self.verticalLayout_12.addWidget(self.borde_top)


        self.verticalLayout_2.addWidget(self.top_box)

        self.fondo = QWidget(self.widget)
        self.fondo.setObjectName(u"fondo")
        self.horizontalLayout = QHBoxLayout(self.fondo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.fondo)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(40, 0, 40, 100)
        self.borde_video = QWidget(self.widget_5)
        self.borde_video.setObjectName(u"borde_video")
        self.borde_video.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.borde_video)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 25, 15, 25)
        self.videoWidget = QWidget(self.borde_video)
        self.videoWidget.setObjectName(u"videoWidget")

        self.verticalLayout_4.addWidget(self.videoWidget)


        self.verticalLayout_3.addWidget(self.borde_video)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.fondo)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, 60, 60)
        self.borde_turnos = QWidget(self.widget_6)
        self.borde_turnos.setObjectName(u"borde_turnos")
        self.verticalLayout_5 = QVBoxLayout(self.borde_turnos)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 0, 20, 20)
        self.base_turnos = QWidget(self.borde_turnos)
        self.base_turnos.setObjectName(u"base_turnos")
        self.verticalLayout_6 = QVBoxLayout(self.base_turnos)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.base_titulo = QWidget(self.base_turnos)
        self.base_titulo.setObjectName(u"base_titulo")
        sizePolicy.setHeightForWidth(self.base_titulo.sizePolicy().hasHeightForWidth())
        self.base_titulo.setSizePolicy(sizePolicy)
        self.base_titulo.setMinimumSize(QSize(0, 50))
        self.verticalLayout_10 = QVBoxLayout(self.base_titulo)
        self.verticalLayout_10.setSpacing(1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 1)
        self.titulo_llamado = QLabel(self.base_titulo)
        self.titulo_llamado.setObjectName(u"titulo_llamado")
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.titulo_llamado.setFont(font2)
        self.titulo_llamado.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.titulo_llamado)

        self.box_titulo = QWidget(self.base_titulo)
        self.box_titulo.setObjectName(u"box_titulo")
        self.box_titulo.setMinimumSize(QSize(0, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.box_titulo)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.box_num = QWidget(self.box_titulo)
        self.box_num.setObjectName(u"box_num")
        self.verticalLayout_8 = QVBoxLayout(self.box_num)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_num = QLabel(self.box_num)
        self.label_num.setObjectName(u"label_num")
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(True)
        self.label_num.setFont(font3)
        self.label_num.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_num)


        self.horizontalLayout_4.addWidget(self.box_num)

        self.box_caja = QWidget(self.box_titulo)
        self.box_caja.setObjectName(u"box_caja")
        self.verticalLayout_9 = QVBoxLayout(self.box_caja)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_caja = QLabel(self.box_caja)
        self.label_caja.setObjectName(u"label_caja")
        self.label_caja.setFont(font3)
        self.label_caja.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_caja)


        self.horizontalLayout_4.addWidget(self.box_caja)


        self.verticalLayout_10.addWidget(self.box_titulo)


        self.verticalLayout_6.addWidget(self.base_titulo)

        self.base_nums = QWidget(self.base_turnos)
        self.base_nums.setObjectName(u"base_nums")
        self.horizontalLayout_3 = QHBoxLayout(self.base_nums)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.nums = QWidget(self.base_nums)
        self.nums.setObjectName(u"nums")
        font4 = QFont()
        font4.setPointSize(20)
        self.nums.setFont(font4)
        self.verticalLayout_7 = QVBoxLayout(self.nums)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.box_1 = QWidget(self.nums)
        self.box_1.setObjectName(u"box_1")
        self.horizontalLayout_5 = QHBoxLayout(self.box_1)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.num1 = QLabel(self.box_1)
        self.num1.setObjectName(u"num1")
        self.num1.setFont(font4)
        self.num1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.num1)

        self.caja1 = QLabel(self.box_1)
        self.caja1.setObjectName(u"caja1")
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(False)
        self.caja1.setFont(font5)
        self.caja1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.caja1)


        self.verticalLayout_7.addWidget(self.box_1)

        self.box_2 = QWidget(self.nums)
        self.box_2.setObjectName(u"box_2")
        self.horizontalLayout_6 = QHBoxLayout(self.box_2)
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.num2 = QLabel(self.box_2)
        self.num2.setObjectName(u"num2")
        self.num2.setFont(font4)
        self.num2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.num2)

        self.caja2 = QLabel(self.box_2)
        self.caja2.setObjectName(u"caja2")
        self.caja2.setFont(font4)
        self.caja2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.caja2)


        self.verticalLayout_7.addWidget(self.box_2)

        self.box_3 = QWidget(self.nums)
        self.box_3.setObjectName(u"box_3")
        self.horizontalLayout_7 = QHBoxLayout(self.box_3)
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.num3 = QLabel(self.box_3)
        self.num3.setObjectName(u"num3")
        self.num3.setFont(font4)
        self.num3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.num3)

        self.caja3 = QLabel(self.box_3)
        self.caja3.setObjectName(u"caja3")
        self.caja3.setFont(font4)
        self.caja3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.caja3)


        self.verticalLayout_7.addWidget(self.box_3)

        self.box_4 = QWidget(self.nums)
        self.box_4.setObjectName(u"box_4")
        self.horizontalLayout_8 = QHBoxLayout(self.box_4)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.num4 = QLabel(self.box_4)
        self.num4.setObjectName(u"num4")
        self.num4.setFont(font4)
        self.num4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.num4)

        self.caja4 = QLabel(self.box_4)
        self.caja4.setObjectName(u"caja4")
        self.caja4.setFont(font4)
        self.caja4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.caja4)


        self.verticalLayout_7.addWidget(self.box_4)

        self.box_5 = QWidget(self.nums)
        self.box_5.setObjectName(u"box_5")
        self.horizontalLayout_9 = QHBoxLayout(self.box_5)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.num5 = QLabel(self.box_5)
        self.num5.setObjectName(u"num5")
        self.num5.setFont(font4)
        self.num5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.num5)

        self.caja5 = QLabel(self.box_5)
        self.caja5.setObjectName(u"caja5")
        self.caja5.setFont(font4)
        self.caja5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.caja5)


        self.verticalLayout_7.addWidget(self.box_5)


        self.horizontalLayout_3.addWidget(self.nums)


        self.verticalLayout_6.addWidget(self.base_nums)


        self.verticalLayout_5.addWidget(self.base_turnos)


        self.horizontalLayout_2.addWidget(self.borde_turnos)


        self.horizontalLayout.addWidget(self.widget_6)


        self.verticalLayout_2.addWidget(self.fondo)

        self.borde_bottom = QWidget(self.widget)
        self.borde_bottom.setObjectName(u"borde_bottom")
        sizePolicy.setHeightForWidth(self.borde_bottom.sizePolicy().hasHeightForWidth())
        self.borde_bottom.setSizePolicy(sizePolicy)
        self.borde_bottom.setMinimumSize(QSize(0, 50))
        self.verticalLayout_11 = QVBoxLayout(self.borde_bottom)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.labelDesplazable = QLabel(self.borde_bottom)
        self.labelDesplazable.setObjectName(u"labelDesplazable")
        self.labelDesplazable.setFont(font2)
        self.labelDesplazable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.labelDesplazable)


        self.verticalLayout_2.addWidget(self.borde_bottom)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        
        #Box list BOX:QWidget[num:QLabel,caja:Qlabel]
        self.list_box=[self.box_1,self.box_2,self.box_3,self.box_4,self.box_5]

		#FUNCTIONS
        self.footerBarAnimation()

        #Create footer reset timer
        self.timer1 = QTimer() 

        # self.consultarProximos(self.con) Which connects function "ConsultarProximos"
        self.timer1.timeout.connect(lambda: self.footerBarAnimation()) 
        self.timer1.start(10000)

        #Show new
        self.timer2 = QTimer()
        self.timer2.timeout.connect(lambda: self.showNew())
        self.timer2.start(2000)
        
        #QTimer.singleShot(5000, lambda: self.showNew(1,1))
        #QTimer.singleShot(11000, lambda: self.showNew(1,1))


        self.refreshTime()
        self.refreshWeather()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Buenos Aires, La Plata", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"22:30", None))
        self.temp.setText(QCoreApplication.translate("MainWindow", u"32`C", None))
        self.titulo_llamado.setText(QCoreApplication.translate("MainWindow", u"LLAMADO TURNOS", None))
        self.label_num.setText(QCoreApplication.translate("MainWindow", u"NUM", None))
        self.label_caja.setText(QCoreApplication.translate("MainWindow", u"CAJA", None))
        self.num1.setText(QCoreApplication.translate("MainWindow", u"B3", None))
        self.caja1.setText(QCoreApplication.translate("MainWindow", u"BOX 1", None))
        self.num2.setText(QCoreApplication.translate("MainWindow", u"B2", None))
        self.caja2.setText(QCoreApplication.translate("MainWindow", u"BOX 1", None))
        self.num3.setText(QCoreApplication.translate("MainWindow", u"B1", None))
        self.caja3.setText(QCoreApplication.translate("MainWindow", u"BOX 1", None))
        self.num4.setText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.caja4.setText(QCoreApplication.translate("MainWindow", u"BOX 1", None))
        self.num5.setText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.caja5.setText(QCoreApplication.translate("MainWindow", u"BOX 1", None))
        self.labelDesplazable.setText(QCoreApplication.translate("MainWindow", u"LABEL DESPLAZABLE", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vent=QMainWindow()
    ui= Pantalla()
    ui.setupUi(vent)
    vent.show()
    sys.exit(app.exec())

