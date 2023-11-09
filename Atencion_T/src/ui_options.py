import os
import shutil
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel
from PySide6.QtMultimedia import (QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget
from connection import Connection
import fondos_rc
import datetime
import manejar_datos
import logger_config
import logging
from ui_popWarning import PopWarning
from ui_publicity import Publicity

AVI = "video/x-msvideo"  # AVI
MP4 = 'video/mp4'

def get_supported_mime_types():
    result = []
    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    return result

class SettingsWindow(object): 

    def showPublicity(self):
        self.ui_pub= Publicity()
        self.pop_publicity= QMainWindow()
        self.ui_pub.setupUi(self.pop_publicity) #Paso la ventana para configuraciones
        self.pop_publicity.setWindowFlags(Qt.FramelessWindowHint)   #Not show windows bar
        self.pop_publicity.setAttribute(Qt.WA_TranslucentBackground) #set translucent background
        self.pop_publicity.show() #Show
        QTimer.singleShot(6000, lambda: self.pop_publicity.close())

    def verHistorial(self):
        QUERY=f'''SELECT [dni],[hora],[tipo],[atiende_usuario]\n
                FROM [turnos].[dbo].[turnos_actual]'''


        #Rows=0
        self.tableWidget.setRowCount(0)
        if self.db.queryExecution(QUERY): #If query executes ok

            #Get the query
            query_data:QSqlQuery= self.db.getQuery()   

            #The nums width is 15px
            self.tableWidget.setColumnWidth(1,85) #Set [col dni],width

            while query_data.next(): #each query row
                
                rows=self.tableWidget.rowCount() #gets the actual row count
                self.tableWidget.setRowCount(rows+1) #add a row

                item_dni= QTableWidgetItem(str(query_data.value(0))) #Create a table widget item
                item_dni.setTextAlignment(Qt.AlignmentFlag.AlignCenter) #Set the align with flag
                self.tableWidget.setItem(rows, 0, item_dni) #Insert the item

                #query gets a QDate item, which uses .toString(time format)
                item_hora= QTableWidgetItem(query_data.value(1).toString('HH:mm')) #Create a table widget item
                item_hora.setTextAlignment(Qt.AlignmentFlag.AlignCenter) #Set the align with flag
                self.tableWidget.setItem(rows, 1, item_hora) #Insert the item

                item_tipo= QTableWidgetItem(str(query_data.value(2))) #Create a table widget item
                item_tipo.setTextAlignment(Qt.AlignmentFlag.AlignCenter) #Set the align with flag
                self.tableWidget.setItem(rows, 2, item_tipo) #Insert the item

                item_atiende= QTableWidgetItem(str(query_data.value(3))) #Create a table widget item
                item_atiende.setTextAlignment(Qt.AlignmentFlag.AlignCenter) #Set the align with flag
                self.tableWidget.setItem(rows, 3, item_atiende) #Insert the item
        else:
            self.popAdvice('Error en la conexion\n con la base de datos') #User error, show advice

        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)



    def get_first_file_path(self, path):
        first_file_path = None
        for root, dirs, files in os.walk(path):
            if len(files) > 0:
                first_file_path = os.path.join(root, files[0])
                break
        return first_file_path
    
    def selectActualVideo(self):

        file_dialog = QFileDialog()
        self._mime_types= []

        is_windows = sys.platform == 'win32'
        if not self._mime_types:
            self._mime_types = get_supported_mime_types()
            if (is_windows and AVI not in self._mime_types):
                self._mime_types.append(AVI)
            elif MP4 not in self._mime_types:
                self._mime_types.append(MP4)

        file_dialog.setMimeTypeFilters(self._mime_types)

        default_mimetype = AVI if is_windows else MP4
        if default_mimetype in self._mime_types:
            file_dialog.selectMimeTypeFilter(default_mimetype)

        movies_location = QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_location)
        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
                  
      
        path_video = url.path() # Path of the selected file
        path_video= path_video[1:] # Take off the first bar
        origen= path_video.replace(r'/','\\') # Modify the final path to generate the full path of the new file
        
        VIDEO_WRITE_QUERY=f'''
        BEGIN TRANSACTION;
        INSERT INTO [turnos].[dbo].[video](ipnum,dir) VALUES('server ip','{origen}');
        COMMIT TRANSACTION; 
        '''
        # Get server Path
        server_folder_path = manejar_datos.getVideoPath()  
        
        try:
        # Replace local file in shared

            shutil.copy(origen, os.path.join(server_folder_path, 'NewVideo.mp4'))

            #Write in the DB the flag of a new video
            self.db.queryExecution(VIDEO_WRITE_QUERY)

            print("Archivo reemplazado exitosamente.")
        except FileNotFoundError:
            print("El archivo original no se encuentra o el directorio de destino no existe.")
        except PermissionError:
            print("Permiso denegado para copiar el archivo en el directorio de destino.")

        logging.info(f'Copied the video from{origen} to {server_folder_path} ')


    def resetTurnos(self):
        query_reset=f'''
        BEGIN TRANSACTION;
        INSERT INTO historial_turnos(dni,hora,tipo,atiende_usuario) 
        SELECT a.dni,a.hora,a.tipo,a.atiende_usuario FROM turnos_actual a;
        DELETE FROM turnos_actual;
        COMMIT TRANSACTION;
        '''

        if (self.db.queryExecution(query_reset)):
            self.popAdvice('Se ha limpiado los turnos \n actuales satisfactoriamente')
        else:
            self.popAdvice('Error en la limpieza de turnos')

    def popAdvice(self,text):  #Create a window of advice
        self.pop= QMainWindow()
        self.ui= PopWarning()
        self.ui.setupUi(self.pop,text) #Paso la ventana para configuraciones
        self.pop.setWindowFlags(Qt.FramelessWindowHint)   #Not show windows bar
        self.pop.setAttribute(Qt.WA_TranslucentBackground) #set translucent background
        self.pop.show() #Show
        QTimer.singleShot(3000, lambda: self.pop.close())    

    def setupUi(self, MainWindow, dataBase):

        self.window= MainWindow

        self.db = dataBase #Get the dataBase from start

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(576, 424)
        MainWindow.setStyleSheet(u"#fondo{\n"
"border-image: url(:/fondos/img/fondos/fondo_sin.jpg);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius:5px;\n"
"	border: 1px solid rgba(255, 255, 255, 130);\n"
"	background-color: rgba(255, 255, 255, 130);\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgba(66, 66, 66, 150);\n"
"	border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QLabel{\n"
"color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fondo = QWidget(self.centralwidget)
        self.fondo.setObjectName(u"fondo")
        self.horizontalLayout = QHBoxLayout(self.fondo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.fondo)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 20, -1, 40)
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_5)

        self.tableWidget = QTableWidget(self.widget_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_8.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.fondo)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(92, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cont1 = QWidget(self.frame)
        self.cont1.setObjectName(u"cont1")
        self.cont1.setMinimumSize(QSize(92, 81))
        self.verticalLayout_4 = QVBoxLayout(self.cont1)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.video_selector = QPushButton(self.cont1)
        self.video_selector.setObjectName(u"video_selector")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_selector.sizePolicy().hasHeightForWidth())
        self.video_selector.setSizePolicy(sizePolicy)
        self.video_selector.setMinimumSize(QSize(60, 60))
        self.video_selector.setMaximumSize(QSize(60, 60))
        icon = QIcon()
        icon.addFile(u":/iconosWhite/img/iconsAtencion/play-3-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.video_selector.setIcon(icon)
        self.video_selector.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.video_selector, 0, Qt.AlignHCenter)

        self.label = QLabel(self.cont1)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.cont1)

        self.cont2 = QWidget(self.frame)
        self.cont2.setObjectName(u"cont2")
        self.cont2.setMinimumSize(QSize(92, 81))
        self.verticalLayout_5 = QVBoxLayout(self.cont2)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 5)
        self.reset_turnos = QPushButton(self.cont2)
        self.reset_turnos.setObjectName(u"reset_turnos")
        sizePolicy.setHeightForWidth(self.reset_turnos.sizePolicy().hasHeightForWidth())
        self.reset_turnos.setSizePolicy(sizePolicy)
        self.reset_turnos.setMinimumSize(QSize(60, 60))
        self.reset_turnos.setMaximumSize(QSize(60, 60))
        icon1 = QIcon()
        icon1.addFile(u":/iconosWhite/img/iconsAtencion/undo-5-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reset_turnos.setIcon(icon1)
        self.reset_turnos.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.reset_turnos, 0, Qt.AlignHCenter)

        self.labelTurnos = QLabel(self.cont2)
        self.labelTurnos.setObjectName(u"labelTurnos")
        self.labelTurnos.setFont(font1)
        self.labelTurnos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelTurnos)


        self.verticalLayout_2.addWidget(self.cont2, 0, Qt.AlignVCenter)

        self.cont3 = QWidget(self.frame)
        self.cont3.setObjectName(u"cont3")
        self.cont3.setMinimumSize(QSize(92, 81))
        self.verticalLayout_6 = QVBoxLayout(self.cont3)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.ver_historial = QPushButton(self.cont3)
        self.ver_historial.setObjectName(u"ver_historial")
        sizePolicy.setHeightForWidth(self.ver_historial.sizePolicy().hasHeightForWidth())
        self.ver_historial.setSizePolicy(sizePolicy)
        self.ver_historial.setMinimumSize(QSize(60, 60))
        self.ver_historial.setMaximumSize(QSize(60, 60))
        icon2 = QIcon()
        icon2.addFile(u":/iconosWhite/img/iconsAtencion/search-2-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ver_historial.setIcon(icon2)
        self.ver_historial.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.ver_historial, 0, Qt.AlignHCenter)

        self.labelHistorial = QLabel(self.cont3)
        self.labelHistorial.setObjectName(u"labelHistorial")
        self.labelHistorial.setFont(font1)
        self.labelHistorial.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.labelHistorial)


        self.verticalLayout_2.addWidget(self.cont3)

        self.cont4 = QWidget(self.frame)
        self.cont4.setObjectName(u"cont4")
        self.cont4.setMinimumSize(QSize(92, 81))
        self.verticalLayout_7 = QVBoxLayout(self.cont4)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 5, 0, 5)
        self.info = QPushButton(self.cont4)
        self.info.setObjectName(u"info")
        self.info.setMinimumSize(QSize(60, 60))
        self.info.setMaximumSize(QSize(60, 60))
        icon3 = QIcon()
        icon3.addFile(u":/iconosWhite/img/iconsAtencion/info-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info.setIcon(icon3)
        self.info.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.info, 0, Qt.AlignHCenter)

        self.labelInfo = QLabel(self.cont4)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setFont(font1)
        self.labelInfo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.labelInfo)


        self.verticalLayout_2.addWidget(self.cont4)


        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.fondo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        #INITIAL WINDOW CONFIG

        #Create DB
        self.db = Connection()
        #Set title
        self.window.setWindowTitle('Menu opciones') #Win title
        
        #Get the actual path
        scriptDir = os.path.dirname(os.path.realpath(__file__))

        #Set the Window icon
        self.window.setWindowIcon(QIcon(scriptDir + os.path.sep + 'logoBlack.png'))
        #self.ventana.setWindowFlags(Qt.FramelessWindowHint)   #Not show windows bar
        #self.ventana.setAttribute(Qt.WA_TranslucentBackground) #set translucent background

        #TABLE CONFS
        self.tableWidget.setColumnWidth(2,120) #Set [col dni],width
        self.tableWidget.setColumnWidth(3,120) #Set [col atiende],width

        #EVENTS
        self.ver_historial.clicked.connect(lambda: self.verHistorial())
        self.video_selector.clicked.connect(lambda: self.selectActualVideo())
        self.reset_turnos.clicked.connect(lambda: self.resetTurnos())
        self.info.clicked.connect(lambda:self.showPublicity())

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"VISOR TURNOS", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"DNI", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Atiende", None));
        self.video_selector.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SELECCION\n"
" VIDEO", None))
        self.reset_turnos.setText("")
        self.labelTurnos.setText(QCoreApplication.translate("MainWindow", u"RESET\n"
"TURNOS", None))
        self.ver_historial.setText("")
        self.labelHistorial.setText(QCoreApplication.translate("MainWindow", u"VER\n"
" HISTORIAL", None))
        self.info.setText("")
        self.labelInfo.setText(QCoreApplication.translate("MainWindow", u"INFO", None))
    # retranslateUi

if __name__ == "__main__":
    db=''
    app = QApplication(sys.argv)
    vent=QMainWindow()
    login= SettingsWindow() #Creo la ventana login
    login.setupUi(vent,db) #Paso la ventana para configuraciones
    vent.show() #Show
    sys.exit(app.exec())
