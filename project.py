from pico2d import *
import random
resolution_width, resolution_height = 384, 264

class Player:
    def __init__(self):
        self.x, self.y = 192, 60
        self.frame = 0
        self.image = load_image('link_run1.png')

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
        self.image.clip_draw(0 + dir_hero, self.frame * 30, 30, 30, self.x, self.y)


class Dungeon01:
    def __init__(self):
        self.image = load_image('dungeon_1.png')
    def draw(self):
        self.image.draw(resolution_width // 2, resolution_height // 2)

class Monster01:
    def __init__(self):
        self.a, self.b = random.randint(51, 329), random.randint(54, 214)
        self.frame = 0
        self.image = load_image('monster_01.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        #tracking_events()
        #collison check
        if self.a >= 330:
            self.a = 329
        elif self.a <= 50:
            self.a = 51
        elif self.b >= 215:
            self.b = 214
        elif self.b <= 55:
            self.b = 54

    def draw(self):
        self.image.clip_draw(0, self.frame * 32, 16, 32, self.a, self.b)

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
            elif event.key == SDLK_z:
                pattack()
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
            elif event.key == SDLK_z:
                player.image = load_image('link_run1.png')


    pass

def tracking_events():
    global mondir_x
    global mondir_y
    for event in events:
        if player.x >= monster1.a:
            monster1.a += 1
            if player.y >= monster1.b:
                monster1.b += 1
            elif player.y < monster1.b:
                monster1.b -= 1
        elif player.x < monster1.a:
            monster1.a -= 1
            if player.y >= monster1.b:
                monster1.b += 1
            elif player.y < monster1.b:
                monster1.b -= 1

def pattack():
    player.image = load_image('link_attack.png')
    player.image.clip_draw(0 + dir_hero, player.frame * 30, 30, 30, player.x, player.y)

# initialization code
open_canvas(resolution_width, resolution_height)

running = True
player = Player()
monster1 = Monster01()
#monster_team01 = [Monster01() for i in range(4)]
dungeon01 = Dungeon01()
dir_x = 0
dir_y = 0
mondir_x = 0
mondir_y = 0
dir_hero = 0
hide_cursor()

# game main loop code

while running:
    clear_canvas()

    player.update()
    monster1.update()
    #for monster01 in monster_team01:
    #    monster01.update()

    dungeon01.draw()
    player.draw()
    monster1.draw()
    #for monster01 in monster_team01:
    #    monster01.draw()

    handle_events()
    #tracking_events()
    update_canvas()
    delay(0.05)
close_canvas()