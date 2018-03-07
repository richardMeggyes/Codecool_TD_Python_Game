from tkinter import *

from constants import *
from enemy import *
from tower import *
from math import sqrt


# TODO NiceToHave: enemy glájdol egyik poziból a másikba és nem ugrál

def donothing():
    print("Doing nothing like a pro")
    pass


def calc_distance_squared(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def collisiondetection(enemies, towers):
    for enemy in enemies:
        for t_iter, tower in enumerate(towers):
            for b_iter, bullet in enumerate(tower.bullets):
                squared_distance = calc_distance_squared(enemy.position, bullet.position)
                # print(enemy.position, bullet.position, squared_distance)
                # print(squared_distance)
                if squared_distance < 50:
                    enemy.hitpoints -= bullet.damage
                    towers[t_iter].bullets.pop(b_iter)


def gameloop():
    pygame.init()
    pygame.font.init()
    
    mainDisplay = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption("CC- Tower Defense")
    
    pygame.display.update()
    
    tiles_list = get_path_from_map(Constants.level1)
    
    clock = pygame.time.Clock()
    clock_counter = 0
    
    # Gameloop
    
    enemies = []
    towers = []
    
    # Sample tower for testing purposes only
    towers.append(Tower(mainDisplay, (400, 130), Constants.tower_image, 9, 0.2))
    towers.append(Tower(mainDisplay, (200, 130), Constants.tower_image, 9, 0.2))
    towers.append(Tower(mainDisplay, (400, 300), Constants.tower_image, 9, 0.2))
    gameon = True
    while gameon:
        # clear the mainDisplay before drawing it again
        mainDisplay.fill(Constants.COLOR_GREY)
        
        for t in towers:
            if not enemies:
                target = tiles_list[0]
                t.valid_target = False
            else:
                for e in reversed(enemies):
                    dist_squared = calc_distance_squared(e.position, t.position)
                    if dist_squared < t.range:
                        target = e.position
                        t.valid_target = True
                        break
            
            t.turn_tower(target)
            t.shoot()
        
        # loop through the events
        for event in pygame.event.get():
            # All the logic of the game should be decided here, and later processed after this FOR
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    enemies.append(Enemy(mainDisplay, Constants.player, 0, tiles_list))
                
                if event.key == pygame.K_BACKSPACE:
                    enemies = []
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    gameon = False
                    # exit(0)
            
            # check if the event is the X button
            if event.type == pygame.QUIT:
                pygame.quit()
                gameon = False
                # exit(0)
        collisiondetection(enemies, towers)
        
        for iter, enemy in enumerate(enemies):
            if enemy.hitpoints < 1:
                enemies.pop(iter)
        
        for i, e in enumerate(enemies):
            if e.place == len(tiles_list) - 1:
                enemies.pop(i)
            if clock_counter % 6 == 0:
                e.move()
        
        # update the mainDisplay
        
        for y in range(int(Constants.HEIGHT / Constants.resolution)):
            for x in range(int(Constants.WIDTH / Constants.resolution)):
                mainDisplay.blit(Constants.grass, (x * Constants.resolution, y * Constants.resolution))
        for item in tiles_list:
            mainDisplay.blit(Constants.path, (item[1] * Constants.resolution, item[0] * Constants.resolution))
        
        mainDisplay.blit(Constants.start_path,
                         (tiles_list[0][0] * Constants.resolution, tiles_list[0][1] * Constants.resolution))
        mainDisplay.blit(Constants.end_path,
                         (tiles_list[-1][0] * Constants.resolution, tiles_list[-1][1] * Constants.resolution))
        
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
    pygame.display.quit()
    pygame.quit()


def createmap():
    pass


def menuloop():
    menu = Tk()
    menu.geometry("%dx%d+0+0" % (Constants.WIDTH, Constants.HEIGHT))
    label1 = Label(menu, text="CC Tower Defense")
    label1.config(font=('Arial', '40'))
    label1.pack(side=TOP, pady=20)
    newgamebutton = Button(menu, text="New Game", command=gameloop)
    newgamebutton.pack(pady=20, padx=60, fill=X)
    # createmapbutton = Button(menu, text="Create new map", command=donothing)
    # createmapbutton.pack(pady=20, padx=60, fill=X)
    exitbutton = Button(menu, text="Exit", command=exit)
    exitbutton.pack(pady=20, padx=60, fill=X)
    menu.mainloop()


def main():
    menuloop()


if __name__ == "__main__":
    main()
