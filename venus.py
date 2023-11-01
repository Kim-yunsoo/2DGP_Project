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


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE


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
        boy.dir = 0
        boy.frame = 0
        boy.wait_time = get_time()  # pico2d import 필요
        pass

    @staticmethod
    def exit(boy, e):
        if space_down(e):
            boy.fire_ball()


    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.face_dir == 1:
            boy.image_IDLE.clip_draw(0, 0, 53, 112, boy.x, boy.y, 140, 285)

        elif boy.face_dir == -1:
            boy.image_IDLE.clip_composite_draw(0, 0, 53, 112, 0, 'h', boy.x, boy.y,  140, 285)



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


class Venus:
    def __init__(self):
        self.x, self.y = 500, 200
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.image_WALK = load_image('resource/venus/venusWalk.png')
        self.image_IDLE = load_image('resource/venus/venusIdle.png')
        self.image_RUN = load_image('resource/venus/venusRun.png')
        self.image_PUNCH = load_image('resource/venus/venusPunch.png')
        self.image_KICK = load_image('resource/venus/venusKick.png')
        self.image_HPUI=load_image('resource/ui/hpUI2.png')
        self.image_jupiterUI=load_image('resource/ui/venusUI.png')
        self.image_RUNPUNCH=load_image('resource/venus/venusRunPunch.png')
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
        self.image_jupiterUI.clip_draw(0, 0, 246, 75,105,640,    160,70)

        for i in range(self.hp//10):
            self.image_HPUI.clip_draw(0, 0,  549, 41,    59+(38*i), 600,    38, 30)