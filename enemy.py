import pygame, os, sys, time

class enemy:

    def __init__(self, display, s, skin, counter, path):
        self.target_display = display
        self.place = 0
        self.speed = s
        self.skin = skin
        self.counter = counter
        self.path = path

    def draw(self):
        resolution = 20
        self.target_display.blit(self.skin, ((self.path[self.place][1] * resolution) - 10, (self.path[self.place][0] * resolution) - 10))

    def move(self):
        self.place += 1