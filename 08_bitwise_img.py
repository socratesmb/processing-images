import cv2
import numpy as np

imag = cv2.imread('img/1.jpg')
h = imag.shape
img = cv2.resize(imag, [int(h[1]/2), int(h[0]/2)])

# Separacion en rgb
r = img[:, :, 0]  # Rojo
g = img[:, :, 1]  # Verde
b = img[:, :, 2]  # Azul

cv2.imshow('RGB', np.hstack([r, g, b]))

# thresholdin para cada espectro de color
_, thres_r = cv2.threshold(r, 50, 255, cv2.THRESH_BINARY)
_, thres_g = cv2.threshold(g, 50, 255, cv2.THRESH_BINARY)
_, thres_b = cv2.threshold(b, 50, 255, cv2.THRESH_BINARY)

cv2.imshow('THR-RGB', np.hstack([thres_r, thres_g, thres_b]))

# Para unir imagenes estas deben estar binarizadas
img_and = cv2.bitwise_and(thres_r, thres_b)
img_or = cv2.bitwise_or(thres_r, thres_b)
img_not = cv2.bitwise_not(thres_r, thres_b)
img_xor = cv2.bitwise_xor(thres_r, thres_b)

cv2.imshow('AND', img_and)
cv2.imshow('OR', img_or)
cv2.imshow('NOT', img_not)
cv2.imshow('X-OR', img_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()
