import pygame
import sys
from Pantalla_Carga import Pantalla_Carga
from Pantalla_Menu_Marte import Mostrar_Menu_Marte

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
    font = pygame.font.Font(None, 36)

    # Texto del título
    titulo = font.render("Selección de Planetas", True, WHITE)
    titulo_rect = titulo.get_rect(center=(screen_width // 2, 40))

    # Lista de opciones de planetas
    planetas = ["Sol", "Mercurio", "Venus", "Tierra", "Luna", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno", "Pluton"]

    # Crea botones para las opciones de planetas
    botones_planetas = []
    y1 = screen_height // 2 - 75
    y2 = screen_height // 2 - 75
    x1, x2 = screen_width // 4 - 100, screen_width // 4 * 3 - 100

    for i, planeta in enumerate(planetas):
        if i < len(planetas) // 2:
            boton = pygame.Rect(x1, y1, 200, 50)
            y1 += 60
        else:
            boton = pygame.Rect(x2, y2, 200, 50)
            y2 += 60
        botones_planetas.append(boton)

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, boton in enumerate(botones_planetas):
                    if boton.collidepoint(x, y):
                        planeta_seleccionado = planetas[i]
                        if (planetas[5]):
                            Pantalla_Carga(screen, font)
                            Mostrar_Menu_Marte()

                        print(f"Has seleccionado {planeta_seleccionado}")
                        # Aquí puedes realizar la acción relacionada con el planeta seleccionado

        # Dibuja el fondo
        screen.fill(BLACK)

        # Dibuja el título
        screen.blit(titulo, titulo_rect)

        # Dibuja los botones de los planetas
        for i, boton in enumerate(botones_planetas):
            pygame.draw.rect(screen, WHITE, boton)
            texto_planeta = font.render(planetas[i], True, BLACK)
            texto_rect = texto_planeta.get_rect(center=boton.center)
            screen.blit(texto_planeta, texto_rect)

        pygame.display.flip()