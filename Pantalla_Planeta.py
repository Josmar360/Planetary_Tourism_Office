import pygame
import random
import math



def Seleccion_Planeta():
   

    #case = random.randint(0, 10)
    case = 0
    if case == 0:
        Planeta = "Sol.png"
    return Planeta

def Pantalla_Planetas(screen, font):
    imagen = pygame.image.load(Seleccion_Planeta())
    imagen = pygame.transform.scale(imagen, (400, 400))  # Cambia el tamaño de la imagen si es necesario

    screen.blit(imagen, (0, 0))  # Pinta la imagen en la pantalla
    pygame.display.update()  # Actualiza la pantalla
    pygame.time.delay(2000)  # Espera 2 segundos
    
    #Dibuja un texto en la pantalla
    text = font.render("Sol", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 10))
    screen.blit(text, text_rect)
    text = font.render("Sol", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 10))
    screen.blit(text, text_rect)
    