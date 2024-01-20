import pygame
from enum import Enum


WIDTH = 1280
HEIGHT = 720
FPS = 60

class Colors(Enum):
    #        R      G    B
    black = (0,     0,   0)
    white = (255, 255, 255)
    red   = (255,   0,   0)
    green = (0,   255,   0)
    blue  = (0,     0, 255)


class SceneEvents(Enum):
    quit_scene = pygame.USEREVENT + 1