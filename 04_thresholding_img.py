import cv2
import numpy as np

# Importe de imagen y conversion a gris
img = cv2.imread('img/1.jpg', 0)

d = img.shape # Obtener ancho y alto de imagen

h = int(d[1]/2) # Nueva altura
w = int(d[0]/2) # Nueva anchura
image = cv2.resize(img, (h, w)) # Redimension de imagen

# Creacion de umbralizacion de imagen
_,white_bit = cv2.threshold(image, 75, 255, cv2.THRESH_BINARY)
_,black_bit = cv2.threshold(image, 75, 255, cv2.THRESH_BINARY_INV)
_,trian_bit = cv2.threshold(image, 75, 255, cv2.THRESH_TRIANGLE)
_,binari_bit = cv2.threshold(image, 75, 255, cv2.THRESH_BINARY)
_,binari_inv_bit = cv2.threshold(image, 75, 255, cv2.THRESH_BINARY_INV)
_,tozero_bit = cv2.threshold(image, 75, 255, cv2.THRESH_TOZERO)
_,tozero_inv_bit = cv2.threshold(image, 75, 255, cv2.THRESH_TOZERO_INV)
_,mask_bit = cv2.threshold(image, 75, 255, cv2.THRESH_MASK)
_,otsu_bit = cv2.threshold(image, 75, 255, cv2.THRESH_OTSU)


#cv2.imshow('ORG-IMG', img)
#cv2.imshow('MOD-IMG', image)
cv2.imshow('IMG BIN - BININV', np.hstack([image, white_bit, black_bit, trian_bit, binari_bit, binari_inv_bit, tozero_bit, tozero_inv_bit, mask_bit, otsu_bit]))

cv2.waitKey(0)
cv2.destroyAllWindows()