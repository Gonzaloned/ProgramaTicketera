from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from ui_NewLogin import Login
from ui_selector import Selector
import os

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
mutex_name = "Global\\MutexAtencion"

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
            app = QApplication(sys.argv)
            vent=QMainWindow()
            login= Login() #Creo la ventana login
            login.setupUi(vent) #Paso la ventana para configuraciones
            vent.show() #Show
            sys.exit(app.exec())
