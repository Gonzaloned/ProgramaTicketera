import datetime
from random import randint
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,QTableWidget,QTableView,
    QWidget,QMessageBox,QTableWidgetItem)
from PyQt6.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel
import sys

DRIVER='ODBC Driver 17 for SQL Server'
SERVER_NAME = 'GONZALO\DBGON'
DATABASE_NAME = 'turnos'
USERNAME = 'gon'
PASSWORD = '123456'

class Connection():
    def __init__(self):
        #Set the new database driver (in this case QODBC)
        self.con = QSqlDatabase().addDatabase('QODBC')

        self.createConnection()    
        #SQL_STATEMENT = "INSERT INTO dbo.turnos_cajas(dni,hora) VALUES (444444,'2015-03-25 15:30:00')"

    def createConnection(self):
        #Setting attributes string to start connection
        conn_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=GONZALO\DBGON;'
        r'DATABASE=turnos;'
        r'Trusted_Connection=yes;'
        )

        #Set the db Server DRIVER,SERVER,DATABASE
        self.con.setDatabaseName(conn_str)

        print('starting connection')
        #Check connection
        if self.con.open():
            print(' Succesfull connection')
        else:
            print("Database Error: %s"  % self.con.lastError().databaseText())
            exit(0)


    def executeQuery(self,query):
        print('processing query')

        #new query object  QSqlQuery(database objetive dbObject)
        qry= QSqlQuery(self.con)

        #Prepare the query to execute
        qry.prepare(query)
        if (qry.exec()):
            print('Query realizada exitosamente')
            return True
        else:
            return False


