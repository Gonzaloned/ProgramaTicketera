# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectornppUyB.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import pantall2_rc
import pantalla1_rc

class Selector(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(94, 326)
        MainWindow.setStyleSheet(u"#main{\n"
"	\n"
"	border-image: url(:/imagenes/img/fondo_sin.jpg);\n"
"\n"
"}\n"
"QPushButton{\n"
"	border-radius:30px;\n"
"	border: 1px solid rgba(255, 255, 255, 130);\n"
"	background-color: rgba(255, 255, 255, 130);\n"
"\n"
"}\n"
"")
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
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(92, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button1 = QPushButton(self.widget)
        self.button1.setObjectName(u"button1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setMinimumSize(QSize(60, 60))
        self.button1.setMaximumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/icons/iconsAtencion/check-mark-7-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button1.setIcon(icon)
        self.button1.setIconSize(QSize(26, 26))

        self.horizontalLayout_2.addWidget(self.button1)


        self.verticalLayout.addWidget(self.widget)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(92, 81))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button4 = QPushButton(self.widget_4)
        self.button4.setObjectName(u"button4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy1)
        self.button4.setMinimumSize(QSize(60, 60))
        self.button4.setMaximumSize(QSize(60, 60))
        icon1 = QIcon()
        icon1.addFile(u":/icons/iconsAtencion/x-mark-3-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button4.setIcon(icon1)
        self.button4.setIconSize(QSize(26, 26))

        self.horizontalLayout_3.addWidget(self.button4)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(92, 81))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button2 = QPushButton(self.widget_2)
        self.button2.setObjectName(u"button2")
        self.button2.setMinimumSize(QSize(60, 60))
        self.button2.setMaximumSize(QSize(60, 60))
        icon2 = QIcon()
        icon2.addFile(u":/icons/iconsAtencion/info-2-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button2.setIcon(icon2)
        self.button2.setIconSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.button2)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(92, 81))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button3 = QPushButton(self.widget_3)
        self.button3.setObjectName(u"button3")
        self.button3.setMinimumSize(QSize(60, 60))
        self.button3.setMaximumSize(QSize(60, 60))
        icon3 = QIcon()
        icon3.addFile(u":/icons/iconsAtencion/settings-5-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button3.setIcon(icon3)
        self.button3.setIconSize(QSize(26, 26))

        self.horizontalLayout_5.addWidget(self.button3)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button1.setText("")
        self.button4.setText("")
        self.button2.setText("")
        self.button3.setText("")
    # retranslateUi

