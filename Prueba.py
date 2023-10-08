import pygame
import os

# Directorio de imágenes
directorio_imagenes = "Recursos_Visuales"

def cargar_imagen(nombre_archivo, tamano=(400, 400)):
    imagen = pygame.image.load(nombre_archivo)
    imagen = pygame.transform.scale(imagen, tamano)
    return imagen

def dibujar_imagen_en_el_centro(screen, imagen):
    x = (screen.get_width() - imagen.get_width()) // 2
    y = (screen.get_height() - imagen.get_height()) // 2
    screen.blit(imagen, (x, y))

def dibujar_texto_en_el_centro(screen, texto, font, color, y_offset):
    text = font.render(texto, True, color)
    text_rect = text.get_rect(center=(screen.get_width() // 2, y_offset))
    screen.blit(text, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Carga la imagen del planeta
    planeta_imagen = cargar_imagen(os.path.join(directorio_imagenes, "Nave.png"))

    # Configura la fuente
    font = pygame.font.Font(None, 72)

    # Dibuja la imagen del planeta en el centro de la pantalla
    dibujar_imagen_en_el_centro(screen, planeta_imagen)

    # Dibuja el texto "VSS Unity" en la parte superior
    dibujar_texto_en_el_centro(screen, " VSS Unity ", font, (255, 0, 0), screen.get_height() // 10)

    # Texto adicional
    texto_adicional = [
        "Nave espacial suborbital:",
        "Capacidad para seis pasajeros",
        "Lanzamiento desde avión nodriza",
        "200,000$",
        "Visión panorámica",
    ]

    y_offset = screen.get_height() // 3.5

    for linea in texto_adicional:
        dibujar_texto_en_el_centro(screen, linea, font, (255, 255, 255), y_offset)
        y_offset += font.get_height() + 10

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
