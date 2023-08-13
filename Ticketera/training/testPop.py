# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popYaTsUo.ui'
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
from PySide6.QtWidgets import *
import pantalla1_rc
import sys

class Pop(QMainWindow):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(549, 441)
        MainWindow.setStyleSheet(u"#fondo{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.295455 rgba(157, 19, 45, 240), stop:1 rgba(0, 73, 113, 240));\n"
"border-radius: 20px;\n"
"	\n"
"}\n"
"\n"
"#txt{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.fondo = QWidget(self.widget)
        self.fondo.setObjectName(u"fondo")
        self.verticalLayout_3 = QVBoxLayout(self.fondo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.txt = QLabel(self.fondo)
        self.txt.setObjectName(u"txt")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.txt.setFont(font)
        self.txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.txt, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.img = QLabel(self.fondo)
        self.img.setObjectName(u"img")
        self.img.setPixmap(QPixmap(u":/iconos/img/fondo.png"))
        self.img.setScaledContents(False)

        self.verticalLayout_3.addWidget(self.img, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.fondo)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt.setText(QCoreApplication.translate("MainWindow", u"Retire su numero \n"
" y tome asiento \n"
" ser\u00e1 llamado por pantallla", None))
        self.img.setText("")
    # retranslateUi



if __name__ == '__main__':
    #Creo app
    app = QApplication(sys.argv)

    #Creo pantalla1

    
    ventana= Pop()

    #Cerrar
    sys.exit(app.exec())