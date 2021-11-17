import game_framework
from pico2d import *
import random
from fireball import Ball
import game_world

PIXEL_PER_METER = (1.0 / 0.3)
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
ENEMY_SPEED = 0.2

player_location = []


def tracking_events1(ball):
    global player_location

    if player_location.__len__() > 0:
        if player_location[0] >= ball.x:
            ball.x += ENEMY_SPEED
            if player_location[1] >= ball.y:
                ball.y += ENEMY_SPEED
            elif player_location[1] < ball.y:
                ball.y -= ENEMY_SPEED
        elif player_location[0] < ball.x:
            ball.x -= ENEMY_SPEED
            if player_location[1] >= ball.y:
                ball.y += ENEMY_SPEED
            elif player_location[1] < ball.y:
                ball.y -= ENEMY_SPEED
    else:
        print("player_location is not has info")



class IdleState:

    def enter(monster03, event):
        monster03.fire_ball()
        tracking_events1(Ball)

    #def do(monster03):
    #    monster03.frameTime += 1
    #    if(monster03.frameTime == monster03.frameTimeMax):
    #        monster03.frame = (monster03.frame +1) % 2
    #        monster03.frameTime = 0
    #    if(monster03.horizon):
    #        monster03.x += monster03.velocity * game_framework.frame_time * 100
    #    else:
    #        monster03.y += monster03.velocity * game_framework.frame_time * 100
    def draw(monster03):
        monster03.image.draw(0, 0, 30, 30, monster03.x, monster03.y)


class Monster_03:
    def __init__(self):
        self.x = random.randint(61, 329)
        self.y = random.randint(54, 214)

        self.image = load_image('monster_03.png')
        self.dir = 0
        self.velocity = 0
        self.horizon = True
        self.frame = 0
        self.frameTime = 0
        self.frameTimeMax = 2
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)

    #def add_event(self, event):
    #   self.event_que.insert(0, event)

    def get_player_location(self, player_x, player_y):
        global player_location
        player_location = [player_x, player_y]
        print("x : %f, y : %f" % (player_location[0], player_location[1]))


    def update(self):
        self.cur_state.do(self)
        #tracking_events1(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            #self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)




