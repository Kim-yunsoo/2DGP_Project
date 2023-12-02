from pico2d import *

import game_world
import game_framework
import select_mode

player1_Win=False
player2_Win=False
go_round3=False
# Game object class here
def handle_events():
    global arrowPosX

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(select_mode)
        else:
            pass


def init():
    # global grass
    global background
    background=load_image('resource/stage/character_explan.png')

def update():
    game_world.update()
    game_world.handle_collision()
def draw():
    # global  background
    clear_canvas()
    background.clip_draw(0,0,837,575,500,350,1000,700)
    game_world.render()
    update_canvas()
def finish():
    game_world.clear()
    pass

def pause():
    pass
def resume():
    pass




