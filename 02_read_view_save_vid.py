import cv2
'''
# region Usar camara del dispositivo
video = cv2.VideoCapture(0)

while(video.isOpened()):
    estado, imagen = video.read()
    if estado == True:
        cv2.imshow('video', imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        
cv2.destroyAllWindows()

# endregion
'''

'''
# region Grabar Video y Guardarlo
video = cv2.VideoCapture(0)
salida = cv2.VideoWriter('vid/VideoTest.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (640,480))

while(video.isOpened()):
    estado, imagen = video.read()
    if estado == True:
        cv2.imshow('video', imagen)
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

        
cv2.destroyAllWindows()
# endregion
'''


# region Cargar video para ver
video = cv2.VideoCapture('vid/VideoTest.mp4')

while(video.isOpened()):
    estado, imagen = video.read()
    if estado == True:
        cv2.imshow('video', imagen)
        if cv2.waitKey(30) & 0xFF == ord('s'):
            break

video.release()        
cv2.destroyAllWindows()
# endregion

