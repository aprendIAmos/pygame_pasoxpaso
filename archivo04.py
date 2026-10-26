import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 400))

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((255, 255, 255))

    # Rectángulo (código anterior)
    pygame.draw.rect(ventana, (0, 0, 0), (50, 300, 40, 40))

    # NUEVO: círculo
    pygame.draw.circle(ventana, (255, 0, 0), (200, 200), 40)

    # NUEVO: línea
    pygame.draw.line(ventana, (0, 0, 255), (300, 100), (450, 100), 5)

    # NUEVO: elipse
    pygame.draw.ellipse(ventana, (0, 255, 0), (500, 150, 120, 60))

    # NUEVO: polígono (triángulo)
    pygame.draw.polygon(
        ventana,
        (255, 165, 0),
        [(650, 300), (700, 200), (750, 300)]
    )

    pygame.display.flip()

pygame.quit()