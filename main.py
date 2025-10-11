import sys

import pygame

pygame.init()
window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Pusheen!")
background = pygame.transform.scale(pygame.image.load("background.png"), (1000, 800))
pusheen = pygame.transform.scale(pygame.image.load("pusheen.png"), (200, 100))
pipe = pygame.transform.scale(pygame.image.load("pipe.png"), (86, 300))
pipeX = 1000.0
pipeY = 540.0
pusheenY = 350.0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    window.blit(background, (0, 0))
    window.blit(pipe, (pipeX, pipeY))
    pipeX -= 3
    keys = pygame.key.get_pressed()
    pusheenY += 4
    if keys[pygame.K_SPACE]:
        pusheenY -= 7
    window.blit(pusheen, (0, pusheenY))

    pygame.display.flip()