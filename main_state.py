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
from heartgauge import Health

name = "MainState"

player = None
monster_01 = None
monster_02 = None
monster_03 = None
health = None

player_location = []

def enter():
    global player
    global monster_01
    global monster_01_01
    global monster_02
    global health
    player = Player()
    map = Map_01()
    monster_01 = Monster_01()
    monster_01_01 = Monster_01()
    monster_02 = Monster_02()
    health = Health()

    game_world.add_object(map, 0)
    game_world.add_object(health, 0)
    game_world.add_object(player, 1)
    game_world.add_object(monster_01, 1)
    game_world.add_object(monster_01_01, 1)
    game_world.add_object(monster_02, 1)



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
    global monster_01_01
    global monster_02
    global health
    global player_location

    for game_object in game_world.all_objects():
        game_object.update()
        if game_object == player:
            player_location = [player.x, player.y]
            health.update_heart(player.get_health())
            print("is player")
            print("x : %f, y : %f" % (player_location[0], player_location[1]))
        elif game_object == monster_01 or game_object == monster_02 or game_object == monster_01_01:
            game_object.get_player_location(player_location[0], player_location[1])
            #print("is monster_01")
            if collide(player, game_object) != [99999, 99999]:
                # player.stop()
                if(player.get_state() == 1):
                    # 플레이어의 상태가 AttackState 일 때 충돌한 적 넉백
                    if game_object.knockback(collide(player, game_object)[0] * -0.5, collide(player, game_object)[1] * -0.5) :
                        game_world.remove_object(game_object)
                else:
                    player.knockback(collide(player, game_object)[0] * 0.5, collide(player, game_object)[1] * 0.5)







def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    return_x = 99999
    return_y = 99999

    if left_a > right_b: return [return_x, return_y]
    if right_a < left_b: return [return_x, return_y]
    if top_a < bottom_b: return [return_x, return_y]
    if bottom_a > top_b: return [return_x, return_y]

    return_x = left_a - left_b
    return_y = top_a - top_b
    return [return_x, return_y]







