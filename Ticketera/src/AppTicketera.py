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
import logger_config
import logging
import win32event
import win32api
import winerror

class SingleInstance:
    def __init__(self, name):
        # Crear un objeto mutex con un nombre único.
        self.mutexname = name
        self.mutex = win32event.CreateMutex(None, False, self.mutexname)
        # Obtener el último error que ocurrió al crear el mutex.
        self.last_error = win32api.GetLastError()

    def already_running(self):
        # Verificar si ya existe un error de "ERROR_ALREADY_EXISTS".
        return self.last_error == winerror.ERROR_ALREADY_EXISTS

    def __del__(self):
        # Cerrar el objeto mutex cuando se destruya la instancia.
        if self.mutex:
            win32api.CloseHandle(self.mutex)

# Nombre único para el objeto mutex.
mutex_name = "Global\\MutexTicketera"

if __name__ == "__main__":
    # Crear una instancia de SingleInstance con el nombre del mutex.
    instance = SingleInstance(mutex_name)
    # Verificar si ya hay una instancia de la aplicación en ejecución.
    if instance.already_running():
        logging.info('Intento de inicio, aplicacion corriendo, EXIT.')
        exit()
    else:
        logging.info('Inicio programa')
        # Aquí puedes colocar el código de tu programa
        if __name__ == "__main__":
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


