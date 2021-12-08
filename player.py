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


RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, z_UP, z_DOWN = range(10)
key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
(SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
(SDL_KEYDOWN, SDLK_UP): UP_DOWN,
(SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
(SDL_KEYDOWN, SDLK_z): z_DOWN,
(SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
(SDL_KEYUP, SDLK_LEFT): LEFT_UP,
(SDL_KEYUP, SDLK_UP): UP_UP,
(SDL_KEYUP, SDLK_DOWN): DOWN_UP,
(SDL_KEYUP, SDLK_z): z_UP,
}

dir_hero = 0


class IdleState:
    def enter(player, event):
        global dir_hero
        if event == RIGHT_DOWN:
            player.velocity = 0
            player.velocity += RUN_SPEED_PPS
            player.dir = 0
            player.horizon = True
        elif event == LEFT_DOWN:
            player.velocity = 0
            player.velocity -= RUN_SPEED_PPS
            player.dir = 0
            player.dir += 128
            player.horizon = True
        elif event == UP_DOWN:
            player.y_velocity = 0
            player.y_velocity += RUN_SPEED_PPS
            player.dir = 0
            player.dir += 64
            player.horizon = False
        elif event == DOWN_DOWN:
            player.y_velocity = 0
            player.y_velocity -= RUN_SPEED_PPS
            player.dir = 0
            player.dir += 192
            player.horizon = False
        elif event == RIGHT_UP:
            player.velocity = 0
        elif event == LEFT_UP:
            player.velocity = 0
        elif event == UP_UP:
            player.y_velocity = 0
        elif event == DOWN_UP:
            player.y_velocity = 0


    def exit(player, event):
        pass

    def do(player):
        player.frameTime += 1
        if(player.frameTime == player.frameTimeMax):
            player.frame = (player.frame +1) % 4
            player.frameTime = 0
        #if(player.horizon):
        player.x += player.velocity * game_framework.frame_time * 100
        #else:
        player.y += player.y_velocity * game_framework.frame_time * 100


    def draw(player):
        #if player.dir == 1:
        player.image.clip_draw(player.frame * 64, player.dir, 64, 64, player.x, player.y)



class AttackState:
    def enter(player, event):
        global dir_hero
        if event == z_DOWN:
            player.image = load_image('player_attack.png')
            player.image.clip_draw(player.frame * 64, player.dir, 64, 64, player.x, player.y)
        elif event == z_UP:
            player.image = load_image('player_idle.png')

    def draw(player):
        player.image.clip_draw(player.frame * 64, player.dir, 64, 64, player.x, player.y)

    def exit(player, event):
        pass

    def do(player):
        player.frameTime += 1
        if(player.frameTime == player.frameTimeMax):
            player.frame = (player.frame +1) % 4
            player.frameTime = 0
        #if(player.horizon):
        player.x += player.velocity * game_framework.frame_time * 100
        #else:
        player.y += player.y_velocity * game_framework.frame_time * 100




    #def do(player):
    #    player.frameTime += 1
    #    if(player.frameTime == player.frameTimeMax):
    #        player.frame = (player.frame +1) % 4
    #        player.frameTime = 0
    #    if(player.horizon):
    #    player.x += player.velocity * game_framework.frame_time * 100
    #    else:
    #    player.y += player.y_velocity * game_framework.frame_time * 100



next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP: IdleState, DOWN_UP: IdleState,
                RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState, z_UP: AttackState, z_DOWN: AttackState},
    AttackState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP: IdleState, DOWN_UP: IdleState,
                RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState, z_UP: AttackState, z_DOWN: AttackState}
}


class Player:

    def __init__(self):
        self.x = 638
        self.y = 131

        self.image = load_image('player_idle.png')
        self.dir = 0
        self.velocity = 0
        self.y_velocity = 0
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
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        # collison check
        if self.x >= 1133:
            self.x = 1132
        elif self.x <= 143:
            self.x = 144
        elif self.y >= 660:
            self.y = 659
        elif self.y <= 105:
            self.y = 106



    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir))
        draw_rectangle(*self.get_bb())



    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 30, self.y - 35, self.x + 30, self.y + 35
        return 0, 0, 0, 0

    def stop(self):
        self.velocity = 0
        self.y_velocity = 0



