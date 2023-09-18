
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from PyQt6.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel
from connection import Connection
import fondos_rc
import fondos_rc
import datetime


class SettingsWindow(object): 

    def verHistorial(self):
        QUERY=f'''SELECT [dni],[hora],[tipo],[atiende_usuario]\n
                FROM [turnos].[dbo].[turnos_actual]'''

        query_data= QSqlQuery(self.db) #Creeate a query and link to db
        query_data.prepare(QUERY) #Set the query

        #Rows=0
        self.tableWidget.setRowCount(0)
        if query_data.exec(): #If query executes ok

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

    def marcarVideoActual(self):
        pass

    def resetTurnos(self):
        QUERY=f'''INSERT INTO turnos_global(dni,hora,tipo,atiende_usuario) 
        SELECT a.dni,a.hora,a.tipo,a.atiende_usuario FROM turnos_actual a'''

        query_data= QSqlQuery(self.db) #Creeate a query and link to db
        query_data.prepare(QUERY) #Set the query

        #Rows=0
        self.tableWidget.setRowCount(0)
        if query_data.exec(): #If query executes ok
            pass

    def infoDisplayer(self):
        pass

    def setupUi(self, MainWindow, dataBase):

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
        icon.addFile(u":/iconosWhite/iconsAtencion/bell-2-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.video_selector.setIcon(icon)
        self.video_selector.setIconSize(QSize(26, 26))

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
        icon1.addFile(u":/iconosWhite/iconsAtencion/check-mark-7-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reset_turnos.setIcon(icon1)
        self.reset_turnos.setIconSize(QSize(26, 26))

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
        icon2.addFile(u":/iconosWhite/iconsAtencion/letter-t-24.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u":/iconosWhite/iconsAtencion/info-2-32.ico", QSize(), QIcon.Normal, QIcon.Off)
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

        self.tableWidget.setColumnWidth(2,120) #Set [col dni],width
        self.tableWidget.setColumnWidth(3,120) #Set [col atiende],width
        self.ver_historial.clicked.connect(lambda: self.verHistorial())
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"VISOR TURNOS", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Numero", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DNI", None));
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

