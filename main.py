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
background = pygame.transform.scale(pygame.image.load("background.png"), (1000, 800))
pusheen = pygame.transform.scale(pygame.image.load("pusheen.png"), (200, 100))
pipe = pygame.transform.scale(pygame.image.load("pipe.png"), (150, 300))
pipe2 = pygame.transform.scale(pygame.image.load("pipe2.png"), (150, 300))
pipe3 = pygame.transform.scale(pygame.image.load("pipe3.png"), (150, 300))
pipe4 = pygame.transform.scale(pygame.image.load("pipe4.png"), (150, 300))
pipe5 = pygame.transform.scale(pygame.image.load("pipe5.png"), (150, 300))
pipe6 = pygame.transform.scale(pygame.image.load("pipe6.png"), (150, 300))
pipeRect = pipe.get_rect()
pipe2Rect = pipe2.get_rect()
pipe3Rect = pipe3.get_rect()
pipe4Rect = pipe4.get_rect()
pipe5Rect = pipe5.get_rect()
pipe6Rect = pipe6.get_rect()
pusheenRect = pusheen.get_rect()
font = pygame.font.SysFont("javanesetext", 80)
pipeX = 1000.0
pipeY = 540.0
pipe2X = 1000.0
pipe2Y = pipeY - 540
pipe3X = 800.0
pipe3Y = pipeY
pipe4X = 800.0
pipe4Y = pipeY - 540
pipe5X = 600.0
pipe5Y = pipeY
pipe6X = 600.0
pipe6Y = pipeY - 540
pusheenX = 50.0
pusheenY = 350.0
# Rectangles
pipeRect.update(pipeX, pipeY, 150, 300)
pipe2Rect.update(pipe2X, pipe2Y, 150, 300)
pipe3Rect.update(pipe3X, pipe3Y, 150, 300)
pipe4Rect.update(pipe4X, pipe4Y, 150, 300)
pipe5Rect.update(pipe5X, pipe5Y, 150, 300)
pipe6Rect.update(pipe6X, pipe6Y, 150, 300)
pusheenRect.update(pusheenX, pusheenY, 200, 100)
# Main game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.blit(background, (0, 0))
    if pygame.Rect.colliderect(pipeRect, pusheenRect) or pygame.Rect.colliderect(pipe2Rect,
                                                                                 pusheenRect) or pygame.Rect.colliderect(
        pipe3Rect, pusheenRect) or pygame.Rect.colliderect(pipe4Rect, pusheenRect) or pygame.Rect.colliderect(pipe5Rect,
                                                                                                              pusheenRect) or pygame.Rect.colliderect(
        pipe6Rect, pusheenRect):
        gameOverText = font.render("Pusheen fell asleep!", 1, (39, 2, 222))
        gameOverText2 = font.render(f"You got a score of {str(score)}", 1, (39, 2, 222))
        window.blit(gameOverText, (200, 300))
        window.blit(gameOverText2, (200, 400))
        pygame.display.update()
        time.sleep(4)
        pygame.quit()
    if pipeX == 100:
        score = score + 1
    if pipe4X == 100:
        score = score + 1
    if pipe6X == 100:
        score = score + 1
    scoreText = font.render(str(score), 1, "blue")
    window.blit(scoreText, scoreText.get_rect(centerx=100))
    pipeRect.update(pipeX, pipeY, 150, 300)
    pipe2Rect.update(pipe2X, pipe2Y, 150, 300)
    pipe3Rect.update(pipe3X, pipe3Y, 150, 300)
    pipe4Rect.update(pipe4X, pipe4Y, 150, 300)
    pipe5Rect.update(pipe5X, pipe5Y, 150, 300)
    pipe6Rect.update(pipe6X, pipe6Y, 150, 300)
    pusheenRect.update(pusheenX, pusheenY, 200, 100)
    window.blit(pipe, (pipeX, pipeY))
    window.blit(pipe2, (pipe2X, pipe2Y))
    window.blit(pipe3, (pipe3X, pipe3Y))
    window.blit(pipe4, (pipe4X, pipe4Y))
    window.blit(pipe5, (pipe5X, pipe5Y))
    window.blit(pipe6, (pipe6X, pipe6Y))
    pipeX -= 4
    pipe2X -= 4
    pipe3X -= 4
    pipe4X -= 4
    pipe5X -= 4
    pipe6X -= 4
    if pipeX <= -100:
        if pipe2X <= -100:
            if pipe3X <= -100:
                if pipe4X <= -100:
                    if pipe5X <= -100:
                        if pipe6X <= -100:
                            pipe6X = 600
                            pipe5X = 600
                    pipe4X = 800.0
                pipe3X = 800.0
            pipe2X = 1000.0
        pipeX = 1000.0
    keys = pygame.key.get_pressed()
    pusheenY += 3.5
    if keys[pygame.K_SPACE]:
        pusheenY -= 7
    window.blit(pusheen, (pusheenX, pusheenY))
    pygame.display.flip()
