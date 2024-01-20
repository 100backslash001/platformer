import pygame
from abc import ABC, abstractclassmethod

from core.helpers.settigns import Colors


class IScene(ABC):
    @abstractclassmethod
    def __init__(self) -> None:
        pass
    
    @abstractclassmethod
    def draw(self) -> None:
        pass
    
    @abstractclassmethod
    def update(self) -> None:
        pass


class Scene(IScene):
    def __init__(self) -> None:
        self.display_surface: pygame.surface.Surface = pygame.display.get_surface()
        self.display_rect: pygame.Rect = self.display_surface.get_rect()

        self.quit_scene: int = pygame.USEREVENT + 1
        
        self.next_scene: Scene = None
    
    def draw(self) -> None:
        raise NotImplementedError('Draw must be overridden in child class')
    
    def update(self):
        raise NotImplementedError('Update must be overridden in child class')
 

class Level1(Scene):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(self) -> None:
        pygame.draw.rect(self.display_surface, Colors.red.value, pygame.Rect(100, 100, 200, 200))
    
    def update(self) -> None:
        event: pygame.event.Event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.next_scene: Scene = Level2()
            pygame.event.post(pygame.event.Event(self.quit_scene))


class Level2(Scene):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(self) -> None:
        pygame.draw.rect(self.display_surface, Colors.blue.value, pygame.Rect(100, 100, 200, 200))
    
    def update(self) -> None:
        event: pygame.event.Event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.next_scene: Scene = Level3()
            pygame.event.post(pygame.event.Event(self.quit_scene))
    

class Level3(Scene):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(self) -> None:
        pygame.draw.rect(self.display_surface, Colors.green.value, pygame.Rect(100, 100, 200, 200))
    
    def update(self) -> None:
        pass