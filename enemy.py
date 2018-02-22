import pygame, os, sys, time


class Enemy:
    
    def __init__(self, display, s, skin, counter, path):
        self.target_display = display
        self.place = 0
        self.speed = s
        self.skin = skin
        self.counter = counter
        self.path = path
        self.position = (0,0)
        self.resolution = 20
    
    def calc_position(self):
        self.position =((self.path[self.place][1] * self.resolution) - 10, (self.path[self.place][0] *
                                                                            self.resolution) - 10)
    
        
    def draw(self):
        self.calc_position()
        self.target_display.blit(self.skin, self.position)
    
    def move(self):
        self.place += 1
