"""
Proyecto de deteccion de figuras geometricas basicas
Author: Grupo UC3M PIC
Date: 02/12/2020
"""

###############################################################
#  Modulos
###############################################################
import cv2
import os
from statistics import mode
import sys

# importar modulos de pyQt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
# importar modulo opencv
import cv2

from main_window import *

###############################################################
# Variables
###############################################################
contador = 0
intentos = []
figuras = ["TRIANGULO","CUADRADO","RECTANGULO","PENTAGONO","EXAGONO","CIRCULO"]
nomAux = "Nada"
#NombreFigura = "Nada"

def test():
    print("Get Figure name")

class MainWindow(QWidget):
    # clase constructor
    def __init__(self):
        # llama a QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # crear un timer
        self.timer = QTimer()
        self.NombreFigura = "Nada"
        
        # llamar a funcion viewCam cada vez que termina temporizar
        self.timer.timeout.connect(self.viewCam)
        
        # set control_bt callback clicked  function
        self.ui.btnIniciar.clicked.connect(self.controlTimer)

    # Ver camara
    
    def viewCam(self):
        # read image in BGR format
        _, image = self.cap.read()
        #Conversion a Escala de Grises
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
        #Aplicando filtros
        gray = cv2.GaussianBlur(gray,(3,3),0)
        edged = cv2.Canny(gray,50,150)
        edged = cv2.dilate(edged, None, iterations=1)
        edged = cv2.erode(edged, None, iterations=1)
        
        #Operaciones Morfologicas Cierre
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        closed = cv2.morphologyEx(edged,cv2.MORPH_CLOSE,kernel,iterations=3)

        #cv2.imshow("Closed",closed)
        #Encontrar contornos
        _,cnts,_= cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #_,cnts,_= cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for c in cnts:
            epsilon = 0.01*cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)
            x,y,w,h = cv2.boundingRect(approx)
            area = cv2.contourArea(c)
            if(area>1600):
                if len(approx)==3:
                    cv2.drawContours(image, [approx], 0, (0,255,0),2)
                    intentos.append(0)
                    
                if len(approx)==4:
                    cv2.drawContours(image, [approx], 0, (0,255,0),2)
                    aspect_ratio = float(w)/h
                    if aspect_ratio == 1:
                        intentos.append(1)
                    else:
                        intentos.append(2)
                    
                if len(approx)==5:
                    intentos.append(3)
                    cv2.drawContours(image, [approx], 0, (0,255,0),2)
                
                if len(approx)==6:
                    intentos.append(4)
                    cv2.drawContours(image, [approx], 0, (0,255,0),2)
                
                if len(approx)>10:
                    intentos.append(5)
                    cv2.drawContours(image, [approx], 0, (0,255,0),2)
                    
            if(len(intentos) >=12):
                #print("Figura detectada")
                try:
                    self.NombreFigura = figuras[mode(intentos)]
                    #break
                except Exception:
                    #print("Error estadistico")
                    pass
                intentos[:] = []
        
        self.ui.lblResultado.setText(self.NombreFigura)
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
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(1)
            # update control_bt text
            self.ui.btnIniciar.setText("PARAR")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.btnIniciar.setText("EMPEZAR")

test()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())