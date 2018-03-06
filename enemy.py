import pygame, os, sys, time


class Enemy:

    def __init__(self, display, skin, counter, path, hp=1):
        self.target_display = display
        self.place = 0
        self.speed = 1
        self.skin = skin
        self.counter = counter
        self.path = path
        self.position = (0, 0)
        self.resolution = 20
        self.hitpoints = hp
    
    def calc_position(self):
        self.position =((self.path[self.place][1] * self.resolution), (self.path[self.place][0] *
                                                                            self.resolution))
    
        
    def draw(self):
        self.calc_position()
        self.target_display.blit(self.skin, self.position)
    
    def move(self):
        self.place += 1
