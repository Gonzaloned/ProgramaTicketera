# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla1nTuMDC.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Pantalla1(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 822)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#center{\n"
"\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"#frame{\n"
"border-radius: 80px\n"
"}\n"
"#center{\n"
"border-radius: 80px\n"
"}\n"
"\n"
"#pushButton{\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.center = QWidget(self.frame)
        self.center.setObjectName(u"center")
        self.center.setMinimumSize(QSize(600, 400))
        self.center.setMaximumSize(QSize(600, 400))
        self.verticalLayout_3 = QVBoxLayout(self.center)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titulo = QWidget(self.center)
        self.titulo.setObjectName(u"titulo")
        self.horizontalLayout = QHBoxLayout(self.titulo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.titulo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.titulo, 0, Qt.AlignHCenter)

        self.ingreseDni = QWidget(self.center)
        self.ingreseDni.setObjectName(u"ingreseDni")
        self.horizontalLayout_2 = QHBoxLayout(self.ingreseDni)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.ingreseDni)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.ingreseDni, 0, Qt.AlignHCenter)

        self.buttonDni = QWidget(self.center)
        self.buttonDni.setObjectName(u"buttonDni")
        self.horizontalLayout_3 = QHBoxLayout(self.buttonDni)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.buttonDni)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 35))
        self.pushButton.setMaximumSize(QSize(200, 35))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.buttonDni)


        self.verticalLayout_2.addWidget(self.center)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BIENVENIDO AL HOSPITAL SUDAMERICANO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Por favor ingrese su dni", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ingresar DNI", None))
    # retranslateUi

