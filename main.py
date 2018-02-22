import pygame, time
from pygame.locals import *


def get_path_from_map(map):
    sorted_list = []

    # start tile
    for iter, row in enumerate(map):
        for iter2, col in enumerate(row):
            if col == '2':
                sorted_list.append([iter2, iter])
                break

    finished_parsing = False
    # get tiles in order
    while not finished_parsing:

        last_x = int(sorted_list[-1][0])
        last_y = int(sorted_list[-1][1])

        try:
            # Check to right
            if map[last_x + 1][last_y] == '1' and [last_x + 1, last_y] not in sorted_list:
                sorted_list.append([last_x + 1, last_y])
            elif map[last_x + 1][last_y] == '3':
                finished_parsing = True

        except:
            pass

        try:
            # Check to left
            if map[last_x - 1][last_y] == '1' and [last_x - 1, last_y] not in sorted_list:
                sorted_list.append([last_x - 1, last_y])
            elif map[last_x - 1][last_y] == '3':
                finished_parsing = True
        except:
            pass

        try:
            # Check to down
            if map[last_x][last_y + 1] == '1' and [last_x, last_y + 1] not in sorted_list:
                sorted_list.append([last_x, last_y + 1])
            elif map[last_x][last_y + 1] == '3':
                finished_parsing = True
        except:
            pass
        try:
            # Check to up
            if map[last_x][last_y - 1] == '1' and [last_x, last_y - 1] not in sorted_list:
                sorted_list.append([last_x, last_y - 1])
            elif map[last_x][last_y - 1] == '3':
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


def import_map(filename):
    return_me = []
    infile = open(filename, 'r')
    for line in infile:
        line = line.strip('\n')
        newline = []
        for c in line:
            newline.append(c)
        return_me.append(newline)
    infile.close()
    return return_me

def enemy_step_forward(enemy_step_update_interval, i, delay_until):
    if time.time() > delay_until:
        i += 1
        delay_until = time.time() + enemy_step_update_interval

    return i, delay_until

    # TODO Az enemy megjelenítést class-ba kéne rendezni, hogy egyszerre több jelenhessen meg a képernyőn, időben is kicsit eltolva egymástól
    # TODO i változót is bele kéne rakni az enemybe, mert ez mondja meg, hogy hova ugorjon
    # TODO NiceToHave: enemy glájdol egyik poziból a másikba és nem ugrál


def main():
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    level1 = import_map("Assets/level1.txt")
    grass = pygame.image.load("Assets/grass.png")
    path = pygame.image.load("Assets/path.png")
    start_path = pygame.image.load("Assets/start_path.png")
    end_path = pygame.image.load("Assets/end_path.png")
    error = pygame.image.load("Assets/error.png")
    player = pygame.image.load("Assets/tower1.png")
    resolution = 20

    pygame.display.flip()

    tiles_list = get_path_from_map(level1)

    #  Gameloop
    i = 0
    delay_until = 0.0
    enemy_step_update_interval = 0.05  # Enemy előreléptetés ideje megadva másodpercben 0.05 = 20 lépés / sec

    while 1:
        # clear the screen before drawing it again
        screen.fill(0)

        for y in range(int(HEIGHT / resolution)):
            for x in range(int(WIDTH / resolution)):
                screen.blit(grass, (x * resolution, y * resolution))
        for item in tiles_list:
            screen.blit(path, (item[1] * resolution, item[0] * resolution))

        screen.blit(start_path, (tiles_list[0][0] * resolution, tiles_list[0][1] * resolution))
        screen.blit(end_path, (tiles_list[-1][0] * resolution, tiles_list[-1][1] * resolution))

        # Minden enemy_step_update_interval-ban megadott másodpercenként előrelépteti az enemyt
        i, delay_until = enemy_step_forward(enemy_step_update_interval, i, delay_until)

        # Display enemy
        screen.blit(player, ((tiles_list[i][1] * resolution) - 10, (tiles_list[i][0] * resolution) - 10))
        # a (-10)-ek az út közepére igazítják

        # update the screen
        pygame.display.flip()
        # loop through the events
        for event in pygame.event.get():
            # check if the event is the X button
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)


if __name__ == "__main__":
    main()
