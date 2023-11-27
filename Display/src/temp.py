# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DisplayV10EiqWBD.ui'
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
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1067, 686)
        MainWindow.setStyleSheet(u"#borde_top {\n"
"	background-color: qlineargradient(spread:pad, x1:0.977, y1:0.636409, x2:0.125, y2:0.636636, stop:0 rgba(4, 42, 79,255), stop:1 rgba(0, 73, 113,255));\n"
"	border-radius:2px;\n"
"}\n"
"#borde_top QLabel{\n"
"	color:white;\n"
"}\n"
"\n"
"#widget{\n"
"	background-image: url(:/img/img/grisSinFondo.jpg);\n"
"}\n"
"\n"
"#borde_video{\n"
"	border-image: url(:/img/img/fondo_sin.jpg);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"\n"
"#titulo_llamado{\n"
"	background-color: rgb(4, 42, 79);\n"
"	color:white;\n"
"	border-radius:2px;\n"
"}\n"
"#borde_turnos{\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"#box_titulo QLabel{\n"
"	background-color: rgb(204, 204, 204);\n"
"\n"
"	color:	rgb(4, 42, 79);\n"
"	border-radius:2px;\n"
"\n"
"}\n"
"\n"
"#nums QLabel{\n"
"	background-color: rgb(204, 204, 204);\n"
"\n"
"	color:	rgb(4, 42, 79);\n"
"	border-radius:2px;\n"
"\n"
"}\n"
"\n"
"#borde_bottom{\n"
"	background-color: rgb(4, 42, 79);\n"
"	color:white;\n"
"}\n"
"#borde_bottom QLabel{\n"
"	background-color: rgb(4, 42, 79);\n"
""
                        "	color:white;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_box = QWidget(self.widget)
        self.top_box.setObjectName(u"top_box")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_box.sizePolicy().hasHeightForWidth())
        self.top_box.setSizePolicy(sizePolicy)
        self.top_box.setMinimumSize(QSize(0, 50))
        self.verticalLayout_12 = QVBoxLayout(self.top_box)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(40, 30, 600, 10)

        self.verticalLayout_2.addWidget(self.top_box)

        self.fondo = QWidget(self.widget)
        self.fondo.setObjectName(u"fondo")
        self.horizontalLayout = QHBoxLayout(self.fondo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.fondo)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 80)
        self.base_fondoVideo = QWidget(self.widget_5)
        self.base_fondoVideo.setObjectName(u"base_fondoVideo")
        self.verticalLayout_4 = QVBoxLayout(self.base_fondoVideo)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(30, 40, 0, 20)
        self.base_hora = QWidget(self.base_fondoVideo)
        self.base_hora.setObjectName(u"base_hora")
        self.base_hora.setMinimumSize(QSize(0, 60))
        self.base_hora.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_13 = QVBoxLayout(self.base_hora)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.borde_top = QWidget(self.base_hora)
        self.borde_top.setObjectName(u"borde_top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.borde_top.sizePolicy().hasHeightForWidth())
        self.borde_top.setSizePolicy(sizePolicy1)
        self.borde_top.setMinimumSize(QSize(300, 60))
        self.borde_top.setMaximumSize(QSize(700, 60))
        self.horizontalLayout_11 = QHBoxLayout(self.borde_top)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 0, 10, 0)
        self.widget_2 = QWidget(self.borde_top)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.city_label = QLabel(self.widget_2)
        self.city_label.setObjectName(u"city_label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.city_label.setFont(font)
        self.city_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.city_label)


        self.horizontalLayout_11.addWidget(self.widget_2, 0, Qt.AlignVCenter)

        self.widget_4 = QWidget(self.borde_top)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_15 = QVBoxLayout(self.widget_7)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.temp_icon = QLabel(self.widget_7)
        self.temp_icon.setObjectName(u"temp_icon")
        self.temp_icon.setStyleSheet(u"border-image:url(https://openweathermap.org/img/w/02n.png);")
        self.temp_icon.setPixmap(QPixmap(u":/img/img/icons8-people-64.png"))
        self.temp_icon.setScaledContents(False)
        self.temp_icon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.temp_icon.setMargin(0)

        self.verticalLayout_15.addWidget(self.temp_icon, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_10.addWidget(self.widget_7, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.temp_label = QLabel(self.widget_8)
        self.temp_label.setObjectName(u"temp_label")
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.temp_label.setFont(font1)
        self.temp_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.temp_label, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_10.addWidget(self.widget_8)


        self.horizontalLayout_11.addWidget(self.widget_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_3 = QWidget(self.borde_top)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.widget_3.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 9, 20, 9)
        self.time_label = QLabel(self.widget_3)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setFont(font1)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.time_label)

        self.hs = QLabel(self.widget_3)
        self.hs.setObjectName(u"hs")
        self.hs.setFont(font)

        self.horizontalLayout_13.addWidget(self.hs, 0, Qt.AlignVCenter)


        self.horizontalLayout_11.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.borde_top)


        self.verticalLayout_4.addWidget(self.base_hora)

        self.borde_video = QWidget(self.base_fondoVideo)
        self.borde_video.setObjectName(u"borde_video")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.borde_video.sizePolicy().hasHeightForWidth())
        self.borde_video.setSizePolicy(sizePolicy3)
        self.borde_video.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.borde_video)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.video_widget = QWidget(self.borde_video)
        self.video_widget.setObjectName(u"video_widget")
        self.video_widget.setMinimumSize(QSize(300, 300))

        self.verticalLayout_14.addWidget(self.video_widget)


        self.verticalLayout_4.addWidget(self.borde_video)


        self.verticalLayout_3.addWidget(self.base_fondoVideo)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.fondo)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, 60, 60)
        self.borde_turnos = QWidget(self.widget_6)
        self.borde_turnos.setObjectName(u"borde_turnos")
        self.verticalLayout_5 = QVBoxLayout(self.borde_turnos)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 0, 20, 20)
        self.base_turnos = QWidget(self.borde_turnos)
        self.base_turnos.setObjectName(u"base_turnos")
        self.verticalLayout_6 = QVBoxLayout(self.base_turnos)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.base_titulo = QWidget(self.base_turnos)
        self.base_titulo.setObjectName(u"base_titulo")
        sizePolicy.setHeightForWidth(self.base_titulo.sizePolicy().hasHeightForWidth())
        self.base_titulo.setSizePolicy(sizePolicy)
        self.base_titulo.setMinimumSize(QSize(0, 50))
        self.verticalLayout_10 = QVBoxLayout(self.base_titulo)
        self.verticalLayout_10.setSpacing(1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 1)
        self.titulo_llamado = QLabel(self.base_titulo)
        self.titulo_llamado.setObjectName(u"titulo_llamado")
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        self.titulo_llamado.setFont(font2)
        self.titulo_llamado.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.titulo_llamado)

        self.box_titulo = QWidget(self.base_titulo)
        self.box_titulo.setObjectName(u"box_titulo")
        self.box_titulo.setMinimumSize(QSize(0, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.box_titulo)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.box_num = QWidget(self.box_titulo)
        self.box_num.setObjectName(u"box_num")
        self.verticalLayout_8 = QVBoxLayout(self.box_num)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_num = QLabel(self.box_num)
        self.label_num.setObjectName(u"label_num")
        font3 = QFont()
        font3.setPointSize(45)
        font3.setBold(True)
        self.label_num.setFont(font3)
        self.label_num.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_num)


        self.horizontalLayout_4.addWidget(self.box_num)

        self.box_caja = QWidget(self.box_titulo)
        self.box_caja.setObjectName(u"box_caja")
        self.verticalLayout_9 = QVBoxLayout(self.box_caja)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_caja = QLabel(self.box_caja)
        self.label_caja.setObjectName(u"label_caja")
        self.label_caja.setFont(font3)
        self.label_caja.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_caja)


        self.horizontalLayout_4.addWidget(self.box_caja)


        self.verticalLayout_10.addWidget(self.box_titulo)


        self.verticalLayout_6.addWidget(self.base_titulo)

        self.base_nums = QWidget(self.base_turnos)
        self.base_nums.setObjectName(u"base_nums")
        self.horizontalLayout_3 = QHBoxLayout(self.base_nums)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.nums = QWidget(self.base_nums)
        self.nums.setObjectName(u"nums")
        font4 = QFont()
        font4.setPointSize(20)
        self.nums.setFont(font4)
        self.verticalLayout_7 = QVBoxLayout(self.nums)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.box_1 = QWidget(self.nums)
        self.box_1.setObjectName(u"box_1")
        self.horizontalLayout_5 = QHBoxLayout(self.box_1)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.num1 = QLabel(self.box_1)
        self.num1.setObjectName(u"num1")
        font5 = QFont()
        font5.setPointSize(36)
        font5.setBold(True)
        self.num1.setFont(font5)
        self.num1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.num1)

        self.caja1 = QLabel(self.box_1)
        self.caja1.setObjectName(u"caja1")
        self.caja1.setFont(font5)
        self.caja1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.caja1)


        self.verticalLayout_7.addWidget(self.box_1)

        self.box_2 = QWidget(self.nums)
        self.box_2.setObjectName(u"box_2")
        self.horizontalLayout_6 = QHBoxLayout(self.box_2)
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.num2 = QLabel(self.box_2)
        self.num2.setObjectName(u"num2")
        self.num2.setFont(font5)
        self.num2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.num2)

        self.caja2 = QLabel(self.box_2)
        self.caja2.setObjectName(u"caja2")
        self.caja2.setFont(font5)
        self.caja2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.caja2)


        self.verticalLayout_7.addWidget(self.box_2)

        self.box_3 = QWidget(self.nums)
        self.box_3.setObjectName(u"box_3")
        self.horizontalLayout_7 = QHBoxLayout(self.box_3)
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.num3 = QLabel(self.box_3)
        self.num3.setObjectName(u"num3")
        self.num3.setFont(font5)
        self.num3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.num3)

        self.caja3 = QLabel(self.box_3)
        self.caja3.setObjectName(u"caja3")
        self.caja3.setFont(font5)
        self.caja3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.caja3)


        self.verticalLayout_7.addWidget(self.box_3)

        self.box_4 = QWidget(self.nums)
        self.box_4.setObjectName(u"box_4")
        self.horizontalLayout_8 = QHBoxLayout(self.box_4)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.num4 = QLabel(self.box_4)
        self.num4.setObjectName(u"num4")
        self.num4.setFont(font5)
        self.num4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.num4)

        self.caja4 = QLabel(self.box_4)
        self.caja4.setObjectName(u"caja4")
        self.caja4.setFont(font5)
        self.caja4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.caja4)


        self.verticalLayout_7.addWidget(self.box_4)

        self.box_5 = QWidget(self.nums)
        self.box_5.setObjectName(u"box_5")
        self.horizontalLayout_9 = QHBoxLayout(self.box_5)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.num5 = QLabel(self.box_5)
        self.num5.setObjectName(u"num5")
        self.num5.setFont(font5)
        self.num5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.num5)

        self.caja5 = QLabel(self.box_5)
        self.caja5.setObjectName(u"caja5")
        self.caja5.setFont(font5)
        self.caja5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.caja5)


        self.verticalLayout_7.addWidget(self.box_5)


        self.horizontalLayout_3.addWidget(self.nums)


        self.verticalLayout_6.addWidget(self.base_nums)


        self.verticalLayout_5.addWidget(self.base_turnos)


        self.horizontalLayout_2.addWidget(self.borde_turnos)


        self.horizontalLayout.addWidget(self.widget_6)


        self.verticalLayout_2.addWidget(self.fondo)

        self.borde_bottom = QWidget(self.widget)
        self.borde_bottom.setObjectName(u"borde_bottom")
        sizePolicy.setHeightForWidth(self.borde_bottom.sizePolicy().hasHeightForWidth())
        self.borde_bottom.setSizePolicy(sizePolicy)
        self.borde_bottom.setMinimumSize(QSize(0, 60))
        self.verticalLayout_11 = QVBoxLayout(self.borde_bottom)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.labelDesplazable = QLabel(self.borde_bottom)
        self.labelDesplazable.setObjectName(u"labelDesplazable")
        self.labelDesplazable.setFont(font1)
        self.labelDesplazable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.labelDesplazable, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.borde_bottom)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.city_label.setText(QCoreApplication.translate("MainWindow", u"Buenos Aires, La Plata", None))
        self.temp_icon.setText("")
        self.temp_label.setText(QCoreApplication.translate("MainWindow", u"32`C", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"22:30", None))
        self.hs.setText(QCoreApplication.translate("MainWindow", u"HS", None))
        self.titulo_llamado.setText(QCoreApplication.translate("MainWindow", u"LLAMADO TURNOS", None))
        self.label_num.setText(QCoreApplication.translate("MainWindow", u"NUM", None))
        self.label_caja.setText(QCoreApplication.translate("MainWindow", u"CAJA", None))
        self.num1.setText(QCoreApplication.translate("MainWindow", u"B3", None))
        self.caja1.setText(QCoreApplication.translate("MainWindow", u"BOX 1", None))
        self.num2.setText(QCoreApplication.translate("MainWindow", u"B2", None))
        self.caja2.setText(QCoreApplication.translate("MainWindow", u"BOX 1", None))
        self.num3.setText(QCoreApplication.translate("MainWindow", u"B1", None))
        self.caja3.setText(QCoreApplication.translate("MainWindow", u"BOX 1", None))
        self.num4.setText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.caja4.setText(QCoreApplication.translate("MainWindow", u"BOX 1", None))
        self.num5.setText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.caja5.setText(QCoreApplication.translate("MainWindow", u"BOX 1", None))
        self.labelDesplazable.setText(QCoreApplication.translate("MainWindow", u"Hospital Privado Sudamericano", None))
    # retranslateUi

