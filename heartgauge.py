import game_framework
import player
from pico2d import *

class Health:
    def __init__(self):
        self.image = load_image('heart.png')

    def draw(self):
        count = player.Player.health
        for i in count:
            self.image.draw_now(100 * i, 600)

