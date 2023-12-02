from pico2d import *

import game_world
import play_mode
import play_mode3
import player1win
import player2win
import title_mode
from moon import Moon
from hp_ui import HPUI
import game_framework
import select_mode
from jupiter import Jupiter
from mars import Mars
from mercury import Mercury
from venus import Venus

player1_Win=False
player2_Win=False
go_round3=False
# Game object class here

def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()




        # elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
        #     game_framework.push_mode(item_mode)


        else:
            player1.handle_event(event)
            player2.handle_event(event)


def init():
    # global grass
    global team
    global player1
    global player2
    global background
    global hpui



    # game_world.add_object(grass, 0)
    hpui=HPUI(2)
    if select_mode.HeroIdle == 2:
        player1 = Moon(1,2)
    elif select_mode.HeroIdle== 0:
        player1 = Jupiter(1,2)
    elif select_mode.HeroIdle == 1:
        player1 = Mars(1,2)
    elif select_mode.HeroIdle == 3:
        player1 = Mercury(1,2)
    elif select_mode.HeroIdle == 4:
        player1 = Venus(1,2)
    #
    if select_mode.HeroIdle2 == 2:
        player2 = Moon(2,2)
    elif select_mode.HeroIdle2 == 0:
        player2 = Jupiter(2,2)
    elif select_mode.HeroIdle2 == 1:
        player2 = Mars(2,2)
    elif select_mode.HeroIdle2 == 3:
        player2 = Mercury(2,2)
    elif select_mode.HeroIdle2 == 4:
         player2 = Venus(2,2)
    # boy.image_IDLE = select_mode.HeroIdle
    background=load_image('resource/stage/stage2.png')

    game_world.add_object(player1, 1)
    game_world.add_object(player2, 1)
    game_world.add_object(hpui, 0)



def update():
    game_world.update()
    game_world.handle_collision()

    if go_round3:#1 대 1 상황
        game_framework.change_mode(play_mode3)
    elif player1_Win:
        play_mode.background.stopBGM()
        game_framework.change_mode(player1win)
    elif player2_Win:
        play_mode.background.stopBGM()

        game_framework.change_mode(player2win)


def draw():
    # global  background
    clear_canvas()
    background.clip_draw(0,0,800,501,500,350,1000,700)
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
    pass

def pause():
    pass
def resume():
    pass




