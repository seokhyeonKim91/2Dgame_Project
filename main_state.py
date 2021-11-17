import random
import json
import os

from pico2d import *
import game_framework
import game_world

from player import Player
from map_01 import Map_01
from monster_01 import Monster_01
from monster_02 import Monster_02
from monster_03 import Monster_03

name = "MainState"

player = None
monster_01 = None
monster_02 = None
monster_03 = None

player_location = []

def enter():
    global player
    global monster_01
    global monster_02
    global monster_03
    player = Player()
    map = Map_01()
    monster_01 = Monster_01()
    monster_02 = Monster_02()
    monster_03 = Monster_03()
    game_world.add_object(map, 0)
    game_world.add_object(player, 1)
    game_world.add_object(monster_01, 1)
    game_world.add_object(monster_02, 1)
    #game_world.add_object(monster_03, 1)



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
    global player
    global monster_01
    global monster_02
    global monster_03
    global player_location

    for game_object in game_world.all_objects():
        game_object.update()
        if game_object == player:
            player_location = [player.x, player.y]
            print("is player")
        if game_object == monster_01:
            monster_01.get_player_location(player_location[0], player_location[1])
            print("is monster_01")
        if game_object == monster_02:
            monster_02.get_player_location(player_location[0], player_location[1])
            print("is monster_01")
        #if game_object == monster_03:
        #    monster_03.get_player_location(player_location[0], player_location[1])
        #   print("is monster_01")


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






