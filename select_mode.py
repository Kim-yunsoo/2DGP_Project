from pico2d import get_events, load_image, clear_canvas, update_canvas, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDLK_RIGHT, SDLK_LEFT, SDLK_d, SDLK_a

import explane_mode
import game_framework
import game_world
import play_mode
from Background1 import Selet

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3
posX = [125, 310, 482, 675, 850]


def init():
    global arrowimage
    global arrowimage2
    global arrowPosX
    global arrowPosY
    global arrowPosX2
    global arrowPosY2
    global pickmoon
    global pickmars
    global pickvenus
    global pickmercury
    global pickjupiter

    global player1
    global player2
    background=Selet()

    game_world.add_object(background,0)

    arrowimage=load_image('resource/select/arrow1p.png')
    arrowimage2=load_image('resource/select/arrow2p.png')
    pickmoon=load_image('resource/select/seletmoon.png')
    pickmars=load_image('resource/select/seletmars.png')
    pickvenus=load_image('resource/select/seletvenus.png')
    pickmercury=load_image('resource/select/seletmercury.png')
    pickjupiter=load_image('resource/select/seletjupiter.png')
    player1=load_image('resource/select/player1.png')
    player2=load_image('resource/select/player2.png')

    arrowPosX=posX[2]
    arrowPosY=340

    arrowPosX2=posX[3]
    arrowPosY2=340
    pass


def finish():
    game_world.clear()
    pass
def pause():
    pass
def resume():
    pass

def update():
    game_world.update()
    game_world.handle_collision()
    pass


def draw():
    clear_canvas()
    game_world.render()


    arrowimage.clip_draw(0,0,106,108,arrowPosX,arrowPosY,60,60)
    arrowimage2.clip_draw(0,0,106,108,arrowPosX2,arrowPosY2,60,60)

    player1.clip_draw(0,0,227,106,230,679   ,207,76)
    player2.clip_draw(0,0,227,106,780,679   ,207,76)

    # player1.draw()



    if arrowPosX2 == posX[0]:#740 542
        pickjupiter.clip_draw(0,0,353,290,  780,510, 315,260)
    elif arrowPosX2 == posX[1]:
        pickmars.clip_draw(0,0,412,298,     780,510, 370,260)
    elif arrowPosX2 == posX[2]:
        pickmoon.clip_draw(0,0,451,295,     770,510, 390,260)
    elif arrowPosX2 == posX[3]:
        pickmercury.clip_draw(0,0,430,295,  780,510, 345,260)
    elif arrowPosX2 == posX[4]:
        pickvenus.clip_draw(0,0,388,294,    780,510, 323,260)

    if arrowPosX == posX[0]:#740 542
        pickjupiter.clip_composite_draw(0,0,353,290,0,'h',200,510, 315,260)
    elif arrowPosX == posX[1]:
        pickmars.clip_composite_draw(0,0,412,298,0,'h',230,510, 370,260)
    elif arrowPosX == posX[2]:
        pickmoon.clip_composite_draw(0,0,451,295,0,'h', 230,510, 390,260)
    elif arrowPosX == posX[3]:
        pickmercury.clip_composite_draw(0,0,430,295,0,'h',200,510, 345,260)
    elif arrowPosX == posX[4]:
        pickvenus.clip_composite_draw(0,0,388,294,0,'h',200,510, 323,260)
    update_canvas()
    pass

def handle_events():
    global arrowPosX
    global arrowPosX2
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(explane_mode)
        elif event.type==SDL_KEYDOWN and event.key == SDLK_d:
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
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
        elif event.type==SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if arrowPosX2 == posX[2]:
                arrowPosX2 = posX[3]
            elif arrowPosX2 == posX[3]:
                arrowPosX2 = posX[4]
            elif arrowPosX2 == posX[4]:
                arrowPosX2 = posX[4]
            elif arrowPosX2 == posX[0]:
                arrowPosX2 = posX[1]
            elif arrowPosX2 == posX[1]:
                arrowPosX2 = posX[2]
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            if arrowPosX2 == posX[0]:
                arrowPosX2 = posX[0]
            elif arrowPosX2 == posX[1]:
                arrowPosX2 = posX[0]
            elif arrowPosX2 == posX[2]:
                arrowPosX2 = posX[1]
            elif arrowPosX2 == posX[3]:
                arrowPosX2 = posX[2]
            elif arrowPosX2 == posX[4]:
                arrowPosX2 = posX[3]


        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            global HeroIdle
            global HeroIdle2
            if arrowPosX == posX[0]:
                HeroIdle = 0
            elif arrowPosX == posX[1]:
                HeroIdle = 1
            elif arrowPosX == posX[2]:
                HeroIdle = 2
            elif arrowPosX == posX[3]:
                HeroIdle = 3
            elif arrowPosX == posX[4]:
                HeroIdle = 4


            if arrowPosX2 == posX[0]:
                HeroIdle2 = 0
            elif arrowPosX2 == posX[1]:
                HeroIdle2 = 1
            elif arrowPosX2 == posX[2]:
                HeroIdle2 = 2
            elif arrowPosX2 == posX[3]:
                HeroIdle2 = 3
            elif arrowPosX2 == posX[4]:
                HeroIdle2 = 4
            game_framework.change_mode(play_mode)

