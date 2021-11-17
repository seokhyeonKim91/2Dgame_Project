import game_framework
from pico2d import *
import random


class Player:

    def __init__(self):
        self.x = random.randint(51, 329)
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



    def add_event(self, event):
        self.event_que.insert(0, event)



    def update(self):
        # 스테이트는 아이들밖에 없으므로 우선 생략
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            #self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)



    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir))



