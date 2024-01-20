import pygame
from enum import Enum


WIDTH: int = 1280
HEIGHT: int = 720
FPS: int = 60

class Colors(Enum):
    #        R      G    B
    black: tuple = (0,     0,   0)
    white: tuple = (255, 255, 255)
    red: tuple   = (255,   0,   0)
    green: tuple = (0,   255,   0)
    blue: tuple  = (0,     0, 255)


class SceneEvents(Enum):
    quit_scene: int = pygame.USEREVENT + 1