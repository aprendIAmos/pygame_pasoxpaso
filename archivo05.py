import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 400))

# NUEVO: posición y velocidad del rectángulo
x = 50
velocidad = 2 # 0.2 -> más lento

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((255, 255, 255))

    # MODIFICADO: usamos la variable x
    pygame.draw.rect(ventana, (0, 0, 0), (x, 300, 40, 40))

    pygame.draw.circle(ventana, (255, 0, 0), (200, 200), 40)

    pygame.draw.line(ventana, (0, 0, 255), (300, 100), (450, 100), 5)

    pygame.draw.ellipse(ventana, (0, 255, 0), (500, 150, 120, 60))

    pygame.draw.polygon(
        ventana,
        (255, 165, 0),
        [(650, 300), (700, 200), (750, 300)]
    )

    # NUEVO: actualizar la posición
    x = x + velocidad

    pygame.display.flip()

pygame.quit()