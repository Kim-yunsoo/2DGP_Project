from pico2d import *

import game_world
import play_mode2
import title_mode
from Background1 import  Background1
from moon import Moon
from hp_ui import HPUI
import game_framework
import select_mode
from jupiter import Jupiter
from mars import Mars
from mercury import Mercury
from venus import Venus
next=False

# Game object class here
player1_score=0
player2_score=0

player1combo=0
player2combo=0

def init():
    # global grass
    global team
    global player1
    global player2
    global background
    global hpui

    # game_world.add_object(grass, 0)
    hpui=HPUI(1)
    if select_mode.HeroIdle == 2:
        player1 = Moon(1,1)
    elif select_mode.HeroIdle== 0:
        player1 = Jupiter(1,1)
    elif select_mode.HeroIdle == 1:
        player1 = Mars(1,1)
    elif select_mode.HeroIdle == 3:
        player1 = Mercury(1,1)
    elif select_mode.HeroIdle == 4:
        player1 = Venus(1,1)

    #
    if select_mode.HeroIdle2 == 2:
        player2 = Moon(2,1)
    elif select_mode.HeroIdle2 == 0:
        player2 = Jupiter(2,1)
    elif select_mode.HeroIdle2 == 1:
        player2 = Mars(2,1)
    elif select_mode.HeroIdle2 == 3:
        player2 = Mercury(2,1)
    elif select_mode.HeroIdle2 == 4:
        player2 = Venus(2,1)
    # boy.image_IDLE = select_mode.HeroIdle

    # background=load_image('resource/stage/stage1.png')
    background=Background1()
    # bgm = load_music('resource/sound/stage1.mp3')
    # bgm.set_volume(32)
    # bgm.repeat_play()


    game_world.add_object(player1, 1)
    game_world.add_object(player2, 1)
    game_world.add_object(background,0)
    game_world.add_object(hpui, 0)


def update():
    if next == True:
        game_framework.change_mode(play_mode2)

    game_world.update()
    game_world.handle_collision()

def draw():
    clear_canvas()
    # background.clip_draw(0,0,800,501,500,350,1000,700)
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
    pass

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
            player1.x = 1000
            player1.y = 1000
            player2.x = 1000
            player2.y = 1000
            game_framework.change_mode(title_mode)


        else:
            player1.handle_event(event)
            player2.handle_event(event)



