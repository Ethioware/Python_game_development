import pygame


# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1920, 1080))

# Background
background = pygame.image.load('background.png')
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 255, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
