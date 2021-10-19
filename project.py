from pico2d import *
import random
resolution_width, resolution_height = 384, 264

class Player:
    def __init__(self):
        self.x, self.y = 192, 60
        self.frame = 0
        self.image = load_image('link_run.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += dir_x * 5
        self.y += dir_y * 5
        #collison check
        if player.x >= 330:
            player.x = 329
        elif player.x <= 50:
            player.x = 51
        elif player.y >= 215:
            player.y = 214
        elif player.y <= 55:
            player.y = 54

    def draw(self):
        self.image.clip_draw(0 + dir_hero, self.frame * 32, 16, 32, self.x, self.y)


class Dungeon01:
    def __init__(self):
        self.image = load_image('dungeon_1.png')
    def draw(self):
        self.image.draw(resolution_width // 2, resolution_height // 2)


def handle_events():
    global running
    global dir_x
    global dir_y
    global dir_hero
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                dir_hero = 0
                dir_hero += 84
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                dir_hero = 0
                dir_hero += 28
            elif event.key == SDLK_UP:
                dir_y += 1
                dir_hero = 0
                dir_hero += 56
            elif event.key == SDLK_DOWN:
                dir_hero = 0
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

    pass

# initialization code
open_canvas(resolution_width, resolution_height)

running = True
player = Player()
dungeon01 = Dungeon01()
dir_x = 0
dir_y = 0
dir_hero = 0
hide_cursor()

# game main loop code

while running:
    player.update()
    clear_canvas()
    dungeon01.draw()
    player.draw()
    handle_events()
    update_canvas()
    delay(0.05)
close_canvas()