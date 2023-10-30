# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, clamp
from sdl2 import SDLK_LSHIFT, SDLK_LCTRL, SDLK_a, SDLK_s

import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5
import select_mode

# state event check
# ( state event type, event value )
def check_push(e):
    return ispush == True

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def shift_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LSHIFT


def shift_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LSHIFT
def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a
def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a and StateMachine.ispunch
def time_out(e):
    return e[0] == 'TIME_OUT'
def s_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s and StateMachine.iskick
def s_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s


# time_out = lambda e : e[0] == 'TIME_OUT'


class Idle:
    @staticmethod
    def enter(boy, e):
        if boy.face_dir == -1:
            boy.action = 2
        elif boy.face_dir == 1:
            boy.action = 3
        boy.frame = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass


    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
    @staticmethod
    def draw(boy):
        if boy.face_dir == 1:
            boy.image_IDLE.clip_draw(0, 0, 46, 109, boy.x, boy.y, 130, 280)

        elif boy.face_dir == -1:
            # boy.image_KICK.clip_draw(0, 0, 79, 115, boy.x, boy.y, 196, 280)
            boy.image_IDLE.clip_composite_draw(0, 0, 46, 109, 0, 'h', boy.x, boy.y,  130, 280)


class Walk:

    @staticmethod
    def enter(boy, e):
        if  right_down(e) or left_up(e) :  # 오른쪽으로 RUN
            boy.face_dir,boy.dir =1,1
        elif left_down(e) or right_up(e) :  # 왼쪽으로 RUN
            boy.face_dir,boy.dir =-1,-1

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):

        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(60, boy.x, 1000 - 60)

        pass

    @staticmethod
    def draw(boy):
        pix_posx = [0, 50, 96, 145, 194, 239, 287, 345, 397, 445, 490]
        if boy.face_dir == 1:
            boy.image_WALK.clip_draw(pix_posx[int(boy.frame)], 0, 53, 108, boy.x, boy.y, 150, 280)

        elif boy.face_dir == -1:
            boy.image_WALK.clip_composite_draw(pix_posx[int(boy.frame)], 0, 53, 108, 0, 'h', boy.x, boy.y, 150, 280)




class Run:
    @staticmethod
    def enter(boy, e):
        if (right_down(e) and StateMachine.isdash) or (left_up(e) and StateMachine.isdash):  # 오른쪽으로 RUN
            boy.dir, boy.action, boy.face_dir = 1, 1, 1
        elif (left_down(e) and StateMachine.isdash) or (right_up(e) and StateMachine.isdash):  # 왼쪽으로 RUN
            boy.dir, boy.action, boy.face_dir = -1, 0, -1

    @staticmethod
    def exit(boy, e):

        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        boy.x += boy.dir * (RUN_SPEED_PPS+300) * game_framework.frame_time
        boy.x = clamp(60, boy.x, 1000 - 60)


        pass
    @staticmethod
    def draw(boy):

        pix_posx = [0, 83, 166, 240, 325, 418]

        if boy.face_dir == 1:
                 boy.image_RUN.clip_draw(pix_posx[int(boy.frame)], 0, 79, 99, boy.x, boy.y, 220, 280)

        elif boy.face_dir == -1:
                boy.image_RUN.clip_composite_draw(pix_posx[int(boy.frame)], 0, 79, 99, 0, 'h',boy.x, boy.y,220, 280)


class Punch:
    @staticmethod
    def enter(boy, e):
        boy.frame=0
        if (right_down(e) and StateMachine.isdash and StateMachine.ispunch) or (right_up(e) and StateMachine.isdash and StateMachine.ispunch)or (right_down(e) and StateMachine.ispunch)  :  # 오른쪽으로 RUN
            boy.dir, boy.action, boy.face_dir = 1, 1, 1
        elif (left_down(e) and StateMachine.isdash and StateMachine.ispunch) or (left_up(e) and StateMachine.isdash and StateMachine.ispunch) or (left_down(e) and StateMachine.ispunch):  # 왼쪽으로 RUN
            boy.dir, boy.action, boy.face_dir = -1, 0, -1

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        # boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time) % 2

        boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time)
        if int(boy.frame) > 1:
            boy.frame = 0
            StateMachine.ispunch = False
            boy.state_machine.handle_event(('TIME_OUT', 0))



        pass
    @staticmethod
    def draw(boy):
        global ispush
        pix_posX = [0, 80]

        if boy.face_dir == 1:
            boy.image_PUNCH.clip_draw(pix_posX[int(boy.frame)], 0, 72, 110, boy.x + 25, boy.y, 180, 280)

        elif boy.face_dir == -1:
                 boy.image_PUNCH.clip_composite_draw(pix_posX[int(boy.frame)], 0, 72, 110, 0, 'h', boy.x-20 , boy.y,  180, 280)


