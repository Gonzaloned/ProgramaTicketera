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
from ManejadorDatos import ManejadorDatos

import LoggingConfig
import logging
DRIVER='ODBC Driver 17 for SQL Server'
SERVER_NAME = 'GONZALO\\DBGON'
DATABASE_NAME = 'turnos'
USERNAME = 'gon'
PASSWORD = '123456'

class ConectorDB():
    def __init__(self):
        #Set the new database driver (in this case QODBC)
        self.con = QSqlDatabase().addDatabase('QODBC')
        self.createConnection()
        
    def createConnection(self):
        
        #Set the db Server DRIVER,SERVER,DATABASE
        self.con.setDatabaseName(ManejadorDatos.getConnectionString())
        
        #Check connection
        if self.con.open():
            logging.info("Correct start of the DB connection")
        else:
            error_msg=("Database Error: %s"  % self.con.lastError().databaseText())
            logging.error(error_msg)

        #Return the QSqlDatabase 
        return self.con

    def resetConnection(self):
        logging.info("Restarting the connection...")
        self.con.close()
        self.createConnection()
        

    def queryExecution(self,query):

        #If con not open, reconnect
        if not(self.con.isOpen()):
            logging.error(f"Incorrect con in query,{query} retry")
            self.resetConnection()
        else:

            #new query object  QSqlQuery(database target)
            self.qry= QSqlQuery(self.con)

            #Prepare the query to execute
            self.qry.prepare(query)

            if (self.qry.exec()):
                print('Query realizada exitosamente')
                return True
            else:
                logging.error("Error in query ", query)
                self.resetConnection()
                return False

    def getQuery(self):
        return self.qry
