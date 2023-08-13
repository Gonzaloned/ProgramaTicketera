from PyQt6.QtSql import *


conn_str = (
r'DRIVER={SQL Server};'
r'SERVER=GONZALO\DBGON;'
r'DATABASE=turnos;'
r'Trusted_Connection=yes;'
)
    
#Create a global var con for the connection


#Set the new database driver (in this case QODBC)
con = QSqlDatabase.addDatabase('QODBC')
con.setDatabaseName(conn_str)
#Set the db Server DRIVER,SERVER,DATABASE


print('starting connection')
#Check connection
if con.open():
    print(' Succesfull connection')
else:
    print("Database Error: %s"  % con.lastError().databaseText())
    exit(1)

query = QSqlQuery("SELECT dni, hora, numero FROM turnos_cajas")
