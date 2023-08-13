import sys
import typing
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from ui_pantalla1 import Pantalla1
from ui_calculadora import Calculadora

if __name__ == '__main__':
    #Creo app
    app = QApplication(sys.argv)

    #Creo UI pantalla 1
    principal= Pantalla1()

    #Creo ventana
    ventana_principal = QMainWindow()

    #Seteo template ventana
    principal.setupUi(ventana_principal)
    
    #Muestro ventana pantalla completa
    ventana_principal.showFullScreen()

    #Cerrar
    sys.exit(app.exec())