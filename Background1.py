from pico2d import *

import game_framework

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3

player1_score=0
player2_score=0
class Selet:
    def __init__(self):

        global image1
        global image3
        global image2
        global titleframe

        # self.image = load_image('resource/stage/stage1.png')
        # self.cw = get_canvas_width()
        # self.ch = get_canvas_height()
        # self.w = self.image.w
        # self.h = self.image.h
        # # fill here
        #
        self.bgm=load_music('resource/sound/selet.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

        titleframe = 0
        image1 = load_image('resource/select/selet1.png')
        image2 = load_image('resource/select/selet2.png')
        image3 = load_image('resource/select/selet3.png')


    def draw(self):
        if int(titleframe) == 0:
            image1.clip_draw(0, 0, 1354, 1085, 500, 350, 1020, 710)
        elif int(titleframe) == 1:
            image2.clip_draw(0, 0, 1354, 1085, 500, 350, 1020, 710)
        elif int(titleframe) == 2:
            image3.clip_draw(0, 0, 1354, 1085, 500, 350, 1020, 710)

        pass

    def update(self):
        global titleframe

        titleframe = (titleframe + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        pass

    def handle_event(self, event):
        pass
class Title:
    def __init__(self):
        global titleimage1
        global titleimage2
        global titleimage3
        global titleframe
        # self.image = load_image('resource/stage/stage1.png')
        # self.cw = get_canvas_width()
        # self.ch = get_canvas_height()
        # self.w = self.image.w
        # self.h = self.image.h
        # # fill here
        #
        self.bgm=load_music('resource/sound/title.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

        titleframe = 0
        titleimage1 = load_image('resource/title/title1.png')
        titleimage2 = load_image('resource/title/title2.png')
        titleimage3 = load_image('resource/title/title3.png')


    def draw(self):
        if int(titleframe) == 0:
            titleimage1.clip_draw(0, 0, 1000, 700, 500, 350, 1010, 710)
        elif int(titleframe) == 1:
            titleimage2.clip_draw(0, 0, 1000, 700, 500, 350, 1010, 710)
        elif int(titleframe) == 2:
            titleimage3.clip_draw(0, 0, 1000, 700, 500, 350, 1010, 710)

        pass

    def update(self):
        global titleframe

        titleframe = (titleframe + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        pass

    def handle_event(self, event):
        pass
class Background1:

    def __init__(self):
        self.image = load_image('resource/stage/stage1.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        # fill here

        self.bgm=load_music('resource/sound/play.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()


    def draw(self):
        self.image.clip_draw(0, 0, 800, 501, 500, 350, 1000, 700)
        pass

    def update(self):
        pass
    def stopBGM(self):
        self.bgm.stop()


    def handle_event(self, event):
        pass

