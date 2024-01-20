import pygame, sys
from pygame.locals import *

from core.helpers.settigns import *
from core.scenes.scene_manager import SceneManager
from core.scenes.levels import Level1


class Game:
    def __init__(self) -> None:
        pygame.init()
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Test')
        
        self.clock = pygame.time.Clock()
        
        self.scene_manager = SceneManager()
        self.scene_manager.add_scene(Level1())

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                 
                if event.type == SceneEvents.quit_scene.value:
                    self.scene_manager.remove_scene(self.scene_manager.current_scene)
                    
            self.scene_manager.update_scenes()
             
            self.screen.fill(Colors.black.value)
            self.scene_manager.draw_scenes()
            pygame.display.update()
            self.clock.tick(FPS)