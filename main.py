import pygame, time
from pygame.locals import *
from maphandlers import *
from simplebutton import *
from enemy import *
from tower import *


def enemy_step_forward(enemy_step_update_interval, i, delay_until):
    if time.time() > delay_until:
        i += 1
        delay_until = time.time() + enemy_step_update_interval
    return i, delay_until
    
    # TODO Az enemy megjelenítést class-ba kéne rendezni, hogy egyszerre több jelenhessen meg a képernyőn,
    # időben is kicsit eltolva egymástól
    # TODO i változót is bele kéne rakni az enemybe, mert ez mondja meg, hogy hova ugorjon
    # TODO NiceToHave: enemy glájdol egyik poziból a másikba és nem ugrál


#  W-i-P gameloop separated for testing purposes
""" 
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

    # a (-10)-ek az út közepére igazítják   """


def main():
    pygame.init()
    pygame.font.init()
    
    WIDTH, HEIGHT = 640, 480
    
    #  Init color triplets
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    purple = (255, 0, 255)
    something_less_eye_cancery = (150, 150, 150)
    mainDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("CC- Tower Defense")
    level1 = import_map("Assets/level1.txt")
    grass = pygame.image.load("Assets/grass.png")
    path = pygame.image.load("Assets/path.png")
    start_path = pygame.image.load("Assets/start_path.png")
    end_path = pygame.image.load("Assets/end_path.png")
    error = pygame.image.load("Assets/error.png")
    player = pygame.image.load("Assets/enemy.png")
    tower_image = "Assets/tower1.png"
    resolution = 20
    
    pygame.display.update()
    
    tiles_list = get_path_from_map(level1)
    
    clock = pygame.time.Clock()
    clock_counter = 0
    # Gameloop
    i = 0
    delay_until = 0.0
    enemy_step_update_interval = 2  # Enemy előreléptetés ideje megadva másodpercben 0.05 = 20 lépés / sec
    widgets = []
    widgets.append(button(mainDisplay, 100, 100, 100, 50, "New Game", green, red, do_nothing))
    widgets.append(button(mainDisplay, 400, 100, 100, 50, "Exit", red, blue, pygame.quit, exit))
    
    enemies = []
    speed = 1
    # enemies.append(Enemy(mainDisplay, speed, player, 0, tiles_list))
    
    towers = []
    towers.append(Tower(mainDisplay, 80, 80, tower_image, 9, 0.2))
    
    while 1:
        # clear the mainDisplay before drawing it again
        mainDisplay.fill(something_less_eye_cancery)

        """if time.time() > delay_until:
            delay_until = time.time() + enemy_step_update_interval
            enemies.append(Enemy(mainDisplay, speed, player, 0, tiles_list))"""
        
        for t in towers:
            if not enemies:
                target = (0, 0)
                valid_target = False
            else:
                target = enemies[0].position
                valid_target = True
            last_distance = 10000
            for e in enemies:
                dist_squared = (t.coord_x - e.position[0]) ** 2 + (t.coord_x - e.position[0]) ** 2
                if dist_squared < last_distance and dist_squared < t.range ** 2:
                    last_distance = dist_squared
                    target = e.position
            
            t.turn_tower(target)
            t.shoot()
            if not enemies:
                t.valid_target = False
            else:
                t.valid_target = True
        
        # loop through the events
        for event in pygame.event.get():
            # All the logic of the game should be decided here, and later processed after this FOR
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for w in widgets:
                    w.pressed(pos[0], pos[1])
            #  Sample key handling for press and release of a specified button (be it mouse or keyboard)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    enemies.append(Enemy(mainDisplay, speed, player, 0, tiles_list))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    enemies = []
            
            # check if the event is the X button
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)
        
        for i, e in enumerate(enemies):
            if e.place == len(tiles_list) - 1:
                enemies.pop(i)
            if clock_counter % 6 == 0:
                e.move()
        
        # update the mainDisplay
        # for w in widgets:
        #    w.draw(mainDisplay)
        for y in range(int(HEIGHT / resolution)):
            for x in range(int(WIDTH / resolution)):
                mainDisplay.blit(grass, (x * resolution, y * resolution))
        for item in tiles_list:
            mainDisplay.blit(path, (item[1] * resolution, item[0] * resolution))

        mainDisplay.blit(start_path, (tiles_list[0][0] * resolution, tiles_list[0][1] * resolution))
        mainDisplay.blit(end_path, (tiles_list[-1][0] * resolution, tiles_list[-1][1] * resolution))

        for e in enemies:
            e.draw()
        for t in towers:
            t.draw()
            for bullet in t.bullets:
                bullet.print_projectile()
        pygame.display.update()
        # set a specific framerate of the display/meaning that every second there will be () ticks of the while
        clock_counter += 1
        if clock_counter == 60:
            clock_counter = 0
        clock.tick(60)


if __name__ == "__main__":
    main()
