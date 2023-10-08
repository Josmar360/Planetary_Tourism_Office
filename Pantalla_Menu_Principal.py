import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Viaja con Nosotros al Espacio")

# Colores
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

# Fuentes
font = pygame.font.Font(None, 36)

# Inicializar variables para nombre y correo electrónico
nombre = ""
correo = ""

# Función para mostrar texto en la pantalla
def mostrar_texto(texto, x, y, color):
    texto_superficie = font.render(texto, True, color)
    screen.blit(texto_superficie, (x, y))

# Función para mostrar botones
def mostrar_boton(texto, x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    mostrar_texto(texto, x + 5, y + 5, BLACK)


# Bucle principal
registrando = True
while registrando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            registrando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Cuando se presiona Enter, mostrar ventana de opciones
                registrando = False
                opciones = True
            elif event.key == pygame.K_BACKSPACE:
                nombre = nombre[:-1]
                correo = correo[:-1]
            else:
                nombre += event.unicode
                correo += event.unicode

    screen.fill(BLACK)
    mostrar_texto("!LA LUNA Y MARTE MÁS CERCA DE TI!", 150, 50, WHITE)
    mostrar_texto("Nombre:", 50, 100, WHITE)
    mostrar_texto(nombre, 100, 100, RED)
    mostrar_texto("Correo electrónico:", 50, 400, WHITE)
    mostrar_texto(correo, 50, 450, RED)
    mostrar_boton("Registrarse", 100, 350, 200, 50, BLUE)

    pygame.display.flip()

# Ventana de opciones
opciones = True
while opciones:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            opciones = False

    screen.fill(WHITE)
    mostrar_texto("Seleccione un planeta:", 100, 50, )
    # Aquí puedes agregar botones para los planetas con imágenes y enlazar las ventanas correspondientes
    mostrar_boton("Luna", 100, 430, 200, 50, BLUE)
    mostrar_boton("Marte", 100, 500, 200, 50, RED)

    pygame.display.flip()

pygame.quit()