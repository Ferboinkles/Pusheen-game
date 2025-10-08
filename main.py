import pygame
import sys

pygame.init()
window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Pusheen!")
background = pygame.transform.scale(pygame.image.load("background.png"), (1000, 800))
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    window.blit(background, (0, 0))
    # Update display
    pygame.display.flip()

   # print("Sleepy time!")
    #sys.exit()  # Immediately stops the program

