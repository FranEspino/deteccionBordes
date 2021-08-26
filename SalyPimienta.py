import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

image = cv2.imread("img/coins.png");

def sp_noise(image,prob):
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

img1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
varianza = input("Ingrese la varianza de sal y pimienta 😋: ")
noise_img = sp_noise(img1, float(varianza))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(noise_img,cmap=plt.cm.gray)
plt.title('Con Sal y pimienta')
plt.axis('off')

plt.show()


