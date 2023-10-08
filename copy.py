import pygame
import os

# Inicializa Pygame
pygame.init()

# Configura la pantalla
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menú de Selección")

# Cargar la imagen de fondo y redimensionarla
fondo_marte = pygame.image.load("Fondo_Marte.png")
fondo_marte = pygame.transform.scale(fondo_marte, (screen_width, screen_height))

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (249, 133, 63)

# Fuente para el texto
font = pygame.font.Font(None, 36)

directorio_imagenes = "Recursos_Visuales"

def Seleccion_Planeta():
    #case = random.randint(0, 10)
    case = 0
    if case == 0:
        Planeta = os.path.join(directorio_imagenes, "Marte.png")
    return Planeta

def Pantalla_Planetas():
    imagen = pygame.image.load(Seleccion_Planeta())
    imagen = pygame.transform.scale(imagen, (1280, 720))  # Cambia el tamaño de la imagen si es necesario

    # Calcula las coordenadas para centrar la imagen
    x = (screen.get_width() - imagen.get_width()) // 2
    y = (screen.get_height() - imagen.get_height()) // 2

    screen.blit(imagen, (x, y))  # Pinta la imagen en la pantalla
 # Crea una fuente más grande para el texto "Sol"
    font_sol = pygame.font.Font(None, 72)
    text = font_sol.render("Marte", True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 10))
    screen.blit(text, text_rect)
    # Nuevo texto a agregar, dividido en líneas
    additional_text_lines = [
        "Costo:"," $100 mil millones ",
        "Destino:"," Marte ",
        "Fecha: ","2025",
        "Tiempo de viaje:" ,"234 días"
       
    ]


    # Renderiza cada línea de texto y la coloca verticalmente
    y_offset = screen.get_height() // 3.5
    for line in additional_text_lines:
        text = font.render(line, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() // 1.3, y_offset))
        screen.blit(text, text_rect)
        y_offset += text.get_height() + 10  #
        

