from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x = 30, y = 30, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('effect1.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 60 or self.x > 330:
            game_world.remove_object(self)
        elif self.y < 54 or self.y > 215:
            game_world.remove_object(self)
