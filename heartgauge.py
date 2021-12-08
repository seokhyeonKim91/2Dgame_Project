import game_framework
from pico2d import *

class Health:



    def __init__(self):
        self.image = load_image('heart.png')
        self.num_of_heart = 0

    def draw(self):
       for i  in range(0, self.num_of_heart):
            self.image.draw(50 + 50 * i, 670)

    def update(self):
        print("health update 능이버섯")

    def update_heart(self, num):
        self.num_of_heart = num
