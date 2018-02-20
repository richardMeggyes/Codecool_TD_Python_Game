# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 3 - Load images
player = pygame.image.load("dude.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player, (10, 10))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                print("ANYÁDAT")
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
