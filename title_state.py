import game_framework
import main_state
from pico2d import *
resolution_width, resolution_height = 1280, 720

name = "TitleState"
image = None
bgm = None
logo_time = 0.0



def enter():
    global image
    global bgm
    image = load_image('gametitle.png')
    bgm = load_music('04 The Moonlighter.mp3')
    bgm.set_volume(30)
    bgm.repeat_play()


def exit():
    global image
    bgm.stop()
    del (image)


def update():
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
    delay(0.1)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(resolution_width // 2, resolution_height // 2)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                game_framework.change_state(main_state)
    pass


