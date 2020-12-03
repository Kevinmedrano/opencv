# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:35:48 2020

@author: Kevin
"""

###############################################################
#  Modulos
###############################################################
import cv2
import os
from statistics import mode


###############################################################
# Variables
###############################################################
contador = 0
intentos = []
figuras = ["TRIANGULO","CUADRADO","RECTANGULO","PENTAGONO","EXAGONO","CIRCULO"]
figura_detectado = False
nomAux = "Nada"
NombreFigura = ""
#creamos el objeto de video (camara)
captura = cv2.VideoCapture(0) 

#audio introductorio
#os.system("mp3 intro.mp3")
while True:
        #capturamos frame a frame
        (grabbed,image) = captura.read()
        #si hemos llegado al final del video salimos
        if not grabbed:
            break
        
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

        cv2.imshow("Closed",closed)
        #Encontrar contornos
        _,cnts,_= cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #_,cnts,_= cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #print "contornos",len(cnts)
        figura_detectado = False
        
        for c in cnts:
                
            epsilon = 0.01*cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)
            x,y,w,h = cv2.boundingRect(approx)
            area = cv2.contourArea(c)
            if(area>1600):
                if len(approx)==3:
                    cv2.drawContours(image, [approx], 0, (0,255,0),2)
                    figura_detectado = True
                    intentos.append(0)
                    
                if len(approx)==4:
                    cv2.drawContours(image, [approx], 0, (0,255,0),2)
                    figura_detectado = True
                    aspect_ratio = float(w)/h
                    if aspect_ratio == 1:
                        intentos.append(1)
                    else:
                        intentos.append(2)
                    
                if len(approx)==5:
                    figura_detectado = True
                    intentos.append(3)
                    cv2.drawContours(image, [approx], 0, (0,255,0),2)
                
                if len(approx)==6:
                    figura_detectado = True
                    intentos.append(4)
                    cv2.drawContours(image, [approx], 0, (0,255,0),2)
                
                if len(approx)>10:
                    figura_detectado = True
                    intentos.append(5)
                    cv2.drawContours(image, [approx], 0, (0,255,0),2)
                    
            if(len(intentos) >=12):
                #print("Figura detectada")
                try:
                    NombreFigura = figuras[mode(intentos)]
                    #break
                except Exception:
                    print("Error estadistico")

                figura_detectado = True
                intentos[:] = []
                print(NombreFigura)
            cv2.putText(image,NombreFigura, (150,100),1,1.5,(0,255,0),2)
        
        #Mostramos imagen
        imagenEscalada = cv2.resize(image,(600,400), interpolation=cv2.INTER_CUBIC)
        cv2.imshow("video", imagenEscalada)
        #capturamos teclado
        tecla=cv2.waitKey(25) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla== 27:
            break

#Liberamos Objeto
captura.release()

#Destruimos Ventanas
cv2.destroyAllWindows()