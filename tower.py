import pygame
import math
from pygame.locals import *
import time


class Tower:
    def __init__(self, display, coord_x, coord_y, image_location, bullet_speed, time_to_shoot_again):
        self.display = display
        self.image = pygame.image.load(image_location)
        self.original_image = self.image
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.SIZE = 40
        self.angle = 0
        self.rect = self.image.get_rect(center=(self.coord_x, self.coord_y))
        self.bullets = []
        self.time = time.time()
        self.time_to_shoot_again = time_to_shoot_again
        self.bullet_speed = bullet_speed
        self.range = 300
    
    def draw(self):
        self.rect = self.image.get_rect(center=(self.coord_x, self.coord_y))
        self.display.blit(self.image, self.rect)
    
    def turn_tower(self, position):
        self.angle = (180 / math.pi) * -math.atan2(position[1] - self.coord_y, position[0] - self.coord_x) - 90
        self.image = pygame.transform.rotate(self.original_image, self.angle)
    
    def shoot(self):
        if self.time + self.time_to_shoot_again < time.time():
            self.time = time.time()
            new_bullet = Projectile(self.display, self.coord_x, self.coord_y, self.angle)
            self.bullets.append(new_bullet)
        
        for i, bullet in enumerate(self.bullets):
            bullet.move(self.bullet_speed)
            
            dist = math.sqrt((self.coord_x - bullet.coord_x) ** 2 + (self.coord_y - bullet.coord_y) ** 2)
            if dist > self.range:
                self.bullets.pop(i)


class Projectile:
    def __init__(self, display, coord_x, coord_y, angle):
        self.display = display
        self.size = 10
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.angle = angle
    
    def print_projectile(self):
        pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(self.coord_x, self.coord_y, self.size, self.size))
    
    def move(self, bullet_speed):
        angle = (math.radians(self.angle) - math.pi / 2) - math.radians(90)
        x = math.sin(angle) * bullet_speed
        y = math.cos(angle) * bullet_speed
        
        self.coord_x += float(x)
        self.coord_y += float(y)


if __name__ == "__main__":
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    tower1 = Tower(screen,30, 50, "./Assets/tower1.png")
    while True:
        pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0, 0, width, height))
        tower1.turn_tower((400,300))
        tower1.draw()
        tower1.shoot()
        
        # update the screen
        pygame.display.flip()
        # loop through the events
        for event in pygame.event.get():
            
            # check if the event is the X button
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)
