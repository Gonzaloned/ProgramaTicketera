
import datetime
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PyQt6.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel
from connection import Connection
import pantalla1_rc
from ui_pop import Pop
import logger_config
import logging

#Subprocess to run node printer file
import subprocess

class Pantalla3(object):
 

    def animateOn(self, win: QMainWindow):
        self.eff = QGraphicsOpacityEffect(win)
        self.eff.setOpacity(0.3)
        win.setGraphicsEffect(self.eff)

        self.anim = QPropertyAnimation(self.eff, b"opacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(0.2)
        self.anim.setEndValue(1)
        self.anim.start()

    def solicitarAtencion(self,tipo):

        #Get the time now() => time_now.strftime('%Y-%m-%d %H:%M:%S')
        time_now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.000')
        
        if tipo==1:
            contador_tipo='contador_tipo_CT'
        if tipo==2:
            contador_tipo='contador_tipo_ST'
        #Query
        QUERY= f'''BEGIN TRANSACTION;

        --Creo variable para guardar siguiente indice
        DECLARE @SiguienteIndice INT;
        
        -- Guardo el siguiente indice del tipo (MAXINDICETIPO+1)
        SELECT @SiguienteIndice=COALESCE(MAX({contador_tipo}), 0) + 1 FROM turnos_actual;

        -- Insertar un nuevo turno a ser llamado
        INSERT INTO turnos_actual(dni,hora,tipo,status,{contador_tipo}) VALUES({self.dni},'{time_now}',{tipo},1,@SiguienteIndice);

        -- Recuperar el ultimo num insertado
        SELECT @SiguienteIndice;

        COMMIT TRANSACTION;
        '''

        #Execute the query
        if (self.db.queryExecution(QUERY)):
            #Get the executed query
            query_data= self.db.getQuery()       
            if(query_data.first()):

                #Save the added num to print the ticket
                numero_agregado:float=query_data.value(0)

                    # Ejecuta el script de Node.js desde Python
                printer_file= r'.\ticketera.js'

                #Parameters list to call NodePrinter
                param_list=[]
                
                #Add num to Ticket params
                param_list.append(str(round(numero_agregado)))

                try:
                    subprocess.Popen(['node', printer_file, *param_list], creationflags=subprocess.CREATE_NO_WINDOW)
                    print("Script de Node.js ejecutado con éxito desde Python.")
                except subprocess.CalledProcessError as e:
                    logging.error(e)
                    print("Error al ejecutar el script de Node.js:", e)
                except FileNotFoundError:
                    logging.error("File not found")
                    print("File not found")
            else:
                logging.error("the num has not been loaded")
                print('hubo error')
                

            #Abro nueva ventana
            self.pop_window = QMainWindow()
            
            #Creo template y seteo el estilo en ventana
            self.pop = Pop()
            self.pop.setupUi(self.pop_window)

            #No frame, no background, show
            self.pop_window.setWindowFlags(Qt.FramelessWindowHint)
            self.pop_window.setAttribute(Qt.WA_TranslucentBackground)

            #Set the pop window main and the others -NO clickeable- until the pop closes
            self.pop_window.setWindowModality(Qt.ApplicationModal)

            #Show pop with the opening animation
            self.pop_window.show()
            self.animateOn(self.pop_window)

            QTimer.singleShot(7000, lambda: self.closeAll())

    def closeAll(self):
        self.window3.close()
        self.pop_window.close()
    
        
    def setupUi(self, base:QMainWindow, dni, database:Connection):
        self.db= database
        self.dni = dni
        self.window3= base
        if not base.objectName():
            base.setObjectName(u"base")
        base.resize(1433, 817)
        base.setStyleSheet(u"#centralwidget{\n"
"	background-image: url(:/imagenes/img/fondo.jpg);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius:15px;\n"
"  	border-style: solid;\n"
"    border-width: 1.5px;\n"
"	color: rgb(0, 73, 113);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#center{\n"
"	border-image: url(:/imagenes/img/fondo_sin.jpg);\n"
"	border-radius: 40px;\n"
"}\n"
"\n"
"#btn1{\n"
"	color: rgba(0, 73, 113, 220);\n"
"	border-color: rgba(0, 73, 113,30);\n"
"}\n"
"\n"
"#btn2{\n"
"	color: rgba(157, 19, 45,220);\n"
"	\n"
"	border-color: rgba(95, 12, 28, 30);\n"
"}\n"
"\n"
"#btn1:pressed{\n"
"	background-color: rgb(223, 223, 223);\n"
"	color: rgba(0, 73, 113, 240);\n"
"  	border-style: solid;\n"
"    border-width: 4px;\n"
"	border-color: rgba(0, 73, 113,20);\n"
"}\n"
"\n"
"#btn2:pressed{\n"
"	background-color: rgb(223, 223, 223);\n"
"	color: rgba(157, 19, 45,240);\n"
"  	border-style: solid;\n"
"    border-width: 4px;\n"
"	border-color: rgba(95, 12, 28, 20);\n"
"\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(base)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(60)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 100, -1, -1)
        self.center = QWidget(self.widget)
        self.center.setObjectName(u"center")
        self.center.setMinimumSize(QSize(900, 500))
        self.horizontalLayout = QHBoxLayout(self.center)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cont1 = QWidget(self.center)
        self.cont1.setObjectName(u"cont1")
        self.verticalLayout_3 = QVBoxLayout(self.cont1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn1 = QPushButton(self.cont1)
        self.btn1.setObjectName(u"btn1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setMinimumSize(QSize(280, 280))
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.btn1.setFont(font)

        self.verticalLayout_3.addWidget(self.btn1, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.cont1)

        self.cont2 = QWidget(self.center)
        self.cont2.setObjectName(u"cont2")
        self.horizontalLayout_3 = QHBoxLayout(self.cont2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn2 = QPushButton(self.cont2)
        self.btn2.setObjectName(u"btn2")
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setMinimumSize(QSize(280, 280))
        self.btn2.setFont(font)

        self.horizontalLayout_3.addWidget(self.btn2)


        self.horizontalLayout.addWidget(self.cont2)


        self.horizontalLayout_2.addWidget(self.center, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.widget)

        base.setCentralWidget(self.centralwidget)

        self.retranslateUi(base)

        QMetaObject.connectSlotsByName(base)

        #Defining events
        self.btn1.clicked.connect(lambda: self.solicitarAtencion(1))
        self.btn2.clicked.connect(lambda: self.solicitarAtencion(2))

    # setupUi

    def retranslateUi(self, base):
        base.setWindowTitle(QCoreApplication.translate("base", u"MainWindow", None))
        self.btn1.setText(QCoreApplication.translate("base", u"CON \n"
" TURNO", None))
        self.btn2.setText(QCoreApplication.translate("base", u"SIN \n"
" TURNO", None))
    # retranslateUi

