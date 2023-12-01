from pico2d import *

import game_world
import play_mode
import play_mode2
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
PosX=[140,645]
def handle_events():
    global arrowPosX

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if arrowPosX ==PosX[0]:
                arrowPosX=PosX[1]

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            if arrowPosX ==PosX[1]:
                arrowPosX=PosX[0]

        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if arrowPosX ==PosX[0]: #재시작
                play_mode.player1_score=0
                play_mode.player2_score=0
                play_mode.next=False
                play_mode2.go_round3=False
                play_mode2.player1_Win=False
                play_mode2.player2_Win=False
                game_framework.change_mode(title_mode)
            if arrowPosX ==PosX[1]: # 나가기
                game_framework.quit()
        else:
            pass


def init():
    # global grass
    global background
    global arrow
    global arrowPosX
    global arrowPosY

    arrowPosX=PosX[0]
    arrowPosY=250

    arrow= load_image('resource/stage/arrowend.png')
    background=load_image('resource/stage/player1winend.png')


def update():
    game_world.update()
    game_world.handle_collision()
def draw():
    # global  background
    clear_canvas()
    background.clip_draw(0,0,1124,953,500,350,1000,700)
    arrow.clip_draw(0,0,48,50,arrowPosX,arrowPosY)
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
    pass

def pause():
    pass
def resume():
    pass




