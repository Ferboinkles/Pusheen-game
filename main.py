import pygame
import sys

# Start pygame
pygame.init()

# Create a window (800x600)
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pusheen!")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill background color
    window.fill((173, 216, 230))  # light blue

    # Draw a "desktop icon"
    pygame.draw.rect(window, (255, 255, 255), (100, 100, 80, 80))
    pygame.draw.circle(window, (0, 0, 255), (140, 140), 30)

    # Update display
    pygame.display.flip()
