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

from PantallaPricipal import PantallaPrincipal

if __name__ == '__main__':

    #Creo app
    app = QApplication(sys.argv)

    #Creo UI pantalla 1
    principal= PantallaPrincipal()

    #Creo ventana
    ventana = QMainWindow()
    ventana.setWindowTitle("Menu Principal")
    ventana.setWindowIcon(QIcon(r"C:\Ticketera\img\logo_sinFondo.png"))
    #Seteo template ventana
    principal.setupUi(ventana)
    
    #Muestro ventana pantalla completa
    #ventana_principal.showFullScreen()
    ventana.show()
    #Cerrar
    sys.exit(app.exec())


