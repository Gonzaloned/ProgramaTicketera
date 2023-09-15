

from PySide6.QtCore import *
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
from PyQt6.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel
from connection import Connection
import fondos_rc
from ui_selector import Selector
from ui_popWarning import PopWarning



class Login(object):

    #self.input.text() -> GET TEXT
    #self.input.setEchoMode(QLineEdit.EchoMode.Password) -> password mode
    #

    #Start the main program
    
    



    #Start a new program       
    def startProgram(self):
        vent= QMainWindow()
        ui= Selector()
        ui.setupUi(vent) #Paso la ventana para configuraciones
        vent.setWindowFlags(Qt.FramelessWindowHint)   #Not show windows bar
        vent.setAttribute(Qt.WA_TranslucentBackground) #set translucent background
        ui.location_on_the_screen()  #set the Position
        vent.show() #Show
        self.window.close()

    def registerUser(self):

        #Save the field values to local vars
        name= self.fullName.text()
        user= self.userRegister.text()
        pass1= self.passRegister.text()
        pass2= self.pass2Register.text()

        print(user.__len__())
        print(name.__len__())

        QUERY= f'''BEGIN TRANSACTION
            --REGISTRAR USUARIO
            INSERT INTO Persona(nombre,usuario,pass) VALUES('{name}','{user}','{pass1}');
            COMMIT TRANSACTION'''
        
        if (pass1==pass2): #if passwds match
            print('passwords match')
            if(user.__len__() >= 4) and (user.__len__() <= 10): #If user > 10char
                print('user lenght is ok')
                if(name.__len__() >= 4) and (name.__len__() < 30): #if name< 30 char
                    print('name lenght is ok')
                    #execute query

                else:  #name +30 char PopAdvice
                    self.popAdvice('El nombre debe tener\n entre 5 y 30 caracteres')
            else: #User +10 char PopAdvice
                self.popAdvice('El usuario debe tener\n entre 4 y 10 caracteres')
        else: #If passwords doesnt match popAdvice
            self.popAdvice('Las constraseñas no coinciden')
         
    def loginUser(self):
        username = self.userLogin.text() #Get the qlineEdit username text
        password = self.passLogin.text() #Get the qlineEdit password text

        query= QSqlQuery()
        query.prepare(f'SELECT * FROM Persona WHERE username:{username}')
        
        if query.first(): # if user exists 
            if (query.value('pass')== password): #If password equals to input, start nuew window
                pass
            else:
                pass
        else:
            #Crear ventana not exists
            pass

    def popAdvice(self,text):  #Create a window of advice
        self.pop= QMainWindow()
        self.ui= PopWarning()
        self.ui.setupUi(self.pop,text) #Paso la ventana para configuraciones
        self.pop.setWindowFlags(Qt.FramelessWindowHint)   #Not show windows bar
        self.pop.setAttribute(Qt.WA_TranslucentBackground) #set translucent background
        self.pop.show() #Show
        QTimer.singleShot(3000, lambda: self.pop.close())

    def setupUi(self, MainWindow):

        self.window= MainWindow #Pass the window to close

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(896, 905)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"#base{\n"
"	background-image: url(:/fondos/img/fondos/fondo.jpg);\n"
"}\n"
"#widget{\n"
"	border-radius:9px;\n"
"}\n"
"#container{\n"
"	border-radius:9px;\n"
"}\n"
"#access_btn{\n"
"	color: rgba(0, 73, 113,255);\n"
"	border: 1px solid rgb(179, 179, 179);\n"
"	border-radius:9px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"#access_btn:pressed{\n"
"	color: rgba(0, 73, 113,225);\n"
"	background-color: rgb(223, 223, 223);\n"
"	border: 1px solid rgba(179, 179, 179,100);\n"
"}\n"
"#register_btn{\n"
"	color: rgba(0, 73, 113,255);\n"
"	border: 1px solid rgb(179, 179, 179);\n"
"	border-radius:9px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"#register_btn:pressed{\n"
"	color: rgba(0, 73, 113,225);\n"
"	background-color: rgb(223, 223, 223);\n"
"	border: 1px solid rgba(179, 179, 179,100);\n"
"}\n"
"QLabel{\n"
"	color: rgb(179, 179, 179);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(179, 179, 179);\n"
"	border: 1px solid rgb(179, 179, 179);\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"	border-radius: "
                        "3px;\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgba(0, 73, 113,255);\n"
