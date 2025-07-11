# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadoraDRTcKI.ui'
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Calculadora(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(602, 726)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	background-color: rgb(255, 255, 0);\n"
"}\n"
"#QWidget{\n"
"	background-color: rgb(85, 85, 127);\n"
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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 100))
        self.widget.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.widget)

        self.text = QWidget(self.frame)
        self.text.setObjectName(u"text")
        self.text.setStyleSheet(u"#QPushButton{\n"
"size:100x100\n"
"}")
        self.gridLayout = QGridLayout(self.text)
        self.gridLayout.setObjectName(u"gridLayout")
        self.B1 = QWidget(self.text)
        self.B1.setObjectName(u"B1")
        self.horizontalLayout = QHBoxLayout(self.B1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.B1)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout.addWidget(self.B1, 0, 0, 1, 1)

        self.B2 = QWidget(self.text)
        self.B2.setObjectName(u"B2")
        self.verticalLayout_3 = QVBoxLayout(self.B2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.B2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.B2, 0, 1, 1, 1)

        self.B3 = QWidget(self.text)
        self.B3.setObjectName(u"B3")
        self.horizontalLayout_2 = QHBoxLayout(self.B3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.B3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.gridLayout.addWidget(self.B3, 0, 2, 1, 1)

        self.B4 = QWidget(self.text)
        self.B4.setObjectName(u"B4")
        self.horizontalLayout_3 = QHBoxLayout(self.B4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_4 = QPushButton(self.B4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.B4, 1, 0, 1, 1)

        self.B5 = QWidget(self.text)
        self.B5.setObjectName(u"B5")
        self.horizontalLayout_4 = QHBoxLayout(self.B5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_5 = QPushButton(self.B5)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_4.addWidget(self.pushButton_5)


        self.gridLayout.addWidget(self.B5, 1, 1, 1, 1)

        self.B6 = QWidget(self.text)
        self.B6.setObjectName(u"B6")
        self.horizontalLayout_5 = QHBoxLayout(self.B6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_6 = QPushButton(self.B6)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_5.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.B6, 1, 2, 1, 1)

        self.B7 = QWidget(self.text)
        self.B7.setObjectName(u"B7")
        self.horizontalLayout_8 = QHBoxLayout(self.B7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_7 = QPushButton(self.B7)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_8.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.B7, 2, 0, 1, 1)

        self.B8 = QWidget(self.text)
        self.B8.setObjectName(u"B8")
        self.horizontalLayout_9 = QHBoxLayout(self.B8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_8 = QPushButton(self.B8)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_9.addWidget(self.pushButton_8)


        self.gridLayout.addWidget(self.B8, 2, 1, 1, 1)

        self.B9 = QWidget(self.text)
        self.B9.setObjectName(u"B9")
        self.horizontalLayout_10 = QHBoxLayout(self.B9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_9 = QPushButton(self.B9)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_10.addWidget(self.pushButton_9)


        self.gridLayout.addWidget(self.B9, 2, 2, 1, 1)

        self.DEL = QWidget(self.text)
        self.DEL.setObjectName(u"DEL")
        self.horizontalLayout_11 = QHBoxLayout(self.DEL)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_10 = QPushButton(self.DEL)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_11.addWidget(self.pushButton_10)


        self.gridLayout.addWidget(self.DEL, 3, 0, 1, 1)

        self.B0 = QWidget(self.text)
        self.B0.setObjectName(u"B0")
        self.horizontalLayout_7 = QHBoxLayout(self.B0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_11 = QPushButton(self.B0)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_7.addWidget(self.pushButton_11)


        self.gridLayout.addWidget(self.B0, 3, 1, 1, 1)

        self.OK = QWidget(self.text)
        self.OK.setObjectName(u"OK")
        self.horizontalLayout_12 = QHBoxLayout(self.OK)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_12 = QPushButton(self.OK)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_12.addWidget(self.pushButton_12)


        self.gridLayout.addWidget(self.OK, 3, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.text)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ACTUAL", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

