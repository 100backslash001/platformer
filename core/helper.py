import os
import pygame as pg

from csv import reader


class AssetLoader:
    @staticmethod
    def load_image(image_name):
        for dirpath, __, filenames in os.walk('./assets'):
            for filename in filenames:
                if filename == image_name:
                    image_path = os.path.join(dirpath, filename)
                    try:
                        img_surface = pg.image.load(image_path)

                        return img_surface
                    except:
                        print(f"Invalid image file: {image_path}")
        
        return None
    
    @staticmethod
    def import_layout(path):
        with open(path) as csv_file:
            layout = reader(csv_file, delimiter=',')

            for line in layout:
                yield line