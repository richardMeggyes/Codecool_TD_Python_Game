import math
import time
from constants import *
import pygame


class Tower:
    def __init__(self, display, position, bullet_speed=9, time_to_shoot_again=0.2,
                 image_location=Constants.tower_image):
        self.display = display
        self.image = pygame.image.load(image_location)
        self.original_image = self.image
        self.position = position
        self.SIZE = 40
        self.angle = 0
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
        self.bullets = []
        self.time = time.time()
        self.time_to_shoot_again = time_to_shoot_again
        self.bullet_speed = bullet_speed
        self.range = 300
        self.valid_target = False
    
    def draw(self):
        self.rect = self.image.get_rect(center=self.position)
        self.display.blit(self.image, self.rect)
    
    def turn_tower(self, position):
        self.angle = (180 / math.pi) * -math.atan2(position[1] - self.position[1], position[0] - self.position[0]) - 90
        self.image = pygame.transform.rotate(self.original_image, self.angle)
    
    def shoot(self):
        if self.time + self.time_to_shoot_again < time.time():
            self.time = time.time()
            if self.valid_target:
                new_bullet = Projectile(self.display, self.position[0], self.position[1], self.angle)
                self.bullets.append(new_bullet)
        
        for i, bullet in enumerate(self.bullets):
            bullet.move(self.bullet_speed)
            
            dist = math.sqrt(
                (self.position[0] - bullet.position[0]) ** 2 + (self.position[1] - bullet.position[1]) ** 2)
            if dist > self.range:
                self.bullets.pop(i)


class Projectile:
    def __init__(self, display, coord_x, coord_y, angle, dmg=1, image_location=Constants.bullet_image):
        self.display = display
        self.size = 10
        self.position = (coord_x, coord_y)
        self.angle = angle
        self.damage = dmg
        self.image = pygame.image.load(image_location)
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
    
    def print_projectile(self):
        # pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(self.position[0], self.position[1], self.size,
        # self.size))
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
        self.display.blit(self.image, self.rect)
    
    def move(self, bullet_speed):
        angle = (math.radians(self.angle) - math.pi / 2) - math.radians(90)
        x = math.sin(angle) * bullet_speed
        y = math.cos(angle) * bullet_speed
        
        self.position = (self.position[0] + float(x), self.position[1] + float(y))


if __name__ == "__main__":
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    tower1 = Tower(screen, 30, 50, "./Assets/tower1.png")
    while True:
        pygame.draw.rect(screen, constants.COLOR_GREY(), pygame.Rect(0, 0, width, height))
        tower1.turn_tower((400, 300))
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
