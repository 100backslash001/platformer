import pygame, sys
from pygame.locals import *

from core.scenes import SceneManager, MainMenuScene
from core.settings import Settings


class Game:
    def __init__(self) -> None:
        pygame.init()

        Settings.Window.display = pygame.display.set_mode(
            (Settings.Window.width.value, Settings.Window.height.value),
            Settings.Window.flags.value,
            Settings.Window.color_depth.value,
            0,
            Settings.Window.vsync.value
        )
        pygame.display.set_caption(Settings.Window.title.value)

        self.clock = pygame.time.Clock()

        self.scene_manager = SceneManager()
        self.scene_manager.add(MainMenuScene(Settings.Scenes.MainMenu.value))
        self.scene_manager.set_scene(Settings.Scenes.MainMenu.value)

    def run(self):
        while True:
            deltatime = self.clock.tick(Settings.Window.fps.value) / 1000.0

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.scene_manager.update(deltatime)

            Settings.Window.display.fill(Settings.Colors.black.value)
            self.scene_manager.draw()
            pygame.display.update()