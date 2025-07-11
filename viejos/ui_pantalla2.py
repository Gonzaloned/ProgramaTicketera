# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla2Ndrqkx.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1028, 796)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	background-color: rgb(255, 170, 255);\n"
"}\n"
"#conTurno{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"#sinTurno{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cartel1 = QWidget(self.frame)
        self.cartel1.setObjectName(u"cartel1")
        self.verticalLayout_2 = QVBoxLayout(self.cartel1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.conTurno = QPushButton(self.cartel1)
        self.conTurno.setObjectName(u"conTurno")
        self.conTurno.setMinimumSize(QSize(400, 300))
        self.conTurno.setMaximumSize(QSize(400, 300))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.conTurno.setFont(font)

        self.verticalLayout_2.addWidget(self.conTurno)


        self.gridLayout.addWidget(self.cartel1, 0, 0, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")

        self.gridLayout.addWidget(self.widget_4, 1, 1, 1, 1)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)

        self.cartel2 = QWidget(self.frame)
        self.cartel2.setObjectName(u"cartel2")
        self.horizontalLayout = QHBoxLayout(self.cartel2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sinTurno = QPushButton(self.cartel2)
        self.sinTurno.setObjectName(u"sinTurno")
        self.sinTurno.setMinimumSize(QSize(400, 300))
        self.sinTurno.setMaximumSize(QSize(400, 300))
        self.sinTurno.setFont(font)

        self.horizontalLayout.addWidget(self.sinTurno)


        self.gridLayout.addWidget(self.cartel2, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.conTurno.setText(QCoreApplication.translate("MainWindow", u"ATENCION CON TURNO", None))
        self.sinTurno.setText(QCoreApplication.translate("MainWindow", u"SOLICITAR TURNO", None))
    # retranslateUi

