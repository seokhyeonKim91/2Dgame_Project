import random
import json
import os

from pico2d import *
import game_framework
import game_world

from player import Player
from map_01 import Map_01
from monster_01 import Monster_01

name = "MainState"

player = None

def enter():
    global player
    player = Player()
    map = Map_01()
    mon_team01 = [Monster_01() for i in  range(3)]
    game_world.add_object(map, 0)
    game_world.add_object(player, 1)
    game_world.add_object(mon_team01, 1)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            player.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






