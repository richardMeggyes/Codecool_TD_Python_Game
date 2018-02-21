import pygame


import tkinter
import pygame
from pygame.locals import *

def convert_map(map):
    map_list = []
    sorted_list = []

    # start tile
    for iter, row in enumerate(map):
        for iter2, col in enumerate(row):
            if col == '2':
                sorted_list.append([iter2, iter])
                break


    finished_parsing = False

    while not finished_parsing:

        last_x = int(sorted_list[-1][0])
        last_y = int(sorted_list[-1][1])

        try:
            # érts: Ha az utolsó elem 0. kordinátája +1-en és 1. kordinátáján 1-es van:
            if map[last_x + 1][last_y] == '1' and [last_x + 1, last_y] not in sorted_list:
                sorted_list.append([last_x + 1, last_y])
                #print(sorted_list[-1], '\n')
            elif map[last_x + 1][last_y] == '3':
                finished_parsing = True

        except:
            pass

        try:
            if map[last_x-1][last_y] == '1'and [last_x - 1, last_y] not in sorted_list:
                sorted_list.append([last_x - 1, last_y])
                #print(sorted_list[-1], '\n')
            elif map[last_x - 1][last_y] == '3':
                finished_parsing = True
        except:
            pass


        try:
            # érts: Ha az utolsó elem 0. kordinátáján és 1. kordinátája + 1-en 1-es van:
            if map[last_x][last_y + 1] == '1' and [last_x, last_y + 1] not in sorted_list:
                sorted_list.append([last_x, last_y + 1])
                #print(sorted_list[-1], '\n')
            elif map[last_x][last_y + 1] == '3':
                finished_parsing = True
        except:
            pass
        try:
            # érts: Ha az utolsó elem 0. kordinátáján és 1. kordinátája - 1-en 1-es van:
            if map[last_x][last_y - 1] == '1' and [last_x, last_y - 1] not in sorted_list:
                sorted_list.append([last_x, last_y -1])
                #print(sorted_list[-1], '\n')
            elif map[last_x][last_y - 1]  == '3':
                finished_parsing = True
        except:
            pass

    # end tile
    for iter, row in enumerate(map):
        for iter2, col in enumerate(row):

            if col == '3':
                sorted_list.append([iter2, iter])
                break


    return sorted_list




def main():
    pygame.init()
    width, height = 640, 480
    screen=pygame.display.set_mode((width, height))
    map1=[]
    infile = open("level.txt", 'r')
    for line in infile:
        line = line.strip('\n')
        newline = []
        for c in line:
            newline.append(c)
        map1.append(newline)
    infile.close()


    print(convert_map(map1))


    grass = pygame.image.load("grass.png")
    path = pygame.image.load("path.png")
    start_path = pygame.image.load("start_path.png")
    end_path = pygame.image.load("end_path.png")
    error = pygame.image.load("error.png")
    res = 20

    pygame.display.flip()


    #  Gameloop
    while 1:
    # clear the screen before drawing it again
        screen.fill(0)
        tiles_list = convert_map(map1)

        for y in range(int(height / res)):
            for x in range(int(width / res)):
                screen.blit(grass, (x * res, y * res))
        for item in tiles_list:
            screen.blit(path, (item[1]*res, item[0]*res))

        screen.blit(start_path, (tiles_list[0][0]*res, tiles_list[0][1]*res))
        screen.blit(end_path, (tiles_list[-1][0]*res, tiles_list[-1][1]*res))


        # update the screen
        pygame.display.flip()
        # loop through the events
        for event in pygame.event.get():
        # check if the event is the X button
            if event.type==pygame.QUIT:
        # if it is quit the game
               pygame.quit()
               exit(0)


main()