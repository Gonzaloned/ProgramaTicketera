# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerkhUWYn.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)
import resources

class Pop(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(500, 400))
        MainWindow.setStyleSheet(u"#fondo{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.295455 rgba(157, 19, 45, 255), stop:1 rgba(0, 73, 113, 255));\n"
"\n"
"	border-radius: 20px;\n"
"	\n"
"}\n"
"\n"
"#texto{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fondo = QWidget(self.centralwidget)
        self.fondo.setObjectName(u"fondo")
        self.verticalLayout_2 = QVBoxLayout(self.fondo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.fondo)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 40, -1, -1)
        self.texto = QLabel(self.widget)
        self.texto.setObjectName(u"texto")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.texto.setFont(font)
        self.texto.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.texto)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.fondo)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(60, 0, 60, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(344, 201))
        self.label.setPixmap(QPixmap(u":/images/img/iconWhite.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.fondo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.texto.setText(QCoreApplication.translate("MainWindow", u"Retire su numero \n"
" y tome asiento \n"
" ser\u00e1 llamado por pantalla", None))
        self.label.setText("")
    # retranslateUi

