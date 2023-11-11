import datetime
import logging
import shutil

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtMultimedia import *
from PySide6.QtMultimediaWidgets import *


#This import generates a parallel subprocess
import manejar_datos
import subprocess
from connection import Connection

import resources_rc
import sys


from multiprocessing import Process

import requests

class Pantalla(object):
    def resetAdvice(self):
        QUERY='''BEGIN TRANSACTION;
        -- Eliminar aviso
        DELETE  FROM advice
        COMMIT TRANSACTION;'''
        self.db_handler.queryExecution(QUERY)

    def adjustWindow(self,ventana:QMainWindow):    
        screen = QGuiApplication.primaryScreen().availableGeometry()
        #print(f' screen: {screen.width()}  {screen.height()}')
        
        print(f'{screen.width()}  H{screen.height()}')
        #print(f' widget: {widget.width()}  {widget.height()}')

        #x = screen.width() - widget.width()
        #y = screen.height() - widget.height()

        #print(f' X: {x} Y: {y}')
        ventana.move(0, screen.height())

    #f to delete layout widget

    def deleteItemsOfLayout(self,layout:QVBoxLayout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())

    def refreshBoxList(self):
        #This method actualizes the box list order to the actual
        #Last to the first
        ultimo = self.list_box[4]
        for i in range(4,0,-1):
            self.list_box[i] = self.list_box[i-1]
        self.list_box[0] = ultimo


    def createLayout(self,layout:QVBoxLayout):
        for elem in self.list_box:
            elem.setParent(self.nums)
            layout.addWidget(elem)
        

    def showNew(self):

        #Check if need to advice
        self.checkAdvice()

        #if exists a call request
        if self.checkNext():

            #actualize the list of widgets (0,1,2,3,4) to (4,0,1,2,3) 
            self.refreshBoxList()

            #Get the childs of the FIRST Box QWidget [QHLayout,Qlabel(num),QLabel(caja)]
            childs= self.list_box[0].children()

            #Save num and caja labels
            num:QLabel = childs[1]
            caja:QLabel = childs[2]

            #Put info in labels
            num.setText(f'{self.next_type} {str(self.next_number)}')
            caja.setText(f'BOX {str(self.caller_box)}')

            #delete actual layout
            self.deleteItemsOfLayout(self.verticalLayout_7)

            #Create ordered layout
            self.createLayout(self.verticalLayout_7)

            #Execute color animation on the FIRST box
            self.boxAnimation(self.list_box[0])

    def checkAdvice(self):
        advice_query= \
        '''BEGIN TRANSACTION;

        DECLARE @advice_num INT;

        -- Obtener el proximo turno disponible
        SELECT TOP (1) @advice_num=num FROM advice ORDER BY num        
        
        -- Eliminar aviso
        DELETE  FROM advice WHERE num=@advice_num

        SELECT @advice_num

        COMMIT TRANSACTION;
        '''


        if (self.db_handler.queryExecution(advice_query)):  
            query= self.db_handler.getQuery()       
            query.first()
            last_num= query.value(0) #Save the num to look
            print(f'Encontre el num {last_num}')
            if not(query.isNull(0)):
                self.lookForTheNum(last_num)

    #This method searchs in the boxes for the num to advice
    def lookForTheNum(self,last_num):
        for elem in self.list_box:
            childs= elem.children() #Get childs of QWidget
            num:QLabel = childs[1] #Get label
            text:str= num.text()
            if text.__contains__(str(last_num)):
                self.boxAnimation(elem)



    def videoCheck(self):
        NEW_VIDEO_QUERY= \
        '''BEGIN TRANSACTION;

        DECLARE @video_num varchar;

        -- Obtener el proximo turno disponible
        SELECT TOP (1) @video_num=ipnum FROM video ORDER BY ipnum        
        
        -- Eliminar aviso
        DELETE  FROM video

        SELECT @video_num

        COMMIT TRANSACTION;
        '''

        if (self.db_handler.queryExecution(NEW_VIDEO_QUERY)):  #If query ok
            query= self.db_handler.getQuery()       #Get query
            query.first()  #Get first row
            if not(query.isNull(0)): #If num <> null

                #Log video changes
                logging.info(f'Video Change, time:{datetime.datetime.now()}')

                #Restart video
                self.restartVideo() 





    @Slot()
    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    def restartVideo(self):

        print('vid restart begins')
        #Stop the player
        self._ensure_stopped()

        #Get the path #f'''\\\\{json_file['IP']}\\Ticketera\\Videos\\
        server_folder_path= f'{manejar_datos.getVideoPath()}NewVideo.mp4'

        #Local video path
        folder_local='C:\\Ticketera\\Videos\\VideoHospital.mp4'

        try:
        # Replace local file with the server file
            shutil.copy(server_folder_path, folder_local)
            print("Archivo reemplazado exitosamente.")
        except FileNotFoundError:
            print("El archivo original no se encuentra o el directorio de destino no existe.")
        except PermissionError:
            print("Permiso denegado para copiar el archivo en el directorio de destino.")

        #Create the link
        url= QUrl.fromLocalFile(folder_local)

        #Reload file to the media player
        self._player.setSource(url)

        #Play      
        QTimer.singleShot(4000,lambda:self._player.play())
        
        QTimer.singleShot(4000,lambda:print('VIDEO STARTED'))

    def initializeVideo(self):

        #Create a playlist
        self._playlist = []  # FIXME 6.3: Replace by QMediaPlaylist?

        self._playlist_index = -1

        #Create audio output
        self._audio_output = QAudioOutput()

        #Create a media player
        self._player = QMediaPlayer()

        #Set the audio output to player
        self._player.setAudioOutput(self._audio_output)

        #Create layout and add the videoW
        self.layout_video = QVBoxLayout(self.video_widget)

        #Create the widget
        self._video_widget = QVideoWidget()
        videoPolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        videoPolicy.setHorizontalStretch(0)
        videoPolicy.setVerticalStretch(0)
        videoPolicy.setHeightForWidth(self._video_widget.sizePolicy().hasHeightForWidth())
        self._video_widget.setSizePolicy(videoPolicy)

        #self._video_widget.setMinimumSize(QSize(ancho, altura))
        self._video_widget.setMaximumSize(QSize(1024, 768))
        self._video_widget.setAspectRatioMode(Qt.AspectRatioMode.IgnoreAspectRatio)

        #Add w to layout
        self.layout_video.addWidget(self._video_widget)

        #Set the video output of the QMediaPlayer-> QVideoWidget
        self._player.setVideoOutput(self._video_widget)

        #Generate the path to the video //GET OF A JSON
        url = QUrl.fromLocalFile(f'{manejar_datos.getVideoPath()}VideoHospital.mp4')
        print(url)
        #Add to playlist
        self._playlist.append(url)
        self._playlist_index = len(self._playlist) - 1

        #Set the source with the QUrl to the Player
        self._player.setSource(url)

        #Play
        self._player.play()

    def checkNext(self): #exececute a query of bring on the last num called by BOX and actualize displa
          
        #Query to get the new num
        data_query= \
        '''BEGIN TRANSACTION;
        DECLARE @proximo_turno INT;
        DECLARE @caja_llamadora INT;
        DECLARE @proximo_tipo INT;

        -- Obtener el proximo turno disponible
        SELECT TOP (1) @proximo_turno=num, @caja_llamadora=atiende_caja, @proximo_tipo=tipo 
        FROM turnos_actual 
        WHERE (status=2) 
        ORDER BY num        
        
        SELECT @proximo_turno, @caja_llamadora, @proximo_tipo

        UPDATE turnos_actual SET status = 3 WHERE num=@proximo_turno

        COMMIT TRANSACTION;
        '''
        #Create a query to get the next display
        query= QSqlQuery(self.db)   #SELF.db is the connection QSqlDatabase already created
        query.prepare(data_query) #Query brings on the next

        if (query.exec()): #If query succeeds (GET THE NEXT NUMBER)         
            query.first()   #Get the first row

            if not(query.isNull(0)): #If value is not null
                self.next_number = query.value(0)  #Save first value to put in screen
                self.caller_box = query.value(1) #Save caller num

                if (query.value(2)== 1): #Save CON TURNO or SIN TURNO
                    self.next_type = 'ST'
                else: 
                    self.next_type = 'CT'   

                return True
            return False
        
    def refreshTime(self):
        #Get the actual time in HH:MM
        time_now=datetime.datetime.now().strftime('%H:%M')

        #Put the time in the label
        self.time_label.setText(time_now)


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

        #Get the icon
        iconcode=data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/w/{iconcode}.png"


        # Descargar la imagen desde la URL
        response = requests.get(icon_url)
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.temp_icon.setPixmap(pixmap)
            self.temp_icon.setScaledContents(False)
            self.temp_icon.setAlignment(Qt.AlignTop | Qt.AlignRight)


        #Save the temp data of the json (In kelvin)
        temp=data['main']['temp']

        #Pass Kelvin to Celsius
        tempC:float=temp-273.15
        self.temp_label.setText(f'{tempC.__round__()}°C')


   
        
    def boxAnimation(self, elem:QWidget):
        
        #MP3 Path
        path='./soundplayer.py'
        subprocess.Popen(['python', path])

        #Change the color between blue and white
        #blue	background-color: rgb(4, 42, 79);color:white;
        #white 	background-color: rgb(204, 204, 204); color:rgb(4, 42, 79);
        elem.setStyleSheet(u"QLabel{background-color: rgb(4, 42, 79);color:white;border-radius:2px;}")
        
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


    def footerBarAnimation(self):
        print('footer starts')
        self.animation = QPropertyAnimation(self.labelDesplazable,b'geometry')
        self.animation.setDuration(11000)

        self.labelDesplazable.setGeometry(-800, 9, 800, 44) #Initial Position
        rect = self.labelDesplazable.geometry() #Get the geometry
        self.animation.setStartValue(rect) #Set the geometry animation value
        transpose=self.ventana.geometry().width() + 1800
        print(transpose)
        rect.translate(transpose,0) #Transpose X to right
        self.animation.setEndValue(rect) #Set the end geo value
        self.animation.start()  #Start


    def setupUi(self, MainWindow):
        self.ventana:QMainWindow= MainWindow
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1067, 686)
        MainWindow.setStyleSheet(u"#borde_top {\n"
"	background-color: qlineargradient(spread:pad, x1:0.977, y1:0.636409, x2:0.125, y2:0.636636, stop:0 rgba(4, 42, 79,255), stop:1 rgba(0, 73, 113,255));\n"
"	border-radius:2px;\n"
"}\n"
"#borde_top QLabel{\n"
"	color:white;\n"
"}\n"
"\n"
"#widget{\n"
"	background-image: url(:/img/img/grisSinFondo.jpg);\n"
"}\n"
"\n"
"#borde_video{\n"
"	border-image: url(:/img/img/fondo_sin.jpg);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"\n"
"#titulo_llamado{\n"
"	background-color: rgb(4, 42, 79);\n"
"	color:white;\n"
"	border-radius:2px;\n"
"}\n"
"#borde_turnos{\n"
"	border-radius:10px;\n"
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
"	background-color: rgb(4, 42, 79);\n"
"	color:white;\n"
"}\n"
"#borde_bottom QLabel{\n"
"	background-color: rgb(4, 42, 79);\n"
""
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
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 80)
        self.base_fondoVideo = QWidget(self.widget_5)
        self.base_fondoVideo.setObjectName(u"base_fondoVideo")
        self.verticalLayout_4 = QVBoxLayout(self.base_fondoVideo)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(30, 40, 0, 20)
        self.base_hora = QWidget(self.base_fondoVideo)
        self.base_hora.setObjectName(u"base_hora")
        self.base_hora.setMinimumSize(QSize(0, 60))
        self.base_hora.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_13 = QVBoxLayout(self.base_hora)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.borde_top = QWidget(self.base_hora)
        self.borde_top.setObjectName(u"borde_top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.borde_top.sizePolicy().hasHeightForWidth())
        self.borde_top.setSizePolicy(sizePolicy1)
        self.borde_top.setMinimumSize(QSize(300, 60))
        self.borde_top.setMaximumSize(QSize(700, 60))
        self.horizontalLayout_11 = QHBoxLayout(self.borde_top)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 0, 10, 0)
        self.widget_2 = QWidget(self.borde_top)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.city_label = QLabel(self.widget_2)
        self.city_label.setObjectName(u"city_label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.city_label.setFont(font)
        self.city_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.city_label)


        self.horizontalLayout_11.addWidget(self.widget_2, 0, Qt.AlignVCenter)

        self.widget_4 = QWidget(self.borde_top)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, 10, -1)
        self.temp_icon = QLabel(self.widget_4)
        self.temp_icon.setObjectName(u"temp_icon")
        self.temp_icon.setStyleSheet(u"border-image:url(https://openweathermap.org/img/w/02n.png);")
        self.temp_icon.setPixmap(QPixmap(u":/img/img/icons8-people-64.png"))
        self.temp_icon.setScaledContents(False)
        self.temp_icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.temp_icon.setMargin(5)

        self.horizontalLayout_10.addWidget(self.temp_icon, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.temp_label = QLabel(self.widget_4)
        self.temp_label.setObjectName(u"temp_label")
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.temp_label.setFont(font1)
        self.temp_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.temp_label, 0, Qt.AlignHCenter)


        self.horizontalLayout_11.addWidget(self.widget_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_3 = QWidget(self.borde_top)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.widget_3.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 9, 20, 9)
        self.time_label = QLabel(self.widget_3)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setFont(font1)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.time_label)

        self.hs = QLabel(self.widget_3)
        self.hs.setObjectName(u"hs")
        self.hs.setFont(font)

        self.horizontalLayout_13.addWidget(self.hs, 0, Qt.AlignVCenter)


        self.horizontalLayout_11.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.borde_top)


        self.verticalLayout_4.addWidget(self.base_hora)

        self.borde_video = QWidget(self.base_fondoVideo)
        self.borde_video.setObjectName(u"borde_video")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.borde_video.sizePolicy().hasHeightForWidth())
        self.borde_video.setSizePolicy(sizePolicy3)
        self.borde_video.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.borde_video)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.video_widget = QWidget(self.borde_video)
        self.video_widget.setObjectName(u"video_widget")
        self.video_widget.setMinimumSize(QSize(300, 300))

        self.verticalLayout_14.addWidget(self.video_widget)


        self.verticalLayout_4.addWidget(self.borde_video)


        self.verticalLayout_3.addWidget(self.base_fondoVideo)


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
        font2.setPointSize(30)
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
        font3.setPointSize(45)
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
        font5 = QFont()
        font5.setPointSize(36)
        font5.setBold(True)
        self.num1.setFont(font5)
        self.num1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.num1)

        self.caja1 = QLabel(self.box_1)
        self.caja1.setObjectName(u"caja1")
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
        self.num2.setFont(font5)
        self.num2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.num2)

        self.caja2 = QLabel(self.box_2)
        self.caja2.setObjectName(u"caja2")
        self.caja2.setFont(font5)
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
        self.num3.setFont(font5)
        self.num3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.num3)

        self.caja3 = QLabel(self.box_3)
        self.caja3.setObjectName(u"caja3")
        self.caja3.setFont(font5)
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
        self.num4.setFont(font5)
        self.num4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.num4)

        self.caja4 = QLabel(self.box_4)
        self.caja4.setObjectName(u"caja4")
        self.caja4.setFont(font5)
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
        self.num5.setFont(font5)
        self.num5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.num5)

        self.caja5 = QLabel(self.box_5)
        self.caja5.setObjectName(u"caja5")
        self.caja5.setFont(font5)
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
        self.borde_bottom.setMinimumSize(QSize(0, 60))
        self.verticalLayout_11 = QVBoxLayout(self.borde_bottom)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.labelDesplazable = QLabel(self.borde_bottom)
        self.labelDesplazable.setObjectName(u"labelDesplazable")
        self.labelDesplazable.setFont(font1)
        self.labelDesplazable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.labelDesplazable, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.borde_bottom)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        #DB
        self.db_handler= Connection()
        self.db=self.db_handler.createConnection()

        #Box list BOX:QWidget[num:QLabel,caja:Qlabel]
        self.list_box=[self.box_1,self.box_2,self.box_3,self.box_4,self.box_5]

		#FUNCTIONS
        self.resetAdvice()
        self.footerBarAnimation() #Init footer
        self.refreshTime() #Init time
        self.refreshWeather() #Init weather

        #Show new number and advice
        self.timerNum = QTimer()
        self.timerNum.timeout.connect(lambda: self.showNew())
        self.timerNum.start(4000)
        
        #f to refresh time
        self.timerWeather = QTimer()
        self.timerWeather.timeout.connect(lambda: self.refreshTime())
        self.timerWeather.start(30000)
        
        #f to refresh weather
        self.timerWeather = QTimer()
        self.timerWeather.timeout.connect(lambda: self.refreshWeather())
        self.timerWeather.start(1800000)
        

        #timer to reset video 15s
        self.timerVideoReset = QTimer()
        self.timerVideoReset.timeout.connect(lambda: self.videoCheck())
        self.timerVideoReset.start(10000)

        #f to initalizate videoPlayer and stream
        self.initializeVideo()

        #f to fit fullscreen
        self.adjustWindow(MainWindow)

        #if footer ends self.footerBarAnimation()
        self.animation.finished.connect(lambda: self.animation.start())
        
        #if video finishes, restart
        self._player.mediaStatusChanged.connect(lambda: self._player.play())
        self._player.setAudioOutput(None)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.city_label.setText(QCoreApplication.translate("MainWindow", u"Buenos Aires, La Plata", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"22:30", None))
        self.hs.setText(QCoreApplication.translate("MainWindow", u"HS", None))
        self.temp_label.setText(QCoreApplication.translate("MainWindow", u"32`C", None))
        self.titulo_llamado.setText(QCoreApplication.translate("MainWindow", u"LLAMADO TURNOS", None))
        self.label_num.setText(QCoreApplication.translate("MainWindow", u"NUM", None))
        self.label_caja.setText(QCoreApplication.translate("MainWindow", u"CAJA", None))
        self.labelDesplazable.setText(QCoreApplication.translate("MainWindow", u"HOSPITAL PRIVADO SUDAMERICANO", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vent=QMainWindow()
    ui= Pantalla()
    ui.setupUi(vent)

    rect= vent.geometry()
    vent.setFixedSize(rect.width(),rect.height())
    vent.showFullScreen()
    sys.exit(app.exec())
