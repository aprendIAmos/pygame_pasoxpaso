import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 400))

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((255, 255, 255))

    # NUEVO: dibujar el personaje
    pygame.draw.rect(ventana, (0, 0, 0), (50, 300, 40, 40))

    pygame.display.flip()

pygame.quit()