import cv2
import numpy as np
from sympy import im

imag = cv2.imread('img/1.jpg')
h=imag.shape
img = cv2.resize(imag, [int(h[1]/2),int(h[0]/2)])

# Necesitamos trabajar con el espacio de colo HSV
imagen_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Creacion de parametros rojos
rojo_bajo, rojo_alto = np.array([0, 50, 30], np.uint8), np.array([5, 255, 255], np.uint8)
rojo2_bajo, rojo2_alto = np.array([168, 50, 30], np.uint8), np.array([179, 255, 255], np.uint8)

# Creacion de parametros verdes
verde_bajo, verde_alto = np.array([38, 50, 30], np.uint8), np.array([55, 255, 255], np.uint8)
verde2_bajo, verde2_alto = np.array([55, 50, 30], np.uint8), np.array([80, 255, 255], np.uint8)

# Creacion de parametros azules
azul_bajo, azul_alto = np.array([82, 50, 30], np.uint8), np.array([110, 255, 255], np.uint8)
azul2_bajo, azul2_alto = np.array([110, 50, 30], np.uint8), np.array([135, 255, 255], np.uint8)

# Creacion de parametros morado
morado_bajo, morado_alto = np.array([130, 50, 30], np.uint8), np.array([150, 255, 255], np.uint8)
morado2_bajo, morado2_alto = np.array([150, 50, 30], np.uint8), np.array([160, 255, 255], np.uint8)

# Creacion de parametros naranja
naranja_bajo, naranaja_alto = np.array([10, 50, 30], np.uint8), np.array([25, 255, 255], np.uint8)
naranja2_bajo, narajan2_alto = np.array([25, 50, 30], np.uint8), np.array([35, 255, 255], np.uint8)

mask_rojo, mask2_rojo = cv2.inRange(imagen_hsv, rojo_bajo, rojo_alto), cv2.inRange(imagen_hsv, rojo2_bajo, rojo2_alto)
mask_verde, mask2_verde = cv2.inRange(imagen_hsv, verde_bajo, verde_alto), cv2.inRange(imagen_hsv, verde2_bajo, verde2_alto)
mask_azul, mask2_azul = cv2.inRange(imagen_hsv, azul_bajo, azul_alto), cv2.inRange(imagen_hsv, azul2_bajo, azul2_alto)
mask_morado, mask2_morado = cv2.inRange(imagen_hsv, morado_bajo, morado_alto), cv2.inRange(imagen_hsv, morado2_bajo, morado2_alto)
mask_naranja, mask2_naranja = cv2.inRange(imagen_hsv, naranja_bajo, naranaja_alto), cv2.inRange(imagen_hsv, naranja2_bajo, narajan2_alto)

img_rojo = cv2.add(mask_rojo, mask2_rojo)
img_verde = cv2.add(mask_verde, mask2_verde)
img_azul = cv2.add(mask_azul, mask2_azul)
img_morado = cv2.add(mask_morado, mask2_morado)
img_naranja = cv2.add(mask_naranja, mask2_naranja)

color_rojo_img = cv2.bitwise_and(img, img, mask=img_rojo)
color_verde_img = cv2.bitwise_and(img, img, mask=img_verde)
color_azul_img = cv2.bitwise_and(img, img, mask=img_azul)
color_morado_img = cv2.bitwise_and(img, img, mask=img_morado)
color_naranja_img = cv2.bitwise_and(img, img, mask=img_naranja)

cv2.imshow('HSV', np.hstack([img, imagen_hsv]))
cv2.imshow('HSV-BN', np.hstack([img_rojo, img_verde, img_azul, img_morado, img_naranja]))
cv2.imshow('HSV-COLOR', np.hstack([color_rojo_img, color_verde_img, color_azul_img, color_morado_img, color_naranja_img]))
cv2.waitKey(0)
cv2.destroyAllWindows()
