import pygame
import random

# Inicialización de Pygame
pygame.init()

# Tamaño de la pantalla
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Tamaño del gusano y de la manzana
snake_size = 20
apple_size = 20

# Velocidad del gusano
snake_speed = 10

# Coordenadas iniciales del gusano
x = width / 2
y = height / 2

# Velocidad inicial del gusano
x_speed = 0
y_speed = 0

# Lista que representa el cuerpo del gusano
snake_body = []
snake_length = 1

# Posición inicial de la manzana
apple_x = round(random.randrange(0, width - apple_size) / 20.0) * 20.0
apple_y = round(random.randrange(0, height - apple_size) / 20.0) * 20.0

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Captura de teclas presionadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -snake_size
                y_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = snake_size
                y_speed = 0
            elif event.key == pygame.K_UP:
                y_speed = -snake_size
                x_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = snake_size
                x_speed = 0

    # Actualización de la posición del gusano
    x += x_speed
    y += y_speed

    # Verificación de colisiones con los límites de la pantalla
    if x < 0 or x >= width or y < 0 or y >= height:
        running = False

    # Dibujado del fondo de la pantalla
    screen.fill(black)

    # Dibujado del gusano
    pygame.draw.rect(screen, white, (x, y, snake_size, snake_size))

    # Dibujado de la manzana
    pygame.draw.rect(screen, red, (apple_x, apple_y, apple_size, apple_size))

    # Actualización del cuerpo del gusano
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    # Verificación de colisión con la manzana
    if x == apple_x and y == apple_y:
        apple_x = round(random.randrange(0, width - apple_size) / 20.0) * 20.0
        apple_y = round(random.randrange(0, height - apple_size) / 20.0) * 20.0
        snake_length += 1

    # Verificación de colisión con el propio cuerpo del gusano
    for segment in snake_body[:-1]:
        if segment == snake_head:
            running = False

    # Dibujado del cuerpo del gusano
    for segment in snake_body:
        pygame.draw.rect(screen, white, (segment[0], segment[1], snake_size, snake_size))

    # Actualización de la pantalla
    pygame.display.update()

    # Control de la velocidad de actualización
    pygame.time.Clock().tick(snake_speed)

# Cierre de Pygame
pygame.quit()
