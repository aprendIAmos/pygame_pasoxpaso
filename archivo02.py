import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 400))

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # NUEVO: pintar el fondo
    ventana.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()