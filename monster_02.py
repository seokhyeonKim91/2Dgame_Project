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
ENEMY_SPEED = 0.15

player_location = []


def tracking_events1(monster):
    global player_location

    if player_location.__len__() > 0:
        if player_location[0] >= monster.x:
            monster.x += ENEMY_SPEED
            if player_location[1] >= monster.y:
                monster.y += ENEMY_SPEED
            elif player_location[1] < monster.y:
                monster.y -= ENEMY_SPEED
        elif player_location[0] < monster.x:
            monster.x -= ENEMY_SPEED
            if player_location[1] >= monster.y:
                monster.y += ENEMY_SPEED
            elif player_location[1] < monster.y:
                monster.y -= ENEMY_SPEED
    else:
        print("player_location is not has info")



class IdleState:

    def enter(monster02, event):
        print("monster Import")

    def do(monster02):
        monster02.frameTime += 1
        if(monster02.frameTime == monster02.frameTimeMax):
            monster02.frame = (monster02.frame +1) % 2
            monster02.frameTime = 0
        if(monster02.horizon):
            monster02.x += monster02.velocity * game_framework.frame_time * 100
        else:
            monster02.y += monster02.velocity * game_framework.frame_time * 100
    def draw(monster02):
        monster02.image.clip_draw(monster02.dir, monster02.frame * 30, 30, 30, monster02.x, monster02.y)


class Monster_02:
    def __init__(self):
        self.x = random.randint(61, 329)
        self.y = random.randint(54, 214)

        self.image = load_image('monster_02.png')
        self.dir = 0
        self.velocity = 0
        self.horizon = True
        self.frame = 0
        self.frameTime = 0
        self.frameTimeMax = 2
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



