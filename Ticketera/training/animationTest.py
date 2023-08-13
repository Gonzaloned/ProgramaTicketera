
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
class Template(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"#fondo{\n"
"	background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"#fondo2{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fondo = QWidget(self.centralwidget)
        self.fondo.setObjectName(u"fondo")
        self.fondo2 = QWidget(self.fondo)
        self.fondo2.setObjectName(u"fondo2")
        self.fondo2.setGeometry(QRect(179, 99, 321, 221))

        self.verticalLayout.addWidget(self.fondo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.reduce()
    # setupUi

    '''def animation(self):
        self.eff = QGraphicsOpacityEffect(self.fondo2)
        self.eff.setOpacity(1)
        self.setGraphicsEffect(self.eff)

        self.animation = QPropertyAnimation(self.eff,b'opacity')
        self.animation.setDuration(5000)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start()'''

    def reduce(self):
        self.eff = QGraphicsOpacityEffect(self.fondo2)
        self.eff.setOpacity(0.3)
        self.fondo2.setGraphicsEffect(self.eff)

        self.anim = QPropertyAnimation(self.eff, b"opacity")
        self.anim.setDuration(2000)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.start()


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

if __name__ == "__main__":
    app= QApplication(sys.argv)
    window= QMainWindow()
    ui= Template()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
