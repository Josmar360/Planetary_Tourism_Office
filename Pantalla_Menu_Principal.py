import pygame
import sys
import os
from Pantalla_Carga import Pantalla_Carga
from Pantalla_Menu_Marte import Pantalla_Menu_Marte

def Pantalla_Menu_Principal():
    # Inicializa Pygame
    pygame.init()

    # Configura la pantalla
    screen_width, screen_height = 1280, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Selección de Planetas")

    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Fuente para el texto
    font = pygame.font.Font(None, 80)

    # Texto del título
    titulo = font.render("Selección de Planetas", True, WHITE)
    titulo_rect = titulo.get_rect(center=(screen_width // 2, 80))

    # Lista de opciones de planetas con imágenes
    directorio_imagenes = "Recursos_Visuales/"

    # Cargar la imagen de fondo
    fondo = pygame.image.load(os.path.join(directorio_imagenes, "Fondo_Espacio.jpg"))
    fondo = pygame.transform.scale(fondo, (screen_width, screen_height))

    planetas = [(directorio_imagenes + "Sol.png", "Sol"),  
                (directorio_imagenes + "Mercurio.png", "Mercurio"), 
                (directorio_imagenes + "Venus.png", "Venus"), 
                (directorio_imagenes + "Tierra.png", "Tierra"), 
                (directorio_imagenes + "Luna.png", "Luna"), 
                (directorio_imagenes + "Marte.png", "Marte"), 
                (directorio_imagenes + "Jupiter.png", "Jupiter"), 
                (directorio_imagenes + "Saturno.png", "Saturno"), 
                (directorio_imagenes + "Urano.png", "Urano"), 
                (directorio_imagenes + "Neptuno.png", "Neptuno"), 
                (directorio_imagenes + "Pluton.png", "Pluton")]

    # Redimensionar las imágenes a 145x145 píxeles
    imagenes_planetas = {}
    x_position = 100  # Posición horizontal inicial para la primera fila
    y_position = 150  # Posición vertical inicial para la primera fila
    for ruta_imagen, nombre_planeta in planetas:
        imagen_planeta = pygame.image.load(ruta_imagen)
        imagen_planeta = pygame.transform.scale(imagen_planeta, (145, 145))
        imagenes_planetas[nombre_planeta] = (imagen_planeta, x_position, y_position)  # Almacenar la posición de la imagen
        x_position += 200  # Espacio horizontal entre planetas
        if x_position >= 1000:  # Si supera cierto valor horizontal, empieza en la siguiente fila
            x_position = 100
            y_position += 200  # Espacio vertical entre filas

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for nombre_planeta, (imagen_planeta, imagen_x_position, imagen_y_position) in imagenes_planetas.items():
                    imagen_rect = imagen_planeta.get_rect()
                    imagen_rect.topleft = (imagen_x_position, imagen_y_position)
                    if imagen_rect.collidepoint(x, y):
                        planeta_seleccionado = nombre_planeta
                        if planeta_seleccionado == "Sol":
                            Pantalla_Carga()
                            #Mostrar_Menu_Marte()
                        elif planeta_seleccionado == "Mercurio":
                            Pantalla_Carga()
                            #Mostrar_Menu_Marte()
                        elif planeta_seleccionado == "Venus":
                            Pantalla_Carga()
                            #Mostrar_Menu_Marte()
                        elif planeta_seleccionado == "Tierra":
                            Pantalla_Carga()
                            #Mostrar_Menu_Marte()
                        elif planeta_seleccionado == "Luna":
                            Pantalla_Carga()
                            #Mostrar_Menu_Marte()
                        elif planeta_seleccionado == "Marte":
                            Pantalla_Carga()
                            Pantalla_Menu_Marte()
                        elif planeta_seleccionado == "Jupiter":
                            Pantalla_Carga()
                            #Mostrar_Menu_Marte()
                        elif planeta_seleccionado == "Saturno":
                            Pantalla_Carga()
                            #Mostrar_Menu_Marte()
                        elif planeta_seleccionado == "Urano":
                            Pantalla_Carga()
                            #Mostrar_Menu_Marte()
                        elif planeta_seleccionado == "Neptuno":
                            Pantalla_Carga()
                            #Mostrar_Menu_Marte()
                        elif planeta_seleccionado == "Pluton":
                            Pantalla_Carga()
                            #Mostrar_Menu_Marte()
                        # Aquí puedes realizar la acción relacionada con el planeta seleccionado

        # Dibuja el fondo
        screen.blit(fondo, (0, 0))

        # Dibuja el título
        screen.blit(titulo, titulo_rect)

        # Dibuja las imágenes de los planetas en dos filas
        for nombre_planeta, (imagen_planeta, imagen_x_position, imagen_y_position) in imagenes_planetas.items():
            imagen_rect = imagen_planeta.get_rect()
            imagen_rect.topleft = (imagen_x_position, imagen_y_position)
            screen.blit(imagen_planeta, imagen_rect)

        pygame.display.flip()

def Pantalla_Menu_Principal_Regreso():
    Pantalla_Menu_Principal()