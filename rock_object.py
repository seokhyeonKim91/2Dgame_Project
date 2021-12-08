import game_framework
from pico2d import *
import random

class Rock_object:
    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 20
        return 0, 0, 0, 0