"""
Proyecto de deteccion de figuras geometricas basicas
Author: Grupo UC3M PIC
Date: 02/12/2020
"""

# IMPORTAR MODULOS DE PYQT PARA LA INTERFACE GRAFICA
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
# IMPORTAR LOS CODIGOS GENERAMOS POR QT DESIGNER 
from Main_UI import *
# IMPORTAR MODULO DETECCION DE FIGURA CREADO
from figura import *

import random

class MainWindow(QWidget):
    # clase constructor
    def __init__(self):
        # llama a QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.tipo ="aprender"
        # crear un timer
        self.timer = QTimer()
        self.NombreFigura = "No hay Figura"
        
        # llamar a funcion viewCam cada vez que termina temporizar
        self.timer.timeout.connect(self.viewCam)
        
        # set control_bt callback clicked  function
        self.ui.btnIniciar.clicked.connect(self.controlTimer)
        
        self.ui.btnInt1.clicked.connect(self.Intento1)
        self.ui.btnInt2.clicked.connect(self.Intento2)
        self.ui.btnInt3.clicked.connect(self.Intento3)
        
        self.ui.btnInt1.setEnabled(False)
        self.ui.btnInt2.setEnabled(False)
        self.ui.btnInt3.setEnabled(False)
        self.intentos =0
        self.valor = 0
        self.puntaje = 0
           
        
    # Ver camara
    def viewCam(self):
        #test()
        # read image in BGR format
        _, image = self.cap.read()
        
        self.NombreFigura = getFigureName(image)
        #print(self.NombreFigura)
        if self.NombreFigura!= "No hay Figura" and self.tipo=="adivinar": 
            self.timer.stop()
            # release video capture
            #self.cap.release()
            #print(self.NombreFigura)
            self.valor = random.randint(1, 3)
            self.intentos +=1
            if self.intentos == 1:
                if self.valor == 1:
                    self.ui.rbInt1op1.setText(self.NombreFigura)
                    figNameInt1op2,figNameInt1op3 = getFigureRandom(self.NombreFigura,1)
                    self.ui.rbInt1op2.setText(figNameInt1op2)
                    self.ui.rbInt1op3.setText(figNameInt1op3)
                    
                if self.valor == 2:
                    self.ui.rbInt1op2.setText(self.NombreFigura)
                    figNameInt1op1,figNameInt1op3 = getFigureRandom(self.NombreFigura,2)
                    self.ui.rbInt1op1.setText(figNameInt1op1)
                    self.ui.rbInt1op3.setText(figNameInt1op3)
                    
                if self.valor == 3:
                    self.ui.rbInt1op3.setText(self.NombreFigura)
                    figNameInt1op2,figNameInt1op1 = getFigureRandom(self.NombreFigura,3)
                    self.ui.rbInt1op2.setText(figNameInt1op2)
                    self.ui.rbInt1op1.setText(figNameInt1op1)
                    
            if self.intentos == 2:
                if self.valor == 1:
                    self.ui.rbInt2op1.setText(self.NombreFigura)
                    figNameInt2op2,figNameInt2op3 = getFigureRandom(self.NombreFigura,1)
                    self.ui.rbInt2op2.setText(figNameInt2op2)
                    self.ui.rbInt2op3.setText(figNameInt2op3)
                    
                if self.valor == 2:
                    self.ui.rbInt2op2.setText(self.NombreFigura)
                    figNameInt2op1,figNameInt2op3 = getFigureRandom(self.NombreFigura,2)
                    self.ui.rbInt2op1.setText(figNameInt2op1)
                    self.ui.rbInt2op3.setText(figNameInt2op3)
                
                if self.valor == 3:
                    self.ui.rbInt2op3.setText(self.NombreFigura)
                    figNameInt2op2,figNameInt2op1 = getFigureRandom(self.NombreFigura,3)
                    self.ui.rbInt2op2.setText(figNameInt2op2)
                    self.ui.rbInt1op1.setText(figNameInt2op1)
            if self.intentos == 3:
                if self.valor == 1:
                    self.ui.rbInt3op1.setText(self.NombreFigura)
                    figNameInt3op2,figNameInt3op3 = getFigureRandom(self.NombreFigura,1)
                    self.ui.rbInt3op2.setText(figNameInt3op2)
                    self.ui.rbInt3op3.setText(figNameInt3op3)
                
                if self.valor == 2:
                    self.ui.rbInt3op2.setText(self.NombreFigura)
                    figNameInt3op1,figNameInt3op3 = getFigureRandom(self.NombreFigura,2)
                    self.ui.rbInt3op1.setText(figNameInt3op1.lower())
                    self.ui.rbInt3op3.setText(figNameInt3op3.lower())
                
                if self.valor == 3:
                    self.ui.rbInt3op3.setText(self.NombreFigura)
                    figNameInt3op2,figNameInt3op1 = getFigureRandom(self.NombreFigura,3)
                    self.ui.rbInt3op2.setText(figNameInt3op2.lower())
                    self.ui.rbInt3op1.setText(figNameInt3op1.lower())
                print(figNameInt2op1+" - "+ figNameInt2op2+" - "+figNameInt2op3)
        if self.tipo == "aprender" and self.NombreFigura != "No hay Figura":
            self.ui.lblResultadoA.setText(self.NombreFigura)    
        # convert image to RGB format
        imagenEscalada = cv2.resize(image,(640,480), interpolation=cv2.INTER_CUBIC)
        image = cv2.cvtColor(imagenEscalada, cv2.COLOR_BGR2RGB)
        
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        
        # create QImage from image
        qImg = QImage(imagenEscalada.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.lblCamara.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        self.ui.lblResultadoB.setText("**********")
        self.ui.lblResultadoA.setText("**********")
        if self.ui.rbAprender.isChecked():
            self.tipo ="aprender"
            
        if self.ui.rbAdivinar.isChecked():
            self.tipo ="adivinar"
            self.ui.btnInt1.setEnabled(True)
            
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(0)
            # update control_bt text
            self.ui.btnIniciar.setText("PARAR - REINICIAR")
        # if timer is started
        else:
            self.ui.btnInt1.setEnabled(False)
            self.ui.btnInt2.setEnabled(False)
            self.ui.btnInt3.setEnabled(False)
            self.intentos = 0;
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.btnIniciar.setText("EMPEZAR")

    def Intento1(self):
        self.ui.btnInt1.setEnabled(False)
        self.ui.btnInt2.setEnabled(True)
        if self.valor == 1 and self.ui.rbInt1op1.isChecked():
            self.puntaje += 1
        if self.valor == 2 and self.ui.rbInt1op2.isChecked():
            self.puntaje += 1
        if self.valor == 3 and self.ui.rbInt1op3.isChecked():
            self.puntaje += 1
        
        self.timer.start(0)
        
    def Intento2(self):
        self.ui.btnInt2.setEnabled(False)
        self.ui.btnInt3.setEnabled(True)
        if self.valor == 1 and self.ui.rbInt2op1.isChecked():
            self.puntaje += 1
        if self.valor == 2 and self.ui.rbInt2op2.isChecked():
            self.puntaje += 1
        if self.valor == 3 and self.ui.rbInt2op3.isChecked():
            self.puntaje += 1
        
        self.timer.start(0)
    
    def Intento3(self):
        self.ui.btnInt3.setEnabled(False)
        
        if self.valor == 1 and self.ui.rbInt3op1.isChecked():
            self.puntaje += 1
        if self.valor == 2 and self.ui.rbInt3op2.isChecked():
            self.puntaje += 1
        if self.valor == 3 and self.ui.rbInt3op3.isChecked():
            self.puntaje += 1
        #print("Resultado: "+str(self.puntaje))
        if self.puntaje == 3:
            self.ui.lblResultadoB.setText("Excelente Intento 3 de 3")
        if self.puntaje == 2:
            self.ui.lblResultadoB.setText("Buen Intento 2 de 3")
        if self.puntaje == 1:
            self.ui.lblResultadoB.setText("Intento Regular 1 de 3")
        if self.puntaje == 0:
            self.ui.lblResultadoB.setText("Sigue Aprendiendo 0 de 3")
        
        self.intentos = 0
        self.puntaje = 0
        
        #print("Result")
        #self.ui.btnInt2.setEnabled(True)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()
    
    sys.exit(app.exec_())
    