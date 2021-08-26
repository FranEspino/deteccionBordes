import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
image = cv2.imread('_lena.png',0)

def AplicarRuido(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

grayImage = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
varianza = input("Ingrese la varianza de sal y pimienta 😋: ")
noise_img = AplicarRuido(image, float(varianza))
#Convertir la imagen a escala de grises

kernel_Sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]])
kernel_Sobel_y = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]])
#Aplicar el filtro sobel
x = cv2.filter2D(noise_img, cv2.CV_16S, kernel_Sobel_x) #Aplicar el filtro en x 
y = cv2.filter2D(noise_img, cv2.CV_16S, kernel_Sobel_y) #Aplicar el filtro en y
#Convertir a 8 bits para su posterior visualización 
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

#Aplicar una máscara de 0.5 para que se vea mejor
sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0) 

#Mostrar las imágenes
plt.subplot(1, 2, 1)
plt.imshow(noise_img, cmap=plt.cm.gray)
plt.title('Imagen con ruido')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sobel, cmap=plt.cm.gray)
plt.title('Sobel con ruido')
plt.axis('off')
plt.show()