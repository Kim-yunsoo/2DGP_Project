# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, clamp, \
    draw_rectangle, load_wav
from sdl2 import SDLK_LSHIFT, SDLK_LCTRL, SDLK_a, SDLK_s, SDLK_RSHIFT, SDLK_g, SDLK_4, SDLK_d, SDLK_h, SDLK_5, SDLK_j, \
    SDLK_6, SDLK_KP_5, SDLK_KP_4, SDLK_KP_6

import game_framework
import game_world
import play_mode2
import play_mode3
from DeadEffect import DeadEffect
from StrongEffect import StrongEffect
from collisionbox import Collision
import play_mode
from effect import Effect

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
def damage(e):
    return e[0] == 'DAMAGE'
def dead(e):
    return e[0] == 'DEAD'
def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def d_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def d_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


#강력편치
def h_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_h
def h_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_h

def num5_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_5
def num5_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_5

def shift_downL(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LSHIFT
def shift_downR(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RSHIFT

def shift_upL(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LSHIFT
def shift_upR(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RSHIFT


def g_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_g
def g_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_g and StateMachine.ispunch1

def num4_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_4
def num4_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_4 and StateMachine.ispunch2

def time_out(e):
    return e[0] == 'TIME_OUT'
def j_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_j and StateMachine.iskick1
def j_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_j
def num6_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_6 and StateMachine.iskick2
def num6_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_6


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
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        if get_time() - boy.wait_time > 2:
            boy.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(boy):
        if boy.face_dir == 1:
            boy.image_IDLE.clip_draw(0, 0, 55, 111, boy.x, boy.y, 150, 280)


        elif boy.face_dir == -1:
            # boy.image_KICK.clip_draw(0, 0, 79, 115, boy.x, boy.y, 196, 280)
            boy.image_IDLE.clip_composite_draw(0, 0, 55, 111, 0, 'h', boy.x, boy.y,  150, 280)


class Walk:

    @staticmethod
    def enter(boy, e):
        if boy.playernum == 2:
            if right_down(e) or left_up(e):  # 오른쪽으로 RUN
                boy.dir, boy.action, boy.face_dir = 1, 1, 1
            elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
                boy.dir, boy.action, boy.face_dir = -1, 0, -1
        elif boy.playernum == 1:
            if d_down(e) or a_up(e):  # 오른쪽으로 RUN
                boy.dir, boy.action, boy.face_dir = 1, 1, 1
            elif a_down(e) or d_up(e):  # 왼쪽으로 RUN
                boy.dir, boy.action, boy.face_dir = -1, 0, -1

    @staticmethod
    def exit(boy, e):

        pass

    @staticmethod
    def do(boy):

        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(60, boy.x, 1000 - 60)

        pass

    @staticmethod
    def draw(boy):
        pix_posx = [0, 49, 95, 140, 185, 235, 288, 345, 400, 448, 495, 537]
        if boy.face_dir == 1:
            boy.image_WALK.clip_draw(pix_posx[int(boy.frame)], 0, 49, 115, boy.x, boy.y, 130, 280)
        elif boy.face_dir == -1:
            boy.image_WALK.clip_composite_draw(pix_posx[int(boy.frame)], 0, 49, 115, 0, 'h', boy.x, boy.y, 130, 280)



class Run:
    @staticmethod
    def enter(boy, e):
        if boy.playernum==1:
            if (d_down(e) and StateMachine.isdash1) or (a_up(e) and StateMachine.isdash1):  # 오른쪽으로 RUN
                boy.dir, boy.face_dir = 1, 1
            elif (a_down(e) and StateMachine.isdash1) or (d_up(e) and StateMachine.isdash1):  # 왼쪽으로 RUN
                boy.dir, boy.face_dir = -1, -1

        elif boy.playernum==2:
            if (right_down(e) and StateMachine.isdash2) or (left_up(e) and StateMachine.isdash2):  # 오른쪽으로 RUN
                boy.dir, boy.face_dir = 1, 1
            elif (left_down(e) and StateMachine.isdash2) or (right_up(e) and StateMachine.isdash2):  # 왼쪽으로 RUN
                boy.dir, boy.face_dir = -1, -1

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
        pix_posx = [4, 85, 158, 230, 310,380]
        if boy.face_dir == 1:
                 boy.image_RUN.clip_draw(pix_posx[int(boy.frame)], 0, 73, 110, boy.x, boy.y,230, 280)

        elif boy.face_dir == -1:
                boy.image_RUN.clip_composite_draw(pix_posx[int(boy.frame)], 0, 73, 110, 0, 'h',boy.x, boy.y, 230, 280)

        # boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)


class Punch:
    @staticmethod
    def enter(boy, e):
        if boy.round == 1:
            P1 = play_mode.player1
            P2 = play_mode.player2
        elif boy.round == 2:
            P1 = play_mode2.player1
            P2 = play_mode2.player2
        elif boy.round == 3:
            P1 = play_mode3.player1
            P2 = play_mode3.player2
        boy.frame=0
        if boy.playernum == 1:
            punchCollision = Collision('punch', boy.face_dir, boy.x, boy.y)
            game_world.add_object(punchCollision)
            game_world.add_collision_pair('player2:punch',P2, punchCollision)
            if (d_down(e) and StateMachine.isdash1 and StateMachine.ispunch1) or (
                    d_up(e) and StateMachine.isdash1 and StateMachine.ispunch1) or (
                    d_down(e) and StateMachine.ispunch1):  # 오른쪽으로 RUN
                boy.dir, boy.action, boy.face_dir = 1, 1, 1
            elif (a_down(e) and StateMachine.isdash1 and StateMachine.ispunch1) or (
                    a_up(e) and StateMachine.isdash1 and StateMachine.ispunch1) or (
                    a_down(e) and StateMachine.ispunch1):  # 왼쪽으로 RUN
                boy.dir, boy.action, boy.face_dir = -1, 0, -1
        elif boy.playernum == 2:
            punchCollision = Collision('punch', boy.face_dir, boy.x, boy.y)
            game_world.add_object(punchCollision)
            game_world.add_collision_pair('player1:punch', P1 ,punchCollision)
            if (right_down(e) and StateMachine.isdash2 and StateMachine.ispunch2) or (
                    right_up(e) and StateMachine.isdash2 and StateMachine.ispunch2) or (
                    right_down(e) and StateMachine.ispunch2):  # 오른쪽으로 RUN
                boy.dir, boy.action, boy.face_dir = 1, 1, 1
            elif (left_down(e) and StateMachine.isdash2 and StateMachine.ispunch2) or (
                    left_up(e) and StateMachine.isdash2 and StateMachine.ispunch2) or (
                    left_down(e) and StateMachine.ispunch2):  # 왼쪽으로 RUN
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
            if boy.playernum == 1:
                StateMachine.ispunch1 = False
            elif boy.playernum == 2:
                StateMachine.ispunch2 = False
            boy.state_machine.handle_event(('TIME_OUT', 0))



        pass
    @staticmethod
    def draw(boy):
        global ispush
        pix_posX=[0,90]
        if boy.face_dir == 1:
                boy.image_PUNCH.clip_draw(pix_posX[int(boy.frame)], 0, 72, 110, boy.x + 30, boy.y, 200, 280)
        elif boy.face_dir == -1:
                 boy.image_PUNCH.clip_composite_draw(pix_posX[int(boy.frame)], 0, 72, 110, 0, 'h', boy.x-30, boy.y, 200, 280)

class Kick:
    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        if boy.round == 1:
            P1 = play_mode.player1
            P2 = play_mode.player2
        elif boy.round == 2:
            P1 = play_mode2.player1
            P2 = play_mode2.player2
        elif boy.round == 3:
            P1 = play_mode3.player1
            P2 = play_mode3.player2
        if boy.playernum == 2:
            punchCollision = Collision('kick', boy.face_dir, boy.x, boy.y)
            game_world.add_object(punchCollision)
            game_world.add_collision_pair('player1:kick', P1, punchCollision)
            if ((right_down(e) and StateMachine.isdash2 and StateMachine.iskick2)
                    or (right_up(e) and StateMachine.isdash2 and StateMachine.iskick2)
                    or (right_down(e) and StateMachine.iskick2)):  # 오른쪽으로 RUN
                boy.face_dir = 1
            elif ((left_down(e) and StateMachine.isdash2 and StateMachine.iskick2)
                  or (left_up(e) and StateMachine.isdash2 and StateMachine.iskick2)
                  or (left_down(e) and StateMachine.iskick2)):  # 왼쪽으로 RUN
                boy.face_dir = -1

        if boy.playernum == 1:
            punchCollision = Collision('kick', boy.face_dir, boy.x, boy.y)
            game_world.add_object(punchCollision)
            game_world.add_collision_pair('player2:kick', P2, punchCollision)
            if ((d_down(e) and StateMachine.isdash1 and StateMachine.iskick1)
                    or (d_up(e) and StateMachine.isdash1 and StateMachine.iskick1)
                    or (d_down(e) and StateMachine.iskick1)):  # 오른쪽으로 RUN
                boy.face_dir = 1
            elif ((a_down(e) and StateMachine.isdash1 and StateMachine.iskick1)
                  or (a_up(e) and StateMachine.isdash1 and StateMachine.iskick1)
                  or (a_down(e) and StateMachine.iskick1)):  # 왼쪽으로 RUN
                boy.face_dir = -1
        boy.frame = 0   #Add

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time)# % 6   Add
        if int(boy.frame) > 1:
            boy.frame = 0
            if boy.playernum == 1:
                StateMachine.iskick1 = False
            if boy.playernum == 2:
                StateMachine.iskick2 = False
            boy.state_machine.handle_event(('TIME_OUT', 0))

            # boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time) % 6
        # boy.x += boy.dir * (RUN_SPEED_PPS+100) * game_framework.frame_time
        # boy.x = clamp(60, boy.x, 1000 - 60)

        pass
    @staticmethod
    def draw(boy):
        pix_posx=[206,320,450]

        if boy.face_dir == 1:
            boy.image_KICK.clip_draw(pix_posx[int(boy.frame)], 0, 95, 112, boy.x, boy.y + 10, 250, 280)

        elif boy.face_dir == -1:
            boy.image_KICK.clip_composite_draw(pix_posx[int(boy.frame)], 0, 95, 112, 0, 'h', boy.x, boy.y+10, 250, 280)
class RunPunch:
    @staticmethod
    def enter(boy, e):
        if boy.round == 1:
            P1 = play_mode.player1
            P2 = play_mode.player2
        elif boy.round == 2:
            P1 = play_mode2.player1
            P2 = play_mode2.player2
        elif boy.round == 3:
            P1 = play_mode3.player1
            P2 = play_mode3.player2
        boy.frame=0
        if boy.playernum == 1:
            punchCollision = Collision('runpunch', boy.face_dir, boy.x, boy.y)
            game_world.add_object(punchCollision)
            game_world.add_collision_pair('player2:runpunch', P2, punchCollision)
            if (StateMachine.isspace1 and d_down(e)) or (StateMachine.isspace1 and d_up(e)):  # 오른쪽으로 RUN
                boy.face_dir = 1
            elif (StateMachine.isspace1 and a_down(e)) or (StateMachine.isspace1 and a_up(e)):  # 왼쪽으로 RUN
                boy.face_dir = -1

        if boy.playernum == 2:
            punchCollision = Collision('runpunch', boy.face_dir, boy.x, boy.y)
            game_world.add_object(punchCollision)
            game_world.add_collision_pair('player1:runpunch',P1, punchCollision)
            if (StateMachine.isspace2 and right_down(e)) or (StateMachine.isspace2 and right_up(e)):  # 오른쪽으로 RUN
                boy.face_dir = 1
            elif (StateMachine.isspace2 and left_down(e)) or (StateMachine.isspace2 and left_up(e)):  # 왼쪽으로 RUN
                boy.face_dir = -1

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time)
        if int(boy.frame) > 3:
            boy.frame = 0
            boy.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(boy):
        pix_posX = [2, 76, 160, 242]

        if boy.face_dir == 1:
            boy.image_RUNPUNCH.clip_draw(pix_posX[int(boy.frame)],0, 85, 113, boy.x + 10, boy.y + 10, 230, 290)
        elif boy.face_dir == -1:
            boy.image_RUNPUNCH.clip_composite_draw(pix_posX[int(boy.frame)], 0, 85, 113, 0, 'h', boy.x-10,  boy.y + 10, 230, 290)

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

        if space_down(e):
            StateMachine.isspace=True
        elif space_up(e):
            StateMachine.isspace = False
        if a_up(e):
            StateMachine.ispunch = True

        if s_up(e):
            StateMachine.iskick = True



        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.boy)


class Jupiter:
    def __init__(self):
        self.x, self.y = 500, 200
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.image_WALK = load_image('resource/jupiter/jupiterWalk.png')
        self.image_IDLE = load_image('resource/jupiter/jupiterIdle.png')
        self.image_RUN = load_image('resource/jupiter/jupiterRun.png')
        self.image_PUNCH = load_image('resource/jupiter/jupiterPunch.png')

        self.image_KICK=load_image('resource/jupiter/jupiterKick.png')
        self.image_HPUI=load_image('resource/ui/hpUI2.png')
        self.image_jupiterUI=load_image('resource/ui/jupiterUI.png')
        self.image_RUNPUNCH = load_image('resource/jupiter/jupiterRunPunch.png')
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

        self.state_machine.draw()
        self.image_jupiterUI.clip_draw(0, 0, 228, 75, 110,640,    160,70)

        for i in range(self.hp//10):
            self.image_HPUI.clip_draw(0, 0,  549, 41,    59+(38*i), 600,    38, 30)
