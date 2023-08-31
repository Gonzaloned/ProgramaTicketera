
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)
import fondos_rc

class popOk(object):
    def setupUi(self, base,text):  #Get the text to create a pop
        if not base.objectName():
            base.setObjectName(u"base")
        base.resize(500, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(base.sizePolicy().hasHeightForWidth())
        base.setSizePolicy(sizePolicy)
        base.setMinimumSize(QSize(500, 400))
        base.setMaximumSize(QSize(636, 720))
        base.setStyleSheet(u"#fondo{\n"
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
        self.verticalLayout = QVBoxLayout(base)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fondo = QWidget(base)
        self.fondo.setObjectName(u"fondo")
        self.verticalLayout_2 = QVBoxLayout(self.fondo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 40)
        self.texto = QLabel(self.fondo)
        self.texto.setObjectName(u"texto")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.texto.setFont(font)
        self.texto.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.texto, 0, Qt.AlignBottom)

        self.imagen = QLabel(self.fondo)
        self.imagen.setObjectName(u"imagen")
        self.imagen.setMaximumSize(QSize(300, 200))
        self.imagen.setPixmap(QPixmap(u":/iconosWhite/img/iconsAtencion/iconWhite.png"))
        self.imagen.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.imagen, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.fondo)


        self.retranslateUi(base)

        QMetaObject.connectSlotsByName(base)

        id = QFontDatabase.addApplicationFont("./fonts/Central W01 Light.ttf")
        print (f"the id is{id}")

        #https://doc.qt.io/qtforpython-5/PySide2/QtGui/QFontDatabase.html#PySide2.QtGui.PySide2.QtGui.QFontDatabase.applicationFontFamilies
        
       #families = QFontDatabase.applicationFontFamilies(id)
        #print(families)

        #self.texto.setFont(QFont(families[0], 30))
        self.texto.setText(text)
    # setupUi

    def retranslateUi(self, base):
        base.setWindowTitle(QCoreApplication.translate("base", u"Form", None))
        
        self.imagen.setText("")
    # retranslateUi

