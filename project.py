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
        tracking_events1()
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
        self.image.clip_draw(0, self.frame * 30, 30, 30, self.a, self.b)

class Monster02:
    def __init__(self):
        self.a, self.b = random.randint(51, 329), random.randint(54, 214)
        self.frame = 0
        self.image = load_image('monster_02.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        tracking_events2()
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
        self.image.clip_draw(0, self.frame * 30, 30, 30, self.a, self.b)

class Ranger_Monster:
    def __init__(self):
        self.a, self.b = random.randint(51, 329), random.randint(54, 214)
        self.frame = 0
        self.image = load_image('monster_03.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        #traking_rmon_effect()
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
        self.image.clip_draw(0, self.frame * 30, 30, 30, self.a, self.b)


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
                dir_hero += 90
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                dir_hero = 0
                dir_hero += 30
            elif event.key == SDLK_UP:
                dir_y += 1
                dir_hero = 0
                dir_hero += 60
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

def pattack():
    player.image = load_image('link_attack.png')
    player.image.clip_draw(0 + dir_hero, player.frame * 30, 30, 30, player.x, player.y)

def tracking_events1():
    if player.x >= monster1.a:
        monster1.a += 3
        if player.y >= monster1.b:
            monster1.b += 3
        elif player.y < monster1.b:
            monster1.b -= 3
    elif player.x < monster1.a:
        monster1.a -= 3
        if player.y >= monster1.b:
            monster1.b += 3
        elif player.y < monster1.b:
            monster1.b -= 3

def tracking_events2():
    if player.x >= monster2.a:
        monster2.a += 1
        if player.y >= monster2.b:
            monster2.b += 1
        elif player.y < monster2.b:
            monster2.b -= 1
    elif player.x < monster2.a:
        monster2.a -= 1
        if player.y >= monster2.b:
            monster2.b += 1
        elif player.y < monster2.b:
            monster2.b -= 1

def traking_rmon_effect():
    ran_effect = load_image('effect.png')
    ran_effect.image.clip_draw(0 + dir_hero, ranger_monster.frame * 30, 30, 30, ranger_monster.a, ranger_monster.b)
    if player.x > ranger_monster.a:
        ranger_monster.a += 5
        if player.y >= ranger_monster.b:
            ranger_monster.b += 5
        elif player.y < ranger_monster.b:
            ranger_monster.b -= 5
    elif player.x < ranger_monster.a:
        ranger_monster.a -= 5
        if player.y >= ranger_monster.b:
            ranger_monster.b += 5
        elif player.y < ranger_monster.b:
            ranger_monster.b -= 5
    #elif player.x == ranger_monster.a and player.y == ranger_monster.b:
        #ran_effect = False

# initialization code
open_canvas(resolution_width, resolution_height)

running = True
player = Player()
monster1 = Monster01()
monster2 = Monster02()
ranger_monster = Ranger_Monster()
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
    monster2.update()
    ranger_monster.update()

    dungeon01.draw()
    player.draw()
    monster1.draw()
    monster2.draw()
    ranger_monster.draw()

    handle_events()
    update_canvas()
    delay(0.05)
close_canvas()