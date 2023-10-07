import pygame
import sys
import math
import random
from Pantalla_Carga import Pantalla_Carga, Seleccion_Planeta
from Pantalla_Planeta import Pantalla_Planetas
# Inicializa Pygame
pygame.init()

# Configura la pantalla
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Oficina Turistica Planetaria")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente para el texto
font = pygame.font.Font(None, 36)

#Variables para estado de la aplicacion
Pantalla_Planeta = 0
Estado_Menu = 1
Estado_Actual = Pantalla_Planeta

def Pantalla_Menu():
    # Estrellas de fondo
    num_stars = 100
    stars = [(random.randint(0, screen_width), random.randint(0, screen_height)) for _ in range(num_stars)]
    
    # Dibuja estrellas de fondo
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 2)
 
# Bucle principal de la aplicación
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if Estado_Actual == Pantalla_Planeta:
        Pantalla_Planetas(screen, font)  # Pasa la pantalla y la fuente como argumentos
        Estado_Actual = 3

    elif Estado_Actual == Estado_Menu:
        Pantalla_Menu()
        Estado_Actual = 5
    
    # Coloca aquí la lógica y el renderizado de tu aplicación principal

    pygame.display.flip()

# Finaliza Pygame
pygame.quit()
sys.exit()