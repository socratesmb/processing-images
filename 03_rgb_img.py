import cv2
import numpy as np

bgr = cv2.imread('img/perro-samurai.jpg')

r = bgr[:,:,0] # Rojo
g = bgr[:,:,1] # Verde
b = bgr[:,:,2] # Azul

cv2.imshow('BGR', np.hstack([r,g,b]))

color = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

r = color[:,:,0] # Rojo
g = color[:,:,1] # Verde
b = color[:,:,2] # Azul

cv2.imshow('RGB', np.hstack([r,g,b]))

gris = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

cv2.imshow('GRIS', gris)

cv2.waitKey(0)
cv2.destroyAllWindows()