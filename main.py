import pygame, time
from pygame.locals import *
from maphandlers import *


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
    #  Init color triplets
    white = (255,255,255)
    black = (0,0,0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    purple = (255, 0, 255)
    mainDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    level1 = import_map("Assets/level1.txt")
    grass = pygame.image.load("Assets/grass.png")
    path = pygame.image.load("Assets/path.png")
    start_path = pygame.image.load("Assets/start_path.png")
    end_path = pygame.image.load("Assets/end_path.png")
    error = pygame.image.load("Assets/error.png")
    player = pygame.image.load("Assets/tower1.png")
    resolution = 20

    pygame.display.update()

    tiles_list = get_path_from_map(level1)

    #  Gameloop
    i = 0
    delay_until = 0.0
    enemy_step_update_interval = 0.05  # Enemy előreléptetés ideje megadva másodpercben 0.05 = 20 lépés / sec

    while 1:
        # clear the mainDisplay before drawing it again
        mainDisplay.fill(0)

        for y in range(int(HEIGHT / resolution)):
            for x in range(int(WIDTH / resolution)):
                mainDisplay.blit(grass, (x * resolution, y * resolution))
        for item in tiles_list:
            mainDisplay.blit(path, (item[1] * resolution, item[0] * resolution))

        mainDisplay.blit(start_path, (tiles_list[0][0] * resolution, tiles_list[0][1] * resolution))
        mainDisplay.blit(end_path, (tiles_list[-1][0] * resolution, tiles_list[-1][1] * resolution))

        # Minden enemy_step_update_interval-ban megadott másodpercenként előrelépteti az enemyt
        i, delay_until = enemy_step_forward(enemy_step_update_interval, i, delay_until)

        # Display enemy
        mainDisplay.blit(player, ((tiles_list[i][1] * resolution) - 10, (tiles_list[i][0] * resolution) - 10))

        # a (-10)-ek az út közepére igazítják

        # update the mainDisplay
        pygame.display.update()
        # loop through the events
        for event in pygame.event.get():
            # check if the event is the X button
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)


if __name__ == "__main__":
    main()
