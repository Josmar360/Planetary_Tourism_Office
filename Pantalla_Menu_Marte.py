import pygame
import sys
import os
from Pantalla_Carga import Pantalla_Carga
from Pantalla_Planeta_Marte import Pantalla_Marte
from Pantalla_Transbordador import Pantalla_Nave
from Pantalla_Marte_Habitat import Pantalla_Habitat
from Pantalla_Equipo import Pantalla_Equipo
from Pantalla_Costos import Pantalla_Costos

# Inicializa Pygame
pygame.init()

# Configura la pantalla
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menú de Selección")

directorio_imagenes = "Recursos_Visuales"
Planeta = os.path.join(directorio_imagenes, "Fondo_Marte.png")

# Cargar la imagen de fondo y redimensionarla
fondo_marte = pygame.image.load(Planeta)
fondo_marte = pygame.transform.scale(fondo_marte, (screen_width, screen_height))

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (249, 133, 63)

# Fuente para el texto
font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 60)

# Lista de opciones del menú
menu_options = [
    "Información del planeta",
    "Información del Transbordador",
    "Información del hábitat",
    "Información del equipo acompañante",
    "Información de costos",
    "Salir del menú"
]

# Tamaño de los rectángulos de opción
opcion_width, opcion_height = 470, 50

# Función para mostrar el menú
def Pantalla_Menu_Marte():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, opcion in enumerate(menu_options):
                    opcion_rect = pygame.Rect(
                        screen_width - 1250,
                        200 + i * (opcion_height + 20),  # Espaciado vertical
                        opcion_width,
                        opcion_height
                    )
                    if opcion_rect.collidepoint(x, y):
                        ejecutar_accion(i)

        # Dibujar el fondo de Marte
        screen.blit(fondo_marte, (0, 0))

        # Dibuja el título del menú
        titulo = font1.render("Menú de Selección", True, WHITE)
        titulo_rect = titulo.get_rect(center=(screen_width // 2, 50))
        screen.blit(titulo, titulo_rect)

        # Dibuja las opciones del menú en rectángulos
        for i, opcion in enumerate(menu_options):
            opcion_rect = pygame.Rect(
                screen_width - 1250,
                200 + i * (opcion_height + 20),  # Espaciado vertical
                opcion_width,
                opcion_height
            )
            pygame.draw.rect(screen, GRAY, opcion_rect)
            opcion_text = font.render(opcion, True, BLACK)
            opcion_text_rect = opcion_text.get_rect(center=opcion_rect.center)
            screen.blit(opcion_text, opcion_text_rect)

        pygame.display.flip()

# Funciones de acción para cada opción del menú
def informacion_planeta():
    Pantalla_Carga()
    Pantalla_Marte()

def informacion_transbordador():
    Pantalla_Carga()
    Pantalla_Nave()

def informacion_habitat():
    Pantalla_Carga()
    Pantalla_Habitat()

def informacion_equipo_acompanante():
    Pantalla_Carga()
    Pantalla_Equipo()

def informacion_costos():
    Pantalla_Carga()
    Pantalla_Costos()

def salir_del_menu():
    screen.fill((0, 0, 0))
    pygame.display.flip()
    sys.exit()

# Asocia las funciones de acción a las opciones del menú
acciones_menu = [
    informacion_planeta,
    informacion_transbordador,
    informacion_habitat,
    informacion_equipo_acompanante,
    informacion_costos,
    salir_del_menu
]

# Función para ejecutar la acción correspondiente
def ejecutar_accion(opcion):
    acciones_menu[opcion]()

if __name__ == "__main__":
    Pantalla_Menu_Marte()
    pygame.display.flip()
