import pygame
import sys
import os
from Pantalla_Planeta_3D import Planeta_3D

#Inicializar Pygame
pygame.init()

directorio_imagenes = "Informacion"
Planeta = os.path.join(directorio_imagenes, "Planeta_Marte.png")

def Pantalla_Marte():
    #Dimensiones de la ventana
    ancho, alto = 1280, 720

    #Crear la ventana
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Información del planeta Marte")

    #Carga la imagen de fondo
    imagen_fondo = pygame.image.load(Planeta)

    #Escala la imagen de fondo para que coincida con las dimensiones de la ventana
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ancho, alto))

    #Fuente y texto
    fuente = pygame.font.Font(None, 36)  # Fuente y tamaño del texto
    texto = "Ver en 3D"

    #Coordenadas del texto (parte inferior derecha)
    texto_x = ancho - 150
    texto_y = alto - 150

    #Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Verifica si se hizo clic en el área del texto
                if texto_rect.collidepoint(event.pos):
                    Planeta_3D()

        #Dibuja la imagen de fondo en la ventana
        ventana.blit(imagen_fondo, (0, 0))

        #Dibuja el texto en la parte inferior derecha
        texto_imagen = fuente.render(texto, True, (0, 0, 0))  # Color del texto: blanco
        texto_rect = texto_imagen.get_rect()
        texto_rect.topleft = (texto_x, texto_y)
        ventana.blit(texto_imagen, texto_rect)

        #Actualizar la pantalla
        pygame.display.flip()