"}\n"
"QComboBox:hover{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#pag_login{\n"
"	border-image: url(:/fondos/img/fondos/fondo_sin.jpg);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"#pag_registro{\n"
"\n"
"	border-image: url(:/fondos/img/fondos/fondo_sin.jpg);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"#logToReg{\n"
"	border: none;\n"
"	color: rgb(179, 179, 179);\n"
"}\n"
"\n"
"#regToLogin{\n"
"	border: none;\n"
"	color: rgb(179, 179, 179);\n"
"}\n"
"#selector{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(179, 179, 179);\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"	border-radius: 3px;\n"
"}")
        self.base = QWidget(MainWindow)
        self.base.setObjectName(u"base")
        self.verticalLayout = QVBoxLayout(self.base)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.base)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QWidget(self.widget)
        self.container.setObjectName(u"container")
        self.container.setMinimumSize(QSize(250, 400))
        self.container.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.container)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stack = QStackedWidget(self.container)
        self.stack.setObjectName(u"stack")
        self.pag_login = QWidget()
        self.pag_login.setObjectName(u"pag_login")
        self.verticalLayout_2 = QVBoxLayout(self.pag_login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_15 = QWidget(self.pag_login)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_16 = QLabel(self.widget_15)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setPixmap(QPixmap(u":/iconosWhite/img/iconsAtencion/key-3-64.ico"))
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_16)


        self.verticalLayout_2.addWidget(self.widget_15)

        self.widget_14 = QWidget(self.pag_login)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_13 = QVBoxLayout(self.widget_14)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.label_15 = QLabel(self.widget_14)
        self.label_15.setObjectName(u"label_15")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_13.addWidget(self.label_15)


        self.verticalLayout_2.addWidget(self.widget_14)

        self.widget_16 = QWidget(self.pag_login)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_14 = QVBoxLayout(self.widget_16)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 0, 10, 0)
        self.label_17 = QLabel(self.widget_16)
        self.label_17.setObjectName(u"label_17")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_17)

        self.userLogin = QLineEdit(self.widget_16)
        self.userLogin.setObjectName(u"userLogin")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userLogin.sizePolicy().hasHeightForWidth())
        self.userLogin.setSizePolicy(sizePolicy)
        self.userLogin.setMinimumSize(QSize(200, 24))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.userLogin.setFont(font3)
        self.userLogin.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.userLogin, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.pag_login)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_15 = QVBoxLayout(self.widget_17)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 0, 10, 0)
        self.label_18 = QLabel(self.widget_17)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_18)

        self.passLogin = QLineEdit(self.widget_17)
        self.passLogin.setObjectName(u"passLogin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.passLogin.sizePolicy().hasHeightForWidth())
        self.passLogin.setSizePolicy(sizePolicy1)
        self.passLogin.setMinimumSize(QSize(200, 24))
        self.passLogin.setFont(font)
        self.passLogin.setEchoMode(QLineEdit.Password)
        self.passLogin.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.passLogin, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.widget_17)

        self.w_selector = QWidget(self.pag_login)
        self.w_selector.setObjectName(u"w_selector")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.w_selector.sizePolicy().hasHeightForWidth())
        self.w_selector.setSizePolicy(sizePolicy2)
        self.w_selector.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.w_selector)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 26, 0)
        self.label_2 = QLabel(self.w_selector)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.selectorCaja = QComboBox(self.w_selector)
        self.selectorCaja.addItem("")
        self.selectorCaja.addItem("")
        self.selectorCaja.addItem("")
        self.selectorCaja.addItem("")
        self.selectorCaja.setObjectName(u"selectorCaja")
        font5 = QFont()
        font5.setFamilies([u"Arial Black"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.selectorCaja.setFont(font5)
        self.selectorCaja.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_2.addWidget(self.selectorCaja)


        self.verticalLayout_2.addWidget(self.w_selector)

        self.widget_13 = QWidget(self.pag_login)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 90))
        self.verticalLayout_12 = QVBoxLayout(self.widget_13)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, 10, 20, 0)
        self.access_btn = QPushButton(self.widget_13)
        self.access_btn.setObjectName(u"access_btn")
        sizePolicy.setHeightForWidth(self.access_btn.sizePolicy().hasHeightForWidth())
        self.access_btn.setSizePolicy(sizePolicy)
        self.access_btn.setMinimumSize(QSize(190, 36))
        self.access_btn.setFont(font4)

        self.verticalLayout_12.addWidget(self.access_btn, 0, Qt.AlignHCenter)

        self.logToReg = QPushButton(self.widget_13)
        self.logToReg.setObjectName(u"logToReg")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setUnderline(True)
        self.logToReg.setFont(font6)

        self.verticalLayout_12.addWidget(self.logToReg)

        self.label_14 = QLabel(self.widget_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_14)


        self.verticalLayout_2.addWidget(self.widget_13)

        self.stack.addWidget(self.pag_login)
        self.pag_registro = QWidget()
        self.pag_registro.setObjectName(u"pag_registro")
        self.verticalLayout_11 = QVBoxLayout(self.pag_registro)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_9 = QWidget(self.pag_registro)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(22, -1, -1, -1)
        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/iconosWhite/img/iconsAtencion/checked-user-64.ico"))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)


        self.verticalLayout_11.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.pag_registro)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_9 = QVBoxLayout(self.widget_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_11 = QLabel(self.widget_10)
        self.label_11.setObjectName(u"label_11")
        font7 = QFont()
        font7.setPointSize(16)
        font7.setBold(True)
        self.label_11.setFont(font7)
        self.label_11.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.label_11)

        self.label = QLabel(self.widget_10)
        self.label.setObjectName(u"label")
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(True)
        self.label.setFont(font8)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)


        self.verticalLayout_11.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.pag_registro)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_10 = QVBoxLayout(self.widget_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 0, 10, 0)
        self.fullName = QLineEdit(self.widget_11)
        self.fullName.setObjectName(u"fullName")
        sizePolicy.setHeightForWidth(self.fullName.sizePolicy().hasHeightForWidth())
        self.fullName.setSizePolicy(sizePolicy)
        self.fullName.setMinimumSize(QSize(200, 22))
        self.fullName.setFont(font)
        self.fullName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.fullName, 0, Qt.AlignHCenter)

        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font8)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_12)

        self.userRegister = QLineEdit(self.widget_11)
        self.userRegister.setObjectName(u"userRegister")
        sizePolicy.setHeightForWidth(self.userRegister.sizePolicy().hasHeightForWidth())
        self.userRegister.setSizePolicy(sizePolicy)
        self.userRegister.setMinimumSize(QSize(200, 22))
        self.userRegister.setFont(font)
        self.userRegister.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.userRegister, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.widget_11)

        self.widget_8 = QWidget(self.pag_registro)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_8 = QVBoxLayout(self.widget_8)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 0, 10, 6)
        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font8)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_9)

        self.passRegister = QLineEdit(self.widget_8)
        self.passRegister.setObjectName(u"passRegister")
        sizePolicy1.setHeightForWidth(self.passRegister.sizePolicy().hasHeightForWidth())
        self.passRegister.setSizePolicy(sizePolicy1)
        self.passRegister.setMinimumSize(QSize(200, 22))
        self.passRegister.setFont(font)
        self.passRegister.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.passRegister.setEchoMode(QLineEdit.Password)
        self.passRegister.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.passRegister, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font8)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.pass2Register = QLineEdit(self.widget_8)
        self.pass2Register.setObjectName(u"pass2Register")
        sizePolicy.setHeightForWidth(self.pass2Register.sizePolicy().hasHeightForWidth())
        self.pass2Register.setSizePolicy(sizePolicy)
        self.pass2Register.setMinimumSize(QSize(200, 22))
        self.pass2Register.setMaximumSize(QSize(16777215, 16777215))
        self.pass2Register.setFont(font)
        self.pass2Register.setEchoMode(QLineEdit.Password)
        self.pass2Register.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.pass2Register, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.widget_8)

        self.widget_12 = QWidget(self.pag_registro)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 90))
        self.verticalLayout_7 = QVBoxLayout(self.widget_12)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 10, 20, 0)
        self.register_btn = QPushButton(self.widget_12)
        self.register_btn.setObjectName(u"register_btn")
        sizePolicy.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy)
        self.register_btn.setMinimumSize(QSize(190, 36))
        self.register_btn.setFont(font4)

        self.verticalLayout_7.addWidget(self.register_btn, 0, Qt.AlignHCenter)

        self.regToLogin = QPushButton(self.widget_12)
        self.regToLogin.setObjectName(u"regToLogin")
        self.regToLogin.setFont(font6)

        self.verticalLayout_7.addWidget(self.regToLogin)

        self.label_8 = QLabel(self.widget_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.verticalLayout_11.addWidget(self.widget_12)

        self.stack.addWidget(self.pag_registro)

        self.horizontalLayout_3.addWidget(self.stack)


        self.horizontalLayout.addWidget(self.container)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.base)

        self.retranslateUi(MainWindow)

        self.stack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)

        #BUTTONS CONF
        self.logToReg.clicked.connect( lambda: self.stack.setCurrentWidget(self.pag_registro))
        self.regToLogin.clicked.connect( lambda: self.stack.setCurrentWidget(self.pag_login))
        self.access_btn.clicked.connect( lambda: self.startProgram())
        self.register_btn.clicked.connect( lambda: self.registerUser())

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_16.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Acceso atencion \n"
" Ticketera", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Constrase\u00f1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CAJA", None))
        self.selectorCaja.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.selectorCaja.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.selectorCaja.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.selectorCaja.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.access_btn.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.logToReg.setText(QCoreApplication.translate("MainWindow", u"No tienes usuario? Registrarse", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Hospital Sudamericano 2023", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Registro nuevo usuario", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre Completo", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Constrase\u00f1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Confirmar Contrase\u00f1a", None))
        self.register_btn.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.regToLogin.setText(QCoreApplication.translate("MainWindow", u"Ya tienes usuario? Acceder", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hospital Sudamericano 2023", None))
    # retranslateUi

