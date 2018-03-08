import pygame, os, sys, time
from constants import *


class Enemy:
    
    def __init__(self, display, skin, counter, path, hp=5):
        self.target_display = display
        self.place = 0
        self.speed = 1
        self.skin = skin
        self.counter = counter
        self.path = path
        self.position = (0, 0)
        self.hitpoints = hp
        self.maxhp = hp
    
    def calc_position(self):
        self.position = (
            (self.path[self.place][1] * Constants.resolution), (self.path[self.place][0] * Constants.resolution))
    
    def draw(self):
        self.calc_position()
        self.target_display.blit(self.skin, self.position)
        
        # health bar
        max_length = 25  # px
        current_length = (self.hitpoints / self.maxhp) * max_length
        bar_height = 5
        offset_y = 10
        # background
        pygame.draw.rect(self.target_display, Constants.COLOR_GREY,
                         (self.position[0] - max_length / 2 + Constants.resolution / 2,
                          self.position[1] - offset_y, max_length, bar_height))
        pygame.draw.rect(self.target_display, Constants.COLOR_GREEN,
                         (self.position[0] - max_length / 2 + Constants.resolution / 2,
                          self.position[1] - offset_y, current_length, bar_height))
    
    def move(self):
        self.place += 1
