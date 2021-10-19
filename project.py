from pico2d import *
import random
resolution_width, resolution_height = 384, 264


def handle_events():
    global running
    global dir_x
    global dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

    pass

# initialization code
open_canvas(resolution_width, resolution_height)
map_ground = load_image('dungeon_1.png')
hero = load_image('link_run.png')


running = True
rx, ry = resolution_width // 2, resolution_height // 2
x = 192
y = 60
frame = 0
dir_x = 0
dir_y = 0
hide_cursor()

# game main loop code

while running:
    clear_canvas()
    map_ground.draw(resolution_width // 2, resolution_height // 2)
    hero.clip_draw(0, frame * 32, 16, 32, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 2
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)
close_canvas()