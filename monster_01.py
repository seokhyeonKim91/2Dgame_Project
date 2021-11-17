import game_framework
from pico2d import *
import random
import player

PIXEL_PER_METER = (1.0 / 0.3)
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class IdleState:
    def do(monster01):
        monster01.frameTime += 1
        if(monster01.frameTime == monster01.frameTimeMax):
            monster01.frame = (monster01.frame +1) % 2
            monster01.frameTime = 0
        if(monster01.horizon):
            monster01.x += monster01.velocity * game_framework.frame_time * 100
        else:
            monster01.y += monster01.velocity * game_framework.frame_time * 100
    def draw(monster01):
        monster01.image.clip_draw(monster01.dir, monster01.frame * 30, 30, 30, monster01.x, monster01.y)





class Monster_01:
    def __init__(self):
        self.x = random.randint(61, 329)
        self.y = random.randint(54, 214)

        self.image = load_image('monster_01.png')
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



    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            #self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)



