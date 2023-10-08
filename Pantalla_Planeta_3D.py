import cv2
import os

def Planeta_3D():
    #Crea un objeto VideoCapture para cargar el video
    directorio_imagenes = "Recursos_3D"
    Video = os.path.join(directorio_imagenes, "Marte.mp4")
    cap = cv2.VideoCapture(Video)

    #Lee el primer frame del video para obtener las dimensiones
    ret, frame = cap.read()
    if not ret:
        raise Exception("No se pudo abrir el video")

    #Configura las dimensiones de la ventana
    ventana_ancho = frame.shape[1]
    ventana_alto = frame.shape[0]
    ventana = cv2.namedWindow("Video de fondo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Video de fondo", ventana_ancho, ventana_alto)

    while True:
        #Lee un frame del video
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        #Muestra el frame en la ventana
        cv2.imshow("Video de fondo", frame)

        #Presiona 'q' para salir del bucle
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    #Libera el objeto VideoCapture y cierra la ventana
    cap.release()
    cv2.destroyAllWindows()
