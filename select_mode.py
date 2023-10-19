from pico2d import get_events, load_image, clear_canvas, update_canvas, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDLK_RIGHT, SDLK_LEFT

import game_framework
import play_mode

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3
posX = [125, 310, 482, 675, 850]


def init():
    global image1
    global image3
    global image2
    global arrowimage
    global titleframe
    global arrowPosX
    global arrowPosY
    global pickmoon
    global pickmars
    global pickvenus
    global pickmercury
    global pickjupiter

    titleframe = 0
    image1 = load_image('resource/select/selet1.png')
    image2 = load_image('resource/select/selet2.png')
    image3 = load_image('resource/select/selet3.png')
    arrowimage=load_image('resource/select/arrow.png')
    pickmoon=load_image('resource/select/seletmoon.png')
    pickmars=load_image('resource/select/seletmars.png')
    pickvenus=load_image('resource/select/seletvenus.png')
    pickmercury=load_image('resource/select/seletmercury.png')
    pickjupiter=load_image('resource/select/seletjupiter.png')

    arrowPosX=posX[2]
    arrowPosY=330
    pass


def finish():
    pass
def pause():
    pass
def resume():
    pass

def update():
    global titleframe

    titleframe = (titleframe + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
    pass


def draw():
    clear_canvas()
    if int(titleframe) == 0:
        image1.clip_draw(0, 0,1354,1085,500,350,1020,710)
    elif int(titleframe) == 1:
        image2.clip_draw(0, 0,1354,1085,500,350,1020,710)
    elif int(titleframe) == 2:
        image3.clip_draw(0, 0,1354,1085,500,350,1020,710)

    arrowimage.draw(arrowPosX,arrowPosY)
    if arrowPosX == posX[0]:
        pickjupiter.draw(740,542)
    elif arrowPosX == posX[1]:
        pickmars.draw(740,545)
    elif arrowPosX == posX[2]:
        pickmoon.draw(740,543)
    elif arrowPosX == posX[3]:
        pickmercury.draw(740,544)
    elif arrowPosX == posX[4]:
        pickvenus.draw(740,543)





    update_canvas()
    pass

def handle_events():
    global arrowPosX
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if arrowPosX == posX[2]:
                arrowPosX = posX[3]
            elif arrowPosX == posX[3]:
                arrowPosX = posX[4]
            elif arrowPosX == posX[4]:
                arrowPosX = posX[4]
            elif arrowPosX == posX[0]:
                arrowPosX = posX[1]
            elif arrowPosX == posX[1]:
                arrowPosX = posX[2]
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            if arrowPosX == posX[0]:
                arrowPosX = posX[0]
            elif arrowPosX == posX[1]:
                arrowPosX = posX[0]
            elif arrowPosX == posX[2]:
                arrowPosX = posX[1]
            elif arrowPosX == posX[3]:
                arrowPosX = posX[2]
            elif arrowPosX == posX[4]:
                arrowPosX = posX[3]


        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            global HeroIdle
            if arrowPosX ==posX[0]:
                HeroIdle = 0
            elif arrowPosX == posX[1]:
                HeroIdle = 1
            elif arrowPosX == posX[2]:
                HeroIdle = 2
            elif arrowPosX == posX[3]:
                HeroIdle = 3
            elif arrowPosX == posX[4]:
                HeroIdle = 4
            game_framework.change_mode(play_mode)

