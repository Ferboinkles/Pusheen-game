import random
import time

import pygame

# Sound
pygame.mixer.init()
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)
# Variabllllllllllles! Awwwwwwwww yeah!
pygame.init()
window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Pusheen!")
score = 0
clock = pygame.time.Clock()
startDown = True
background = pygame.transform.scale(pygame.image.load("background.png"), (1000, 800))
pusheen = pygame.transform.scale(pygame.image.load("pusheen.png"), (150, 100))
pipe = pygame.transform.scale(pygame.image.load("pipe.png"), (150, 700))
pipe2 = pygame.transform.scale(pygame.image.load("pipe2.png"), (150, 700))
pipe3 = pygame.transform.scale(pygame.image.load("pipe3.png"), (150, 700))
pipe4 = pygame.transform.scale(pygame.image.load("pipe4.png"), (150, 700))
pipeRect = pipe.get_rect()
pipe2Rect = pipe2.get_rect()
pipe3Rect = pipe3.get_rect()
pipe4Rect = pipe4.get_rect()
pusheenRect = pusheen.get_rect()
font = pygame.font.SysFont("javanesetext", 70)
pipeX = 1000.0
pipeY = random.randint(200, 700)
pipe2X = 1000.0
pipe2Y = pipeY - 1000
pipe3X = 500.0
pipe3Y = random.randint(200, 700)
pipe4X = 500.0
pipe4Y = pipe3Y - 1000
pusheenX = 50.0
pusheenY = 350.0
# Rectangles
pipeRect.update(pipeX, pipeY, 150, 700)
pipe2Rect.update(pipe2X, pipe2Y, 150, 700)
pipe3Rect.update(pipe3X, pipe3Y, 150, 700)
pipe4Rect.update(pipe4X, pipe4Y, 150, 700)
pusheenRect.update(pusheenX, pusheenY, 150, 100)
# Main game
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.blit(background, (0, 0))
    if pygame.Rect.colliderect(pipeRect, pusheenRect) or pygame.Rect.colliderect(pipe2Rect,
                                                                                 pusheenRect) or pygame.Rect.colliderect(
        pipe3Rect, pusheenRect) or pygame.Rect.colliderect(pipe4Rect,
                                                           pusheenRect) or pusheenY == 10 or pusheenY == -810:
        gameOverText = font.render("Pusheen fell asleep!", 1, (10, 208, 247))
        gameOverText2 = font.render(f"You got a score of {str(score)}", 1, (10, 208, 247))
        window.blit(gameOverText, (200, 300))
        window.blit(gameOverText2, (200, 400))
        pygame.display.update()
        time.sleep(4)
        pygame.quit()
    if pipeX == 100:
        score = score + 1
    if pipe4X == 100:
        score = score + 1
    scoreText = font.render(str(score), 1, (10, 208, 247))
    window.blit(scoreText, scoreText.get_rect(centerx=100))
    pipeRect.update(pipeX, pipeY, 150, 700)
    pipe2Rect.update(pipe2X, pipe2Y, 150, 700)
    pipe3Rect.update(pipe3X, pipe3Y, 150, 700)
    pipe4Rect.update(pipe4X, pipe4Y, 150, 700)
    pusheenRect.update(pusheenX, pusheenY, 150, 100)
    window.blit(pipe, (pipeX, pipeY))
    window.blit(pipe2, (pipe2X, pipe2Y))
    window.blit(pipe3, (pipe3X, pipe3Y))
    window.blit(pipe4, (pipe4X, pipe4Y))
    pipeX -= 4.5
    pipe2X -= 4.5
    pipe3X -= 4.5
    pipe4X -= 4.5
    if pipeX <= -100:
        pipeX = 1000.0
        pipeY = random.randint(200, 700)
        pipe2X = 1000.0
        pipe2Y = pipeY - 1000

    if pipe3X <= -100:
        pipe3X = 1000.0
        pipe3Y = random.randint(200, 700)
        pipe4X = 1000.0
        pipe4Y = pipe3Y - 1000

    keys = pygame.key.get_pressed()
    pusheenY += 4.5
    if keys[pygame.K_SPACE]:
        pusheenY -= 9
    window.blit(pusheen, (pusheenX, pusheenY))
    if keys[pygame.K_b]:
        gameOverText = font.render("You seem to have pressed the paws button!", 1, (10, 208, 247))
        gameOverText2 = font.render("Have a 5 second break meow!", 1, (10, 208, 247))
        window.blit(gameOverText, (0, 300))
        window.blit(gameOverText2, (80, 400))
        pygame.display.update()
        time.sleep(5)
    pygame.display.flip()
    if startDown:
        text3 = font.render("3", 1, (10, 208, 247))
        window.blit(text3, (500, 300))
        pygame.display.update()
        time.sleep(1)
        text2 = font.render("2", 1, (10, 208, 247))
        window.blit(text2, (550, 300))
        pygame.display.update()
        time.sleep(1)
        text1 = font.render("1", 1, (
            10, 208, 247
        ))
        window.blit(text1, (600, 300))
        pygame.display.update()
        time.sleep(1)
        startDown = False
