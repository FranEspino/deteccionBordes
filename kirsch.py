
# Filtrado de convolución personalizado
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar imagen
image = cv2.imread('_lena.png', 0)
image = cv2.resize(image, (800, 800))

# Operador de detección de bordes de Kirsch

m, n = image.shape
list = []
kirsch = np.zeros((m, n))
for i in range(2, m-1):
    for j in range(2, n-1):
        d1 = np.square(5 * image[i - 1, j - 1] + 5 * image[i - 1, j] + 5 * image[i - 1, j + 1] -
                       3 * image[i, j - 1] - 3 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
                       3 * image[i + 1, j] - 3 * image[i + 1, j + 1])
        d2 = np.square((-3) * image[i - 1, j - 1] + 5 * image[i - 1, j] + 5 * image[i - 1, j + 1] -
                       3 * image[i, j - 1] + 5 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
                       3 * image[i + 1, j] - 3 * image[i + 1, j + 1])
        d3 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] + 5 * image[i - 1, j + 1] -
                       3 * image[i, j - 1] + 5 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
                       3 * image[i + 1, j] + 5 * image[i + 1, j + 1])
        d4 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] -
                       3 * image[i, j - 1] + 5 * image[i, j + 1] - 3 * image[i + 1, j - 1] +
                       5 * image[i + 1, j] + 5 * image[i + 1, j + 1])
        d5 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] - 3
                       * image[i, j - 1] - 3 * image[i, j + 1] + 5 * image[i + 1, j - 1] +
                       5 * image[i + 1, j] + 5 * image[i + 1, j + 1])
        d6 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] +
                       5 * image[i, j - 1] - 3 * image[i, j + 1] + 5 * image[i + 1, j - 1] +
                       5 * image[i + 1, j] - 3 * image[i + 1, j + 1])
        d7 = np.square(5 * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] +
                       5 * image[i, j - 1] - 3 * image[i, j + 1] + 5 * image[i + 1, j - 1] -
                       3 * image[i + 1, j] - 3 * image[i + 1, j + 1])

        # El primer método: tome el valor máximo en todas las direcciones, el efecto no es bueno, use otro método
        list = [d1, d2, d3, d4, d5, d6, d7]
        kirsch[i, j] = np.max(list)
        # El segundo método: redondear el módulo en todas las direcciones
        #kirsch[i, j] =int(np.sqrt(d1+d2+d3+d4+d5+d6+d7+d8))


plt.subplot(1, 2, 1)
plt.imshow(image, cmap=plt.cm.gray)
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(kirsch, cmap=plt.cm.gray)
plt.title('Método de Prewitt')
plt.axis('off')


plt.show()
