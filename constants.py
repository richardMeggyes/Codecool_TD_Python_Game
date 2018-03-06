import pygame

from maphandlers import *


class Constants:
    WIDTH, HEIGHT = 640, 480
    COLOR_WHITE = (255, 255, 255)
    COLOR_GREY = (200, 200, 200)
    COLOR_BLACK = (0, 0, 0)
    COLOR_PURPLE = (255, 0, 255)
    COLOR_RED = (255, 0, 0)
    COLOR_GREEN = (0, 255, 0)
    COLOR_BLUE = (0, 0, 255)
    level1 = import_map("Assets/level1.txt")
    grass = pygame.image.load("Assets/grass.png")
    path = pygame.image.load("Assets/path.png")
    start_path = pygame.image.load("Assets/start_path.png")
    end_path = pygame.image.load("Assets/end_path.png")
    error = pygame.image.load("Assets/error.png")
    player = pygame.image.load("Assets/enemy.png")
    tower_image = "Assets/tower1.png"
    resolution = 20
