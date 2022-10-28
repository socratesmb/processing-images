import cv2
import numpy as np

# Importe de imagen y conversion a gris
img = cv2.imread('img/5.jpg', 0)

d = img.shape # Obtener ancho y alto de imagen

image = cv2.resize(img, (int(d[1]/2), int(d[0]/2))) # Redimension de imagen

# Creacion de umbralizacion de imagen
_,thre1 = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
_,thre2 = cv2.threshold(image, 70, 255, cv2.THRESH_BINARY)
_,thre3 = cv2.threshold(image, 90, 255, cv2.THRESH_BINARY)

#region Otros Filtros
'''
_,black_bit = cv2.threshold(image, 75, 255, cv2.THRESH_BINARY_INV)
_,trian_bit = cv2.threshold(image, 75, 255, cv2.THRESH_TRIANGLE)
_,binari_bit = cv2.threshold(image, 75, 255, cv2.THRESH_BINARY)
_,binari_inv_bit = cv2.threshold(image, 75, 255, cv2.THRESH_BINARY_INV)
_,tozero_bit = cv2.threshold(image, 75, 255, cv2.THRESH_TOZERO)
_,tozero_inv_bit = cv2.threshold(image, 75, 255, cv2.THRESH_TOZERO_INV)
_,mask_bit = cv2.threshold(image, 75, 255, cv2.THRESH_MASK)
_,otsu_bit = cv2.threshold(image, 75, 255, cv2.THRESH_OTSU)'''
#endregion


#cv2.imshow('ORG-IMG', img)
#cv2.imshow('MOD-IMG', image)
cv2.imshow('IMG BIN - BININV', np.hstack([image, thre1, thre2, thre3]))

cv2.waitKey(0)
cv2.destroyAllWindows()