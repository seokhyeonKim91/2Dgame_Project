from pico2d import *
resolution_width, resolution_height = 384, 264

class Map_01:
    def __init__(self):
        self.image = load_image('dungeon_1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(resolution_width // 2, resolution_height // 2)
