import cv2

imagen = cv2.imread('img/perro-samurai.jpg') # Leer una imagen

#cv2.imwrite('perro-samurai-gris.jpg', imagen) # Guardar imagen

# Visualizar imange
cv2.imshow('Test de salida', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
