import game_framework
from pico2d import *
resolution_width, resolution_height = 1280, 720

name = "GameoverState"
image = None
bgm = None
logo_time = 0.0

def enter():
    global image
    global bgm
    bgm = load_music('22 The Void.mp3')
    bgm.set_volume(30)
    bgm.repeat_play()
    image = load_image('gameover.png')


def exit():
    global image
    delay(3)
    bgm.stop()
    del (image)


def update():
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
    game_framework.quit()
    delay(0.5)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(resolution_width // 2, resolution_height // 2)
    update_canvas()


def handle_events():
    events = get_events()
    pass


