from pico2d import get_events, load_image, clear_canvas, update_canvas, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import play_mode
import select_mode

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3


def init():
    global titleimage1
    global titleimage2
    global titleimage3
    global titleframe

    titleframe = 0
    titleimage1 = load_image('resource/title/title1.png')
    titleimage2 = load_image('resource/title/title2.png')
    titleimage3 = load_image('resource/title/title3.png')
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
        titleimage1.clip_draw(0, 0,1000,700,500,350,1010,710)
    elif int(titleframe) == 1:
        titleimage2.clip_draw(0, 0,1000,700,500,350,1010,710)
    elif int(titleframe) == 2:
        titleimage3.clip_draw(0, 0,1000,700,500,350,1010,710)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(select_mode)

