from pico2d import *

import game_world
import item_mode
import title_mode
from grass import Grass
from moon import Moon
from hp_ui import HPUI
import game_framework
import select_mode
from jupiter import Jupiter
from mars import Mars
from mercury import Mercury
from venus import Venus


# Game object class here

def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_mode(item_mode)
        else:
            boy.handle_event(event)


def init():
    # global grass
    global team
    global boy
    global background
    global hpui

    # game_world.add_object(grass, 0)
    hpui=HPUI()
    if select_mode.HeroIdle == 2:
        boy = Moon()
    elif select_mode.HeroIdle == 0:
        boy = Jupiter()
    elif select_mode.HeroIdle == 1:
        boy = Mars()
    elif select_mode.HeroIdle == 3:
        boy = Mercury()
    elif select_mode.HeroIdle == 4:
        boy = Venus()

    # boy.image_IDLE = select_mode.HeroIdle
    background=load_image('resource/stage/stage1.png')

    game_world.add_object(boy, 1)
    game_world.add_object(hpui, 0)



def update():
    game_world.update()


def draw():
    global  background
    clear_canvas()
    background.clip_draw(0,0,800,501,500,350,1000,700)
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
    pass

def pause():
    # boy.wait_time=10000000000000000000000000.0
    pass
def resume():
    # boy.wait_time= get_time()
    pass




