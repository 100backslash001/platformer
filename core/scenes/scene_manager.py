import pygame


class SceneManager:
    def __init__(self) -> None:
        self.scenes = []
        self.current_scene = None
    
    def add_scene(self, scene=None, remove_previous=False):
        if remove_previous and not self.is_empty():
            self.remove_scene(self.scenes[-1])

        self.scenes.append(scene)
        self.current_scene = scene
        
    def remove_scene(self, scene=None):
        if scene is None and self.current_scene is None:
            raise Exception('Nothing to remove')
        
        if scene == self.current_scene:
            self.scenes.pop(self.scenes.index(scene))

        if scene is not None and scene.next_scene:
            self.add_scene(scene.next_scene, True)
            
        
    def is_empty(self):
        return len(self.scenes) < 1
    
    def draw_scenes(self):
        for scene in self.scenes:
            scene.draw()
    
    def update_scenes(self):
        for scene in self.scenes:
            scene.update()