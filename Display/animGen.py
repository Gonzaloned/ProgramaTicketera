'''def animationListGenerator(self, listBox: [QWidget]):#, listNum: [QLabel], listCaja: [QLabel]): 
    #https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsEffect.html
    self.animationList = []
    for elem in listBox:
        act=QGraphicsColorizeEffect(elem) #Create a new QGraphicsOpacityEffect with the Qobject
        act.setStrength(0)  #Set color streght of the effect
        act.setColor(QColor(0,73,113)) #BLUE
        elem.setGraphicsEffect(act) #Assign the effect to elem
        anim = QPropertyAnimation(act, b'strength') #Create the animation of the effect
        anim.setStartValue(0)
        anim.setDuration(5000)#Duration to colorize
        anim.setEndValue(1)
        self.animationList.append(anim)  #Add the effect to the temporal list            

'''