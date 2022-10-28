import cv2
import numpy as np

img = cv2.imread('img/1.jpg')
h = img.shape
image = cv2.resize(img, [int(h[1]/2), int(h[0]/2)])

imagen_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

rojo_bajo, rojo_alto = np.array(
    [0, 50, 30], np.uint8), np.array([5, 255, 255], np.uint8)
rojo2_bajo, rojo2_alto = np.array(
    [168, 50, 30], np.uint8), np.array([179, 255, 255], np.uint8)

mask_rojo, mask2_rojo = cv2.inRange(imagen_hsv, rojo_bajo, rojo_alto), cv2.inRange(
    imagen_hsv, rojo2_bajo, rojo2_alto)

img_rojo = cv2.add(mask_rojo, mask2_rojo)

contorno, _ = cv2.findContours(
    img_rojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujo de contorno de todo
# cv2.drawContours(image, contorno, -1, (0, 0, 255), 1)

# Dibujo de contorno por tamaño de area
for i in contorno:
    a = cv2.contourArea(i)
    if a > 20:
        nc=cv2.convexHull(i) # Para crear una zona general
        cv2.drawContours(image, [i], 0, (0, 0, 255), 1)

cv2.imshow('IMG', image)
cv2.imshow('IMG-BIT', img_rojo)

cv2.waitKey(0)
cv2.destroyAllWindows()