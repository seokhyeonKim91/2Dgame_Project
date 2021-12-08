from pico2d import *
resolution_width, resolution_height = 1280, 720

class Map_01:
    def __init__(self):
        self.image = load_image('dungeon.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(resolution_width // 2, resolution_height // 2)
