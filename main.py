import sys

import pygame

# Sound
# pygame.mixer.init()
# Variabllllllllllles! Awwwwwwwww yeah!
pygame.init()
window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Pusheen!")
score = 0
background = pygame.transform.scale(pygame.image.load("background.png"), (1000, 800))
pusheen = pygame.transform.scale(pygame.image.load("pusheen.png"), (200, 100))
pipe = pygame.transform.scale(pygame.image.load("pipe.png"), (86, 300))
pipe2 = pygame.transform.scale(pygame.image.load("pipe2.png"), (86, 300))
pipe3 = pygame.transform.scale(pygame.image.load("pipe3.png"), (86, 300))
pipe4 = pygame.transform.scale(pygame.image.load("pipe4.png"), (86, 300))
pipeRect = pipe.get_rect()
pipe2Rect = pipe2.get_rect()
pipe3Rect = pipe2.get_rect()
pipe4Rect = pipe2.get_rect()
pusheenRect = pusheen.get_rect()
font = pygame.font.SysFont("Press Start 2P", 80)
pipeX = 1000.0
pipeY = 540
pipe2X = 1000.0
pipe2Y = 0
pipe3X = 850.0
pipe3Y = 540.0
pipe4X = 850.0
pipe4Y = 0
pusheenX = 50.0
pusheenY = 350.0
# Rectangles
pipeRect.update(pipeX, pipeY, 86, 300)
pipe2Rect.update(pipe2X, pipe2Y, 86, 300)
pipe3Rect.update(pipe3X, pipe3Y, 86, 300)
pipe4Rect.update(pipe4X, pipe4Y, 86, 300)
pusheenRect.update(pusheenX, pusheenY, 200, 100)
# Main game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    window.blit(background, (0, 0))
    if pygame.Rect.colliderect(pipeRect, pusheenRect) or pygame.Rect.colliderect(pipe2Rect,
                                                                                 pusheenRect) or pygame.Rect.colliderect(
            pipe3Rect, pusheenRect) or pygame.Rect.colliderect(pipe4Rect, pusheenRect):
        sys.exit()
    if pipeX == 100:
        score = score + 1
    if pipe4X == 100:
        score = score + 1
    scoreText = font.render(str(score), 1, "blue")
    window.blit(scoreText, scoreText.get_rect(centerx=100) )
    pipeRect.update(pipeX, pipeY, 86, 300)
    pipe2Rect.update(pipe2X, pipe2Y, 86, 300)
    pipe3Rect.update(pipe3X, pipe3Y, 86, 300)
    pipe4Rect.update(pipe4X, pipe4Y, 86, 300)
    pusheenRect.update(pusheenX, pusheenY, 200, 100)
    window.blit(pipe, (pipeX, pipeY))
    window.blit(pipe2, (pipe2X, pipe2Y))
    window.blit(pipe3, (pipe3X, pipe3Y))
    window.blit(pipe4, (pipe4X, pipe4Y))
    pipeX -= 3
    pipe2X -= 3
    pipe3X -= 3
    pipe4X -= 3
    if pipeX <= -100:
        if pipe2X <= -100:
            if pipe3X <= -100:
                if pipe4X <= -100:
                    pipe3X = 850.0
                    pipe4X = 850.0
            pipe2X = 1000.0
        pipeX = 1000.0
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
