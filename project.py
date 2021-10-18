from pico2d import *
import random


class Hero:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0

    def update(self): # 소년의 행위 구현.
        self.x += 5 # 속성 값을 바꿈으로 써, 행위(오른쪽으로 이동)를 구현
        self.frame = (self.frame + 1 ) % 8
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Monster:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0

    def update(self): # 소년의 행위 구현.
        self.x += 5 # 속성 값을 바꿈으로 써, 행위(오른쪽으로 이동)를 구현
        self.frame = (self.frame + 1 ) % 8
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Map:
    def __init__(self): # 생성자
        self.image = load_image('map_001.png')

    def draw(self):
        self.image.draw(400, 30)
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()

map =Map() #Grass 라는 클래스로부터, grass 객체를 생성한다.
hero = Hero()
team = [ Monster() for i in range(5)]


running = True

# game main loop code

while running:

    handle_events() # 키 입력을 받아들이는 처리

    #Game logic
    for monster in team:
        monster.update() # 소년의 상호작용

    #Game drawing
    clear_canvas()
    map.draw()

    for monster in team:
        monster.draw()
    update_canvas()

    delay(0.05)
# finalization code