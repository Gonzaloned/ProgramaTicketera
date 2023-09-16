# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingseZjTtx.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import fondos_rc
import fondos_rc

class Settings(object):
    def setupUi(self, MainWindow):
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

        self.verticalLayout_4.addWidget(self.llamar, 0, Qt.AlignHCenter)

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

        self.verticalLayout_5.addWidget(self.sinTurno, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.cont2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.cont2, 0, Qt.AlignVCenter)

        self.cont3 = QWidget(self.frame)
        self.cont3.setObjectName(u"cont3")
        self.cont3.setMinimumSize(QSize(92, 81))
        self.verticalLayout_6 = QVBoxLayout(self.cont3)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.conTurno = QPushButton(self.cont3)
        self.conTurno.setObjectName(u"conTurno")
        sizePolicy.setHeightForWidth(self.conTurno.sizePolicy().hasHeightForWidth())
        self.conTurno.setSizePolicy(sizePolicy)
        self.conTurno.setMinimumSize(QSize(60, 60))
        self.conTurno.setMaximumSize(QSize(60, 60))
        icon2 = QIcon()
        icon2.addFile(u":/iconosWhite/iconsAtencion/letter-t-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.conTurno.setIcon(icon2)
        self.conTurno.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.conTurno, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.cont3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.cont3)

        self.cont4 = QWidget(self.frame)
        self.cont4.setObjectName(u"cont4")
        self.cont4.setMinimumSize(QSize(92, 81))
        self.verticalLayout_7 = QVBoxLayout(self.cont4)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 5, 0, 5)
        self.settings = QPushButton(self.cont4)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(60, 60))
        self.settings.setMaximumSize(QSize(60, 60))
        icon3 = QIcon()
        icon3.addFile(u":/iconosWhite/iconsAtencion/info-2-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon3)
        self.settings.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.settings, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.cont4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.cont4)


        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.fondo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"VISOR TURNOS", None))
        self.llamar.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SELECCION\n"
" VIDEO", None))
        self.sinTurno.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"RESET\n"
"TURNOS", None))
        self.conTurno.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VER\n"
" HISTORIAL", None))
        self.settings.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"INFO", None))
    # retranslateUi

