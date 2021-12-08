import game_framework
from pico2d import *

class Heart:
    def __init__(self):
        self.x = 100
        self.y = 650
        self.image = load_image('heart.png')
        self.image.draw_now(600,600)