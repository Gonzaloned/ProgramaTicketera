

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QGuiApplication)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from PyQt6.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel
from connection import Connection
import iconos_rc
import fondos_rc

class Selector(object):

###########################################################################################
    ###FUNCTIONS CALLED BY THE BUTTONS
###########################################################################################

    #bells ring again
    def notificar(self):
        self.db.executeQuery()

    #Calls next shift
    def llamarProximo(self, tipo:int):
        self.db= Connection()
        #f'SELECT TOP (1) num FROM turnos_actual WHERE tipo={tipo} ORDER BY hora'
        transaction=\
        f'''BEGIN TRANSACTION;

        DECLARE @proximo_turno INT;

        -- Obtener el próximo turno disponible

        SELECT TOP 1 @proximo_turno = id
        FROM turnos_global
        WHERE estado = 'esperando'
        ORDER BY fecha_hora_llegada;

        -- Asignar el turno a una persona específica (supongamos que la persona tiene el ID 1)
        
        UPDATE turnos_global
        SET estado = 'atendido', persona_id = 1
        WHERE id = @proximo_turno;

        -- Actualizar el turno actual que se muestra en pantalla
        UPDATE turnos_actual
        SET turno_actual_id = @proximo_turno;

        COMMIT TRANSACTION;'''


        if (self.db.executeQuery(query_proximo)):
            qry= QSqlQuery(query_proximo)
            print(qry.nextResult())

    #Opens the options    
    def abrirOpciones(self):
        pass

    #cerrar programa
    def cerrarSelectora(self):
        self.ventana.close()


    #  This function calculates the position in the screen
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
"	border-image: url(:/fondos/img/fondo_sin.jpg);\n"
"	border-radius:20px;\n"
#"	border: 1px solid rgba(255, 255, 255, 130);\n"
"}\n"
"QPushButton{\n"
"	border-radius:30px;\n"
"	border: 1px solid rgba(255, 255, 255, 130);\n"
"	background-color: rgba(255, 255, 255, 130);\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgba(66, 66, 66, 150);\n"
"	border: 1px solid rgba(255, 255, 255, 80);\n"
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
        icon.addFile(u":/iconosWhite/iconsAtencion/bell-2-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.llamar.setIcon(icon)
        self.llamar.setIconSize(QSize(26, 26))

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
        icon1.addFile(u":/iconosWhite/iconsAtencion/check-mark-7-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sinTurno.setIcon(icon1)
        self.sinTurno.setIconSize(QSize(26, 26))

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
        icon2.addFile(u":/iconosWhite/iconsAtencion/letter-t-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.conTurno.setIcon(icon2)
        self.conTurno.setIconSize(QSize(26, 26))

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
        icon3.addFile(u":/iconosWhite/iconsAtencion/settings-5-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon3)
        self.settings.setIconSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.settings)


        self.verticalLayout.addWidget(self.cont4)

        self.cont5 = QWidget(self.frame)
        self.cont5.setObjectName(u"cont5")
        self.cont5.setMinimumSize(QSize(92, 81))
        self.horizontalLayout_5 = QHBoxLayout(self.cont5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.reset = QPushButton(self.cont5)
        self.reset.setObjectName(u"reset")
        self.reset.setMinimumSize(QSize(60, 60))
        self.reset.setMaximumSize(QSize(60, 60))
        icon4 = QIcon()
        icon4.addFile(u":/iconosWhite/iconsAtencion/x-mark-3-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reset.setIcon(icon4)
        self.reset.setIconSize(QSize(26, 26))

        self.horizontalLayout_5.addWidget(self.reset)


        self.verticalLayout.addWidget(self.cont5)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


        ##EVENTS
        self.llamar.clicked.connect(lambda: self.notificar())
        self.sinTurno.clicked.connect(lambda: self.llamarProximo(1))
        self.conTurno.clicked.connect(lambda: self.llamarProximo(2))
        self.settings.clicked.connect(lambda: self.abrirOpciones())
        self.reset.clicked.connect(lambda: self.cerrarSelectora())
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.llamar.setText("")
        self.sinTurno.setText("")
        self.conTurno.setText("")
        self.settings.setText("")
        self.reset.setText("")
    # retranslateUi

