import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 400))

x = 50
y = 300
velocidad = 0.2

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    # Movimiento del personaje
    if teclas[pygame.K_RIGHT]:
        x = x + velocidad

    if teclas[pygame.K_LEFT]:
        x = x - velocidad

    if teclas[pygame.K_UP]:
        y = y - velocidad

    if teclas[pygame.K_DOWN]:
        y = y + velocidad

    # NUEVO: controlar los límites de la ventana
    if x < 0:
        x = 0

    if x > 760:
        x = 760

    if y < 0:
        y = 0

    if y > 360:
        y = 360

    ventana.fill((255, 255, 255))

    pygame.draw.rect(ventana, (0, 0, 0), (x, y, 40, 40))

    pygame.draw.circle(ventana, (255, 0, 0), (200, 200), 40)

    pygame.draw.line(ventana, (0, 0, 255), (300, 100), (450, 100), 5)

    pygame.draw.ellipse(ventana, (0, 255, 0), (500, 150, 120, 60))

    pygame.draw.polygon(
        ventana,
        (255, 165, 0),
        [(650, 300), (700, 200), (750, 300)]
    )

    pygame.display.flip()

pygame.quit()