class Kick:
    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        if (right_down(e) and StateMachine.isdash and StateMachine.iskick) or (right_up(e) and StateMachine.isdash and StateMachine.iskick)or (right_down(e) and StateMachine.iskick)  :  # 오른쪽으로 RUN
            boy.face_dir =  1
        elif (left_down(e) and StateMachine.isdash and StateMachine.iskick) or (left_up(e) and StateMachine.isdash and StateMachine.iskick) or (left_down(e) and StateMachine.iskick):  # 왼쪽으로 RUN
            boy.face_dir = -1
        boy.frame = 0   #Add

    @staticmethod
    def exit(boy, e):
        if space_down(e):
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time)# % 6   Add
        if int(boy.frame) > 2:
            boy.frame = 0
            StateMachine.iskick = False
            boy.state_machine.handle_event(('TIME_OUT', 0))

            boy.x = clamp(60, boy.x, 1000 - 60)

        pass
    @staticmethod
    def draw(boy):
        pix_posx = [0, 86, 190]
        if boy.face_dir == 1:
            boy.image_KICK.clip_draw(pix_posx[int(boy.frame)],  0, 103, 109, boy.x, boy.y, 270, 280)

        elif boy.face_dir == -1:
            boy.image_KICK.clip_composite_draw(pix_posx[int(boy.frame)], 0, 103, 109, 0, 'h', boy.x, boy.y, 270, 280)
class RunPunch:
    @staticmethod
    def enter(boy, e):
        boy.frame=0
        if (StateMachine.isspace and right_down(e)) or (StateMachine.isspace and right_up(e)) :  # 오른쪽으로 RUN
            boy.face_dir = 1
        elif (StateMachine.isspace and left_down(e)) or(StateMachine.isspace and left_up(e)):  # 왼쪽으로 RUN
            boy.face_dir = -1

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time)
        if int(boy.frame) > 2:
            boy.frame = 0
            boy.state_machine.handle_event(('TIME_OUT', 0))



        pass
    @staticmethod
    def draw(boy):
        pix_posX = [8, 107, 207]

        if boy.face_dir == 1:
            boy.image_RUNPUNCH.clip_draw(pix_posX[int(boy.frame)], 0, 93, 107, boy.x + 10, boy.y + 10, 260, 290)

        elif boy.face_dir == -1:
            boy.image_RUNPUNCH.clip_composite_draw(pix_posX[int(boy.frame)], 0, 93, 107, 0, 'h', boy.x-10,  boy.y+10, 260, 290)

class StateMachine:
    isdash = False
    ispunch = True
    iskick = True
    isspace=False
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Walk, left_down: Walk, left_up: Idle, right_up: Idle, space_down: Idle,a_down:Punch, s_down:Kick},
            Walk: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, shift_down:Run, a_down:Punch, s_down:Kick,},
            Run:{shift_up:Walk, right_up: Idle, left_up:Idle, right_down: Idle, left_down: Idle, a_down:Punch, s_down:Kick,space_down:RunPunch},
            Punch:{right_down:Walk , left_down:Walk, s_down:Kick, time_out:Idle},
            Kick:{ right_down:Walk , left_down:Walk,a_down:Punch, time_out:Idle},
            RunPunch:{time_out:Idle}
        }

    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)

    def handle_event(self, e):
        global ispush
        global istoggle
        if shift_down(e):
            StateMachine.isdash=True
        elif shift_up(e):
            StateMachine.isdash = False

        # if a_down(e):
        #     StateMachine.ispunch = True
        if a_up(e):
            StateMachine.ispunch = True

        if s_up(e):
            StateMachine.iskick = True


        if space_down(e):
            StateMachine.isspace=True
        elif space_up(e):
            StateMachine.isspace = False

        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.boy)


class Mercury:
    def __init__(self):
        self.x, self.y = 500, 200
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.image_WALK = load_image('resource/mercury/mercuryWalk.png')
        self.image_IDLE = load_image('resource/mercury/mercuryIdle.png')
        self.image_RUN = load_image('resource/mercury/mercuryRun.png')
        self.image_PUNCH = load_image('resource/mercury/mercuryPunch.png')
        self.image_KICK = load_image('resource/mercury/mercuryKick.png')
        self.image_HPUI=load_image('resource/ui/hpUI2.png')
        self.image_jupiterUI=load_image('resource/ui/mercuryUI.png')
        self.image_RUNPUNCH=load_image('resource/mercury/mercuryRunPunch.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.item = None
        self.hp=100


        pass

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        # for i in range(self.hp//10) :

        self.state_machine.draw()
        self.image_jupiterUI.clip_draw(0, 0, 246, 75,   110,640,    160,70)

        for i in range(self.hp//10):
            self.image_HPUI.clip_draw(0, 0, 549, 41, 59 + (38 * i), 600, 38, 30)