import pygame as pg

from core.settings import Settings


class Button:
    def __init__(
        self,
        x, y,
        width, height,
        title, font_size
    ) -> None:
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.title = title
        self.font_size = int(font_size)
    
    def draw(self):
        pg.draw.rect(Settings.Window.display, Settings.Colors.red.value, pg.Rect(self.x, self.y, self.width, self.height))