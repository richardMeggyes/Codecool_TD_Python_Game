import pygame


import tkinter
import pygame
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
map1=[]
infile = open("level.txt", 'r')
for line in infile:
    line = line.strip('\n')
    map1.append(line)
infile.close()

grass = pygame.image.load("grass.png")
path = pygame.image.load("path.png")
error = pygame.image.load("error.png")
res = 20

pygame.display.flip()
#print(map1)



#  Gameloop
while 1:
    # 5   clear the screen before drawing it again
    #screen.fill(0)
    for x in range(int(width / res)):
        for y in range(int(height / res)):
            if (map1[y][x] == '0'):  # 0 means grass
                screen.blit(grass, (x * res, y * res))
            elif (map1[y][x] == '1'):  # 1 means path
                screen.blit(path, (x * res, y * res))
            else:
                screen.blit(error, (x*res, y*res))

    # update the screen
    pygame.display.flip()
    # loop through the events
    for event in pygame.event.get():


        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 

