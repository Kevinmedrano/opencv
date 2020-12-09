# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:00:50 2020

@author: Kevin
"""
###############################################################
#  Modulos
###############################################################
import cv2
import os
from statistics import mode
import sys


###############################################################
# Variables
###############################################################
contador = 0
intentos = []
figuras = ["Triangulo","Cuadrado","Rectangulo","Pentagono","Exagono","Circulo"]
# Matrices para seleccion alternativos de posibles respuestas para opcion adivinar
ListTriangulo = [["Cuadrado","Circulo"],
                 ["Rectangulo","Pentagono"],
                 ["Exagono","Cuadrado"]]

ListCuadrado = [["Rriangulo","Rectangulo"],
                ["Pentagono","Exagono"],
                ["Circulo","Triangulo"]]

ListRectangulo = [["Cuadrado","Circulo"],
                 ["Rectangulo","Pentagono"],
                 ["Exagono","Cuadrado"]]

ListPentagono = [["Triangulo","Cuadrado"],
                 ["Rectangulo","Exagono"],
                 ["Circulo","Triangulo"]]

ListExagono = [["Circulo","Pentagono"],
                 ["Rectangulo","Cuadrado"],
                 ["Triangulo","Circulo"]]

ListCirculo = [["Cuadrado","Triangulo"],
                 ["Rectangulo","Cuadrado"],
                 ["Exagono","Pentagono"]]

def getFigureName(image):
    figura_name = "No hay Figura"
    # CONVERSION A ESCALA DE GRISES
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # APLICAMOS FILTRO GAUSSIANO
    gray = cv2.GaussianBlur(gray,(3,3),0)
    # APLICAMOS DETECCION DE BORDES CON CANNY
    edged = cv2.Canny(gray,50,150)
    # FILTRO PARA MEJORAR LA IMAGEN BINARIA DE BORDES CON DILATE Y ERODE
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    # FILTRO OPERACIONES MORFOLOGICAS CIERRE
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    # OBTENCION DE CONTORNOS CERRADOS - CONECTADOS
    closed = cv2.morphologyEx(edged,cv2.MORPH_CLOSE,kernel,iterations=3)

    # ENCONTRAR CONTORNOS
    _,cnts,_= cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #OPENCV3
    #_,cnts,_= cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #OPENCV4
    
    # ANALIZAR LOS CONTORNOS ENCONTRADOS
    for c in cnts:
        # CALCULAR LA PRESION DE APROXIMACION MEDIANTE EL PERIMETRO DEL CONTORNO ENCONTRADO
        epsilon = 0.01*cv2.arcLength(c,True)
        # DETERMINAR EL NUMERO DE VERTICES
        approx = cv2.approxPolyDP(c,epsilon,True)
        # DETERMINAR DIMENSION ANCHO - ALTO Y PUNTOS X Y DEL CONTORNO
        x,y,w,h = cv2.boundingRect(approx)
        # DETERMINAR EL AREA DEL CONTORNO PARA DESPRECIAR DETERMINADOS TAMAÑOS NO DESEADOS
        area = cv2.contourArea(c)
        if(area>1700):
            if len(approx)==3:
                # DIBUJAR EL CONTORNO ENCONTRADO
                cv2.drawContours(image, [approx], 0, (0,255,0),2)
                # SE AGREGA EL INDICE DE LA FIGURA QUE CORRESPONDE
                intentos.append(0)
                
            if len(approx)==4:
                cv2.drawContours(image, [approx], 0, (0,255,0),2)
                # PARA EL CASO DEL CUADRADO Y RECTANGULO CON EL MISMO NUMERO DE VERTICES
                aspect_ratio = float(w)/h # SI LA DIVISION RESULTANTE ES 1 UNA FIGURA CUADRADA
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
        # SE VERIFICA 10 CAPTURAS DE DETECCION DE FIGURAS PARA MEJORAR LA PROBABILIDAD DE ACIERTO        
        if(len(intentos) >= 12):
            # CONTROL DE SECEPCION PARA EVITAR EL CIERRE DE LA APLICACION
            try:
                # APLICANDO LA MODA Y OBTENCION DEL NOMBRE DE LA FIGURA DE LA LISTA
                figura_name = figuras[mode(intentos)]
            except Exception:
                pass
            # LIMPIAMOS LOS INTENTOS DE DETECCION
            intentos[:] = []
    # RETORNAMOS EL NOMBRE DE LA FIGURA EN CASO DE SER ENCONTRADO UNA
    return figura_name

def getFigureRandom(lastFigure,valor):
    if lastFigure == "Triangulo":
        return ListTriangulo[valor-1][0], ListTriangulo[valor-1][1]
    if lastFigure == "Cuadrado":
        return ListCuadrado[valor-1][0], ListCuadrado[valor-1][1]
    if lastFigure == "Rectangulo":
        return ListRectangulo[valor-1][0], ListRectangulo[valor-1][1]
    if lastFigure == "Pentagono":
        return ListPentagono[valor-1][0], ListPentagono[valor-1][1]
    if lastFigure == "Exagono":
        return ListExagono[valor-1][0], ListExagono[valor-1][1]
    if lastFigure == "Circulo":
        return ListCirculo[valor-1][0], ListCirculo[valor-1][1]
    
    