import game_framework
from pico2d import *
resolution_width, resolution_height = 1280, 720

name = "VictoryState"
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('victory.png')


def exit():
    global image
    delay(1)
    del (image)


def update():
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
    game_framework.quit()
    delay(0.1)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(resolution_width // 2, resolution_height // 2)
    update_canvas()


def handle_events():
    events = get_events()
    pass


