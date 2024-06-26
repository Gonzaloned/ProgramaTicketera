import datetime
from random import randint
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,QTableWidget,QTableView,
    QWidget,QMessageBox,QTableWidgetItem)
from PySide6.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel
import sys
import manejar_datos

import logger_config
import logging
DRIVER='ODBC Driver 17 for SQL Server'
SERVER_NAME = 'GONZALO\\DBGON'
DATABASE_NAME = 'turnos'
USERNAME = 'gon'
PASSWORD = '123456'

class Connection():
    def __init__(self):
        #Set the new database driver (in this case QODBC)
        self.con = QSqlDatabase().addDatabase('QODBC')
        self.createConnection()
        

    def createConnection(self):
        #Setting attributes string to start connection
        connection_string=manejar_datos.getConnectionString()
        #Set the db Server DRIVER,SERVER,DATABASE
        self.con.setDatabaseName(connection_string)
        print('Created a connection')
        #Check connection
        if self.con.open():
            print(' Succesfull connection')
            logging.info("Correct connection")
        else:
            error_msg=("Database Error: %s"  % self.con.lastError().databaseText())
            print(error_msg)
            logging.error(error_msg)

        return self.con

    def resetConnection(self):
        logging.info("The connection to db has been restarted")
        self.con.close()
        self.createConnection()
        

    def checkConnection(self):
        if (self.con.isValid()):
            return True
        else:
            self.resetConnection()


    def queryExecution(self,query):

        print(query)

        #If con not open, reconnect
        if not(self.con.isValid()):
            logging.error("Incorrect con in query, retry")
            self.resetConnection()

        #new query object  QSqlQuery(database target)
        self.qry= QSqlQuery(self.con)

        #Prepare the query to execute
        self.qry.prepare(query)
        if (self.qry.exec()):
            print('Query realizada exitosamente')
            return True
        else:
            logging.error("Error in query")
            self.resetConnection()
            return False

    def getQuery(self):
        return self.qry
