import pygame
import random
import math
import os


def Seleccion_Planeta():
    directorio_imagenes = "Recursos_Visuales"

    case = random.randint(0, 10)
    if (case == 0):
        Planeta = os.path.join(directorio_imagenes, "Sol.png")
    elif (case == 1):
        Planeta = os.path.join(directorio_imagenes, "Mercurio.png")
    elif (case == 2):
        Planeta = os.path.join(directorio_imagenes, "Venus.png")
    elif (case == 3):
        Planeta = os.path.join(directorio_imagenes, "Tierra.png")
    elif (case == 4):
        Planeta = os.path.join(directorio_imagenes, "Luna.png")
    elif (case == 5):
        Planeta = os.path.join(directorio_imagenes, "Marte.png")
    elif (case == 6):
        Planeta = os.path.join(directorio_imagenes, "Jupiter.png")
    elif (case == 7):
        Planeta = os.path.join(directorio_imagenes, "Saturno.png")
    elif (case == 8):
        Planeta = os.path.join(directorio_imagenes, "Urano.png")
    elif (case == 9):
        Planeta = os.path.join(directorio_imagenes, "Neptuno.png")
    elif (case == 10):
        Planeta = os.path.join(directorio_imagenes, "Pluton.png")
    return Planeta

def Pantalla_Carga():
    # Configura la pantalla
    screen_width, screen_height = 1280, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Selección de Planetas")

    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Fuente para el texto
    font = pygame.font.Font(None, 80)

    imagen = pygame.image.load(Seleccion_Planeta())
    imagen = pygame.transform.scale(imagen, (200, 200))  # Cambia el tamaño de la imagen si es necesario

    # Variables para la animación de la imagen
    imagen_x = screen.get_width() // 2
    imagen_y = screen.get_height() // 2
    imagen_rotation_speed = 1  # Ajusta la velocidad de rotación

    # Estrellas de fondo
    num_stars = 300
    stars = [(random.randint(0, screen.get_width()), random.randint(0, screen.get_height())) for _ in range(num_stars)]

    # Bucle de carga
    loading = True
    clock = pygame.time.Clock()
    while loading:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loading = False

        # Lógica de animación de la imagen
        imagen_rotation_speed += 2

        # Limpia la pantalla
        screen.fill((0, 0, 0))

        # Dibuja estrellas de fondo
        for star in stars:
            pygame.draw.circle(screen, (255, 255, 255), star, 2)

        # Rota y dibuja la imagen
        imagen_rotada = pygame.transform.rotate(imagen, imagen_rotation_speed)
        imagen_rect = imagen_rotada.get_rect(center=(imagen_x + int(150 * math.cos(math.radians(imagen_rotation_speed))), imagen_y + int(150 * math.sin(math.radians(imagen_rotation_speed)))))
        screen.blit(imagen_rotada, imagen_rect)

        # Dibuja el texto de progreso
        text = font.render("Cargando...", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.1))
        screen.blit(text, text_rect)

        pygame.display.flip()

        # Controla la velocidad de fotogramas
        clock.tick(40)  # Puedes ajustar esto para cambiar la velocidad de la animación

        # Simula la carga completada después de un cierto tiempo
        if imagen_rotation_speed >= 360:
            loading = False

    # Limpia la pantalla
    screen.fill((0, 0, 0))
    pygame.display.flip()
