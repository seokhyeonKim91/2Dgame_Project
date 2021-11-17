import game_framework
from pico2d import *


# Player Run Speed
PIXEL_PER_METER = (1.0 / 0.3)
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP = range(8)
key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
(SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
(SDL_KEYDOWN, SDLK_UP): UP_DOWN,
(SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
(SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
(SDL_KEYUP, SDLK_LEFT): LEFT_UP,
(SDL_KEYUP, SDLK_UP): UP_UP,
(SDL_KEYUP, SDLK_DOWN): DOWN_UP,
}

dir_hero = 0


class IdleState:
    def enter(player, event):
        global dir_hero
        if event == RIGHT_DOWN:
            player.velocity = 0
            player.velocity += RUN_SPEED_PPS
            player.dir = 0
            player.dir += 90
            player.horizon = True
        elif event == LEFT_DOWN:
            player.velocity = 0
            player.velocity -= RUN_SPEED_PPS
            player.dir = 0
            player.dir += 30
            player.horizon = True
        elif event == UP_DOWN:
            player.velocity = 0
            player.velocity += RUN_SPEED_PPS
            player.dir = 0
            player.dir += 60
            player.horizon = False
        elif event == DOWN_DOWN:
            player.velocity = 0
            player.velocity -= RUN_SPEED_PPS
            player.dir = 0
            player.horizon = False
        elif event == RIGHT_UP:
            player.velocity = 0
        elif event == LEFT_UP:
            player.velocity = 0
        elif event == UP_UP:
            player.velocity = 0
        elif event == DOWN_UP:
            player.velocity = 0


    def exit(player, event):
        pass

    def do(player):
        player.frameTime += 1
        if(player.frameTime == player.frameTimeMax):
            player.frame = (player.frame +1) % 2
            player.frameTime = 0
        if(player.horizon):
            player.x += player.velocity * game_framework.frame_time * 100
        else:
            player.y += player.velocity * game_framework.frame_time * 100



    def draw(player):
        #if player.dir == 1:
        player.image.clip_draw(player.dir, player.frame * 30, 30, 30, player.x, player.y)





next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState}
#    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState},
#    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState}
}


class Player:

    def __init__(self):
        self.x = 192
        self.y = 60

        self.image = load_image('link_run1.png')
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
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            #self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        # collison check
        if self.x >= 330:
            self.x = 329
        elif self.x <= 60:
            self.x = 61
        elif self.y >= 215:
            self.y = 214
        elif self.y <= 54:
            self.y = 55



    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir))



    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

