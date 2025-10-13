import sys

import pygame

# Variabllllllllllles! Awwwwwwwww yeah!
pygame.init()
window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Pusheen!")
background = pygame.transform.scale(pygame.image.load("background.png"), (1000, 800))
pusheen = pygame.transform.scale(pygame.image.load("pusheen.png"), (200, 100))
pipe = pygame.transform.scale(pygame.image.load("pipe.png"), (86, 300))
pipe2 = pygame.transform.scale(pygame.image.load("pipe2.png"), (86, 300))
pipeRect = pipe.get_rect()
pipe2Rect = pipe2.get_rect()
pusheenRect = pusheen.get_rect()
pipeX = 1000.0
pipeY = 540
pipe2X = 1000.0
pipe2Y = 0
pusheenX = 50.0
pusheenY = 350.0
pipeRect.update(pipeX, pipeY, 86, 300)
pipe2Rect.update(pipe2X, pipe2Y, 86, 300)
pusheenRect.update(pusheenX, pusheenY, 200, 100)
# Main game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pygame.Rect.colliderect(pipeRect, pusheenRect) or pygame.Rect.colliderect(pipe2Rect, pusheenRect):
        sys.exit()
    pipeRect.update(pipeX, pipeY, 86, 300)
    pipe2Rect.update(pipe2X, pipe2Y, 86, 300)
    pusheenRect.update(pusheenX, pusheenY, 200, 100)
    window.blit(background, (0, 0))
    window.blit(pipe, (pipeX, pipeY))
    window.blit(pipe2, (pipe2X, pipe2Y))
    pipeX -= 3
    pipe2X -= 3
    if pipeX <= -100:
        if pipe2X <= -100:
            pipeX = 1000.0
        pipe2X = 1000.0
    if pusheenY <= 0:
        sys.exit()
    if pusheenY >= 800:
        sys.exit()
    keys = pygame.key.get_pressed()
    pusheenY += 3.5
    if keys[pygame.K_SPACE]:
        pusheenY -= 7
    window.blit(pusheen, (pusheenX, pusheenY))

    pygame.display.flip()