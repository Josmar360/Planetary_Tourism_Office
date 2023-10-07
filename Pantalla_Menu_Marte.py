import pygame
import sys
import os

# Inicializa Pygame
pygame.init()

# Configura la pantalla
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menú del planeta")

directorio_imagenes = "Recursos_Visuales"

# Carga la imagen de fondo
fondo = pygame.image.load(os.path.join(directorio_imagenes, "Fondo_Marte.png"))
fondo = pygame.transform.scale(fondo, (screen_width, screen_height))  # Escala la imagen al tamaño de la pantalla

# Colores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Fuente para el texto
font = pygame.font.Font(None, 36)

# Función para mostrar el menú
def Mostrar_Menu_Marte():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Si se presiona la tecla 1, entra a la informacion del planeta
                    Informacion_Planeta()
                elif event.key == pygame.K_2:
                    #Si se presiona la tecla 2, entra a la informacion del transbordador
                    Informacion_Transbordador()
                elif event.key == pygame.K_3:
                    #Si se presiona la tecla 3, entra a la informacion del habitat
                    Informacion_Habitat()
                elif event.key == pygame.K_4:
                    #Si se presiona la tecla 4, entra a la informacion del equipo
                    Informacion_Equipo()
                elif event.key == pygame.K_5:
                    #Si se presiona la tecla 5, entra a la informacion del costos
                    Informacion_Costos()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Dibuja el fondo
        screen.blit(fondo, (0, 0))

        # Dibuja el título del menú
        titulo = font.render("Menú del planeta", True, WHITE)
        titulo_rect = titulo.get_rect(center=(screen_width // 2, 100))
        screen.blit(titulo, titulo_rect)

        # Dibuja las opciones del menú
        opcion_planeta = font.render("Informacion del planeta (1)", True, GRAY)
        opcion_transbordador = font.render("Informacion del Transbordador (2)", True, GRAY)
        opcion_habitat = font.render("Informacion del habitat (3)", True, GRAY)
        opcion_equipo = font.render("Informacion del equipo acompañante (4)", True, GRAY)
        opcion_costo = font.render("Informacion de costos (5)", True, GRAY)
        opcion_salir = font.render("Salir del menu (ESC)", True, GRAY)

        opcion_planeta_rect = opcion_planeta.get_rect(center=(screen_width -1100, 300))
        opcion_transbordador_rect = opcion_transbordador.get_rect(center=(screen_width -1054, 350))
        opcion_habitat_rect = opcion_habitat.get_rect(center=(screen_width -1100, 400))
        opcion_equipo_rect = opcion_equipo.get_rect(center=(screen_width -1020, 450))
        opcion_costo_rect = opcion_costo.get_rect(center=(screen_width -1108, 500))
        opcion_salir_rect = opcion_salir.get_rect(center=(screen_width -1136, 550))

        screen.blit(opcion_planeta, opcion_planeta_rect)
        screen.blit(opcion_transbordador, opcion_transbordador_rect)
        screen.blit(opcion_habitat, opcion_habitat_rect)
        screen.blit(opcion_equipo, opcion_equipo_rect)
        screen.blit(opcion_costo, opcion_costo_rect)
        screen.blit(opcion_salir, opcion_salir_rect)

        pygame.display.flip()

# Función para iniciar la informacion
def Informacion_Planeta():
    print("Informacion del planeta")

def Informacion_Transbordador():
    print("Informacion del transbordador")

def Informacion_Habitat():
    print("Informacion del habitat")

def Informacion_Equipo():
    print("Informacion del equipo")

def Informacion_Costos():
    print("Informacion de costos")