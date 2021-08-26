import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('_lena.png',0)
#Convertir la imagen a escala de grises
grayImage = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
kernel_Roberts_x = np.array([
    [1, 0],
    [0, -1]
    ])
kernel_Roberts_y = np.array([
    [0, -1],
    [1, 0]
    ])
#Aplicar el filtro Roberts
x = cv2.filter2D(grayImage, cv2.CV_16S, kernel_Roberts_x) #Aplicar el filtro en x 
y = cv2.filter2D(grayImage, cv2.CV_16S, kernel_Roberts_y) #Aplicar el filtro en y
#Convertir a 8 bits para su posterior visualización 
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

#Aplicar una máscara de 0.5 para que se vea mejor
Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0) 

#Mostrar las imágenes
plt.subplot(1, 2, 1)
plt.imshow(grayImage, cmap=plt.cm.gray)
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(Roberts, cmap=plt.cm.gray)
plt.title('Método de Roberts')
plt.axis('off')


plt.show()