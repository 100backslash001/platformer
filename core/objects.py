import pygame as pg

from core.helper import AssetLoader
from core.settings import Settings

class Background(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pg.transform.scale(
            AssetLoader.load_image('Background.png'),
            (
                Settings.Window.width.value,
                Settings.Window.height.value
            )
        )
        self.rect = self.image.get_rect(topleft=(0, 0))
    
    def draw(self):
        Settings.Window.display.blit(self.image, self.rect)