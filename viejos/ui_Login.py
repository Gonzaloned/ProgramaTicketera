# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginrFMuKg.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

from Custom_Widgets.Widgets import QCustomStackedWidget
import imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1377, 798)
        MainWindow.setMinimumSize(QSize(80, 0))
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: white;\n"
"font-color: white;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-image: url(:/gon/img/fondo.jpg);\n"
"}\n"
"\n"
"#widget{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"#stackedWidget{\n"
" 	border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0.091, y1:0, x2:1, y2:0, stop:0 rgba(59,22,66,255), stop:1 rgba(156,25,42,255))\n"
"	\n"
"}\n"
"\n"
"#titulo {\n"
"\n"
"	font: 87 12pt \"Arial Black\";\n"
"}\n"
"#titulo_2 {\n"
"\n"
"	font: 87 12pt \"Arial Black\";\n"
"}\n"
"QLineEdit {\n"
"	background-color:rgba(255, 255, 255, 190);\n"
"	border-radius: 10px;\n"
"	padding: 8px 3px;\n"
"    font: 75 9pt \"Sitka Text\";\n"
"}\n"
"\n"
"QLabel {\n"
"	\n"
"	font: 75 9.2pt \"Sitka Text\";\n"
"}\n"
"\n"
"QPushButton{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	border-radius: 10px;\n"
"	background-color:rgba(255, 255, 255, 190);\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 450))
        self.widget.setMaximumSize(QSize(250, 450))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.stackedWidget = QCustomStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"img/icons8-people-64.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.titulo = QLabel(self.page)
        self.titulo.setObjectName(u"titulo")

        self.verticalLayout_3.addWidget(self.titulo, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_4.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.checkBox = QCheckBox(self.page)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 0))

        self.verticalLayout_3.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Sitka Text"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"img/acceso.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.titulo_2 = QLabel(self.page_2)
        self.titulo_2.setObjectName(u"titulo_2")

        self.verticalLayout_6.addWidget(self.titulo_2, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_5.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_5.addWidget(self.lineEdit_6)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.verticalSpacer_4 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 0))

        self.verticalLayout_6.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_6.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1377, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ingrese su informaci\u00f3n para registrarse", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Ingrese nombre completo", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Nuevo usuario", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Nueva contrase\u00f1a", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"De acuerdo con nuestras pol\u00edticas de uso", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ya registrado? Iniciar sesi\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hospital Privado Sudamericano 2023 ", None))
        self.label_3.setText("")
        self.titulo_2.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesi\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ingrese sus credenciales de acceso", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Acceder", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"No tienes usuario? Registrarse", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hospital Privado Sudamericano 2023 ", None))
    # retranslateUi

