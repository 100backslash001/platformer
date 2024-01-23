import importlib
import pygame as pg
from abc import ABC, abstractmethod

from core.settings import Settings
from core.helper import AssetLoader
from core.objects import Background


class Scene(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def update(self, deltatime):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass


class MainMenuScene(Scene):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.background = Background()
        self.gui_generator = AssetLoader.import_layout('./layouts/gui.csv')
        self.ui_elements = []

        for element in self.gui_generator:
            element_name = element[0]
            args = element[1:]

            ui = importlib.import_module('core.ui')
            cls = getattr(ui, element_name)
            self.ui_elements.append(cls(*args))

    def enter(self):
        print("Entering main menu")

    def exit(self):
        print("Exiting main menu")
    
    def update(self, deltatime):
        pass

    def draw(self):
        Settings.Window.display.fill(Settings.Colors.white.value)
        self.background.draw()

        for element in self.ui_elements:
            element.draw()

    def handle_events(self, events):
        return super().handle_events(events)

class SceneManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        self.scenes = {}
        self.current_scene = None
    
    def add(self, scene: Scene):
        self.scenes[scene.name] = scene
    
    def set_scene(self, scene_name):
        if self.current_scene:
            self.current_scene.exit()
        
        self.current_scene = self.scenes.get(scene_name)

        if self.current_scene:
            self.current_scene.enter()
    
    def update(self, deltatime):
        if self.current_scene:
            self.current_scene.update(deltatime)
    
    def draw(self):
        if self.current_scene:
            self.current_scene.draw()
    
    def handle_events(self, events):
        if self.current_scene:
            self.current_scene.handle_events(events)