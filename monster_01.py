import game_framework
from pico2d import *
import random

PIXEL_PER_METER = (1.0 / 0.3)
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
ENEMY_SPEED = 0.1

player_location = []


def tracking_events1(monster):
    global player_location

    if player_location.__len__() > 0:
        if player_location[0] >= monster.x:
            monster.x += ENEMY_SPEED
            monster.dir = 0
            if player_location[1] > monster.y:
                monster.y += ENEMY_SPEED
                monster.dir = 0
                monster.dir += 64
            elif player_location[1] < monster.y:
                monster.y -= ENEMY_SPEED
                monster.dir = 0
                monster.dir += 192
        elif player_location[0] < monster.x:
            monster.x -= ENEMY_SPEED
            monster.dir = 0
            monster.dir += 128
            if player_location[1] > monster.y:
                monster.y += ENEMY_SPEED
                monster.dir = 0
                monster.dir += 64
            elif player_location[1] < monster.y:
                monster.y -= ENEMY_SPEED
                monster.dir = 0
                monster.dir += 192
        #elif player_location[1] == monster.y:
        #    if player_location[0] > monster.x:
        #        monster.dir = 0
        #        monster.dir += 192
        #    elif player_location[0] < monster.x:
        #        monster.dir = 0
        #        monster.dir += 64


    else:
        print("player_location is not has info")



class IdleState:

    def enter(monster01, event):
        print("monster Import")

    def do(monster01):
        monster01.frameTime += 1
        if(monster01.frameTime == monster01.frameTimeMax):
            monster01.frame = (monster01.frame +1) % 4
            monster01.frameTime = 0
        if(monster01.horizon):
            monster01.x += monster01.velocity * game_framework.frame_time * 100
        else:
            monster01.y += monster01.velocity * game_framework.frame_time * 100
    def draw(monster01):
        monster01.image.clip_draw(monster01.frame * 64, monster01.dir, 64, 64, monster01.x, monster01.y)


class Monster_01:
    def __init__(self):
        self.x = random.randint(144, 1132)
        self.y = random.randint(106, 659)

        self.health = 3

        self.image = load_image('monster_01.png')
        self.dir = 0
        self.velocity = 0
        self.horizon = True
        self.frame = 0
        self.frameTime = 0
        self.frameTimeMax = 80
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)



    #def add_event(self, event):
    #   self.event_que.insert(0, event)

    def get_player_location(self, player_x, player_y):
        global player_location
        player_location = [player_x, player_y]
        print("x : %f, y : %f" % (player_location[0], player_location[1]))


    def update(self):
        self.cur_state.do(self)
        tracking_events1(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            #self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 30
        return 0, 0, 0, 0

    def stop(self):
        self.velocity = 0
        self.y_velocity = 0

    def knockback(self, x, y):
        self.x += x
        self.y += y
        self.health -= 1
        if self.health == 0:
            return True
        else:
            return False



