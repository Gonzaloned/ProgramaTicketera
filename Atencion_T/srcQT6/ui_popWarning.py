
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import fondos_rc

class PopWarning(object):
    def setupUi(self, MainWindow, entradaTexto):
        #Save window locally
        self.ventana= MainWindow

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 228)
        MainWindow.setMaximumSize(QSize(320, 230))
        MainWindow.setStyleSheet(u"#fondo{\n"
"\n"
"	border-image: url(:/fondos/img/fondos/fondo_sin.jpg);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius:15px;\n"
"	color: rgb(0, 73, 113);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#btn1{\n"
"	color: rgba(0, 73, 113, 220);\n"
"	border: 1px solid rgba(0, 73, 113,30);\n"
"}\n"
"\n"
"#btn2{\n"
"	color: rgba(157, 19, 45,220);	\n"
"	border: 1px solid rgba(95, 12, 28, 30);\n"
"}\n"
"\n"
"#fondo{border-radius: 15px}\n"
"#btn1:pressed{\n"
"	\n"
"	background-color: rgb(160, 159, 176);\n"
"	color: rgba(0, 73, 113, 240);\n"
"  	border-style: solid;\n"
"    border-width: 2px;\n"
"	border-color: rgba(0, 73, 113,20);\n"
"}\n"
"\n"
"#btn2:pressed{	\n"
"	background-color: rgb(160, 159, 176);\n"
"	color: rgba(157, 19, 45,240);\n"
"  	border-style: solid;\n"
"    border-width: 2px;\n"
"	border-color: rgba(95, 12, 28, 20);\n"
"\n"
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
        self.verticalLayout_2 = QVBoxLayout(self.fondo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.fondo)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.text = QLabel(self.widget_3)
        self.text.setObjectName(u"text")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.text.setFont(font)
        self.text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.text)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.fondo)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 140))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn2 = QPushButton(self.widget_2)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(200, 40))
        self.btn2.setMaximumSize(QSize(200, 40))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.btn2.setFont(font1)

        self.horizontalLayout.addWidget(self.btn2, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.fondo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        #INITIAL WINDOW CONFIG
        self.ventana.setWindowFlags(Qt.FramelessWindowHint)   #Not show windows bar
        self.ventana.setAttribute(Qt.WA_TranslucentBackground) #set translucent background


        #Put the text in the label
        self.text.setText(entradaTexto)

        #EVENTS

        self.btn2.clicked.connect(lambda: self.ventana.close())

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        self.btn2.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vent=QMainWindow()
    popW= Warning() #Creo la ventana login
    popW.setupUi(vent, 'mensaje') #Paso la ventana y mensaje
    vent.show() #Show
    sys.exit(app.exec())
