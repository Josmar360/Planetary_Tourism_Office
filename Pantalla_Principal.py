import pygame
import sys
import random
from Pantalla_Carga import Pantalla_Carga
from Pantalla_Menu_Principal import Pantalla_Menu_Principal

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
Estado_Carga = 0
Estado_Menu = 9
Estado_Carga2 = 2
Estado_Actual = Estado_Carga

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

    if Estado_Actual == Estado_Carga:
        Pantalla_Carga(screen, font)  #Pasa la pantalla y la fuente como argumentos
        Estado_Actual = Estado_Menu

    elif Estado_Actual == Estado_Menu:
        Pantalla_Menu_Principal()
        Estado_Actual = Estado_Carga2
    
    elif Estado_Actual == Estado_Carga2:
        Pantalla_Carga(screen, font)
        Estado_Actual = Estado_Carga #salir opcion

    # Coloca aquí la lógica y el renderizado de tu aplicación principal
    pygame.display.flip()

# Finaliza Pygame
pygame.quit()
sys.exit()