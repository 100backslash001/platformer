from enum import Enum


class Settings:
    class Window(Enum):
        def __init__(self, value) -> None:
            super().__init__()
            self.display = None

        width = 1280
        flags = 0
        vsync = 1
        color_depth = 32
        height = 720
        fps = 60
        title = 'Little Platform'

    class Colors(Enum):
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 255, 255)
    
    class Scenes(Enum):
        MainMenu = 'MainMenu'