# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, clamp, \
    draw_rectangle, load_wav
from sdl2 import SDLK_LSHIFT, SDLK_LCTRL, SDLK_a, SDLK_s, SDLK_RSHIFT, SDLK_g, SDLK_4, SDLK_d, SDLK_h, SDLK_5, SDLK_j, \
    SDLK_6, SDLK_KP_5, SDLK_KP_4, SDLK_KP_6

import game_framework
import play_mode2
import play_mode3
from DeadEffect import DeadEffect
from StrongEffect import StrongEffect
from collisionbox import Collision
import play_mode
import game_world
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
def damage(e):
    return e[0] == 'DAMAGE'
def dead(e):
    return e[0] == 'DEAD'
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
            boy.image_IDLE.clip_draw(0, 0, 46, 109, boy.x, boy.y, 130, 280)
            # boy.image_PUNCH.clip_draw(0, 0, 65, 110, boy.x , boy.y,  180, 280)
            # boy.image_WALK.clip_draw(498, 0, 44, 115, boy.x, boy.y, 130, 280)





        elif boy.face_dir == -1:
            # boy.image_KICK.clip_draw(0, 0, 79, 115, boy.x, boy.y, 196, 280)
            boy.image_IDLE.clip_composite_draw(0, 0, 46, 109, 0, 'h', boy.x, boy.y,  130, 280)

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
        # boy.frame = (boy.frame + 1) % 8
        # boy.x += boy.dir * 5

        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        # boy.x += boy.dir * 5
        boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(60, boy.x, 1000 - 60)

        pass

    @staticmethod
    def draw(boy):
        pix_posx = [8, 50, 90, 134, 180, 223, 267, 318, 367, 413, 452, 498]
        if boy.face_dir == 1:
            boy.image_WALK.clip_draw(pix_posx[int(boy.frame)], 0, 44, 115, boy.x, boy.y, 130, 280)

        elif boy.face_dir == -1:
            boy.image_WALK.clip_composite_draw(pix_posx[int(boy.frame)], 0, 44, 115, 0, 'h', boy.x, boy.y, 130, 280)



class Run:
    @staticmethod
    def enter(boy, e):
        if boy.playernum == 1:
            if (d_down(e) and StateMachine.isdash1) or (a_up(e) and StateMachine.isdash1):  # 오른쪽으로 RUN
                boy.dir, boy.face_dir = 1, 1
            elif (a_down(e) and StateMachine.isdash1) or (d_up(e) and StateMachine.isdash1):  # 왼쪽으로 RUN
                boy.dir, boy.face_dir = -1, -1

        elif boy.playernum == 2:
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
        pix_posx = [0, 102, 197, 305, 410, 505]

        if boy.face_dir == 1:
                 boy.image_RUN.clip_draw(pix_posx[int(boy.frame)], 0, 84, 99, boy.x, boy.y, 220, 280)

        elif boy.face_dir == -1:
                boy.image_RUN.clip_composite_draw(pix_posx[int(boy.frame)], 0, 84, 99, 0, 'h',boy.x, boy.y,220, 280)

        # boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)



class Punch:
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

        if boy.playernum == 1:
            punchCollision = Collision('punch', boy.face_dir, boy.x, boy.y)
            game_world.add_object(punchCollision)
            game_world.add_collision_pair('player2:punch', P2, punchCollision)
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
            game_world.add_collision_pair('player1:punch', P1, punchCollision)
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
        pix_posX = [0, 62]

        if boy.face_dir == 1:
                boy.image_PUNCH.clip_draw(pix_posX[int(boy.frame)], 0, 65, 110, boy.x+20 , boy.y,  180, 280)
        elif boy.face_dir == -1:
                 boy.image_PUNCH.clip_composite_draw(pix_posX[int(boy.frame)], 0, 65, 110, 0, 'h', boy.x-20 , boy.y,  180, 280)


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
        pix_posx = [7, 100, 190]

        if boy.face_dir == 1:
            boy.image_KICK.clip_draw(pix_posx[int(boy.frame)], 0, 93, 109, boy.x+30, boy.y, 250, 280)


        elif boy.face_dir == -1:
            boy.image_KICK.clip_composite_draw(pix_posx[int(boy.frame)], 0, 93, 109, 0, 'h', boy.x-30, boy.y, 250, 280)
class RunKick:
    @staticmethod
    def enter(boy, e):
        boy.frame=0
        if boy.round == 1:
            P1 = play_mode.player1
            P2 = play_mode.player2
        elif boy.round == 2:
            P1 = play_mode2.player1
            P2 = play_mode2.player2
        elif boy.round == 3:
            P1 = play_mode3.player1
            P2 = play_mode3.player2

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
            game_world.add_collision_pair('player1:runpunch', P1, punchCollision)
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
        if int(boy.frame) > 2:
            boy.frame = 0
            boy.state_machine.handle_event(('TIME_OUT', 0))



        pass
    @staticmethod
    def draw(boy):
        pix_posX = [6, 103, 211]

        if boy.face_dir == 1:
            boy.image_RUNKICK.clip_draw(pix_posX[int(boy.frame)], 0, 97, 106, boy.x + 30, boy.y + 10, 300, 290)

        elif boy.face_dir == -1:
            boy.image_RUNKICK.clip_composite_draw(pix_posX[int(boy.frame)], 0,  97, 106, 0, 'h', boy.x-30,  boy.y + 10, 300, 290)



class Damage:
    def enter(boy, e):
        boy.frame = 0

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time)  # % 6   Add

        if int(boy.frame) > 1:
            boy.frame = 0
            boy.state_machine.handle_event(('TIME_OUT', 0))

            # boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time) % 6
        # boy.x += boy.dir * (RUN_SPEED_PPS+100) * game_framework.frame_time
        # boy.x = clamp(60, boy.x, 1000 - 60)

        pass

    @staticmethod
    def draw(boy):
        if boy.face_dir == 1:
            # boy.image_KICK.clip_draw(0, 0, 70, 114, boy.x, boy.y + 10, 220, 280)
            boy.image_DAMAGE.clip_draw(0, 0, 60, 111, boy.x, boy.y , 180, 280)
        elif boy.face_dir == -1:
            boy.image_DAMAGE.clip_composite_draw(0, 0, 60, 111, 0, 'h', boy.x, boy.y , 180, 280)


class Dead:
    def enter(boy, e):
        boy.frame = 0
        boy.newtime=get_time()

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time)  # % 6   Add

        if int(boy.frame) > 3:
            boy.frame = 3

        if get_time() - boy.newtime > 5:
            boy.y = 1000
            boy.x = 1000
            if boy.round == 1:
                play_mode.next = True
            if play_mode.player1_score == 2:
                play_mode.next = False
                play_mode2.go_round3 = False
                play_mode2.player1_Win = True
            elif play_mode.player2_score == 2:
                play_mode.next = False
                play_mode2.go_round3 = False
                play_mode2.player2_Win = True
            elif play_mode.player1_score == 1 and play_mode.player2_score == 1:
                play_mode.next = False
                play_mode2.go_round3 = True

            # 버그 막기


            # boy.frame = (boy.frame + (FRAMES_PER_ACTION) * ACTION_PER_TIME * game_framework.frame_time) % 6
        # boy.x += boy.dir * (RUN_SPEED_PPS+100) * game_framework.frame_time
        # boy.x = clamp(60, boy.x, 1000 - 60)

        pass

    @staticmethod
    def draw(boy):
        pix_posx = [0, 109, 227, 367]
        if boy.face_dir == 1:
            # boy.image_KICK.clip_draw(0, 0, 70, 114, boy.x, boy.y + 10, 220, 280)
            boy.image_DEAD.clip_draw(pix_posx[int(boy.frame)],0,123,115,boy.x, boy.y,290,305)
        elif boy.face_dir == -1:
            boy.image_DEAD.clip_composite_draw(pix_posx[int(boy.frame)], 0, 123, 115, 0, 'h', boy.x, boy.y, 290, 305)


class StateMachine:
    isdash1 = False
    ispunch1 = True
    iskick1 = True
    isspace1=False

    isdash2 = False
    ispunch2 = True
    iskick2 = True
    isspace2 = False
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        if boy.playernum == 1:
            self.transitions = {
                Idle: {d_down: Walk, a_down: Walk, a_up: Idle, d_up: Idle, h_down: Idle,
                       g_down: Punch, j_down: Kick,damage:Damage,dead:Dead},
                Walk: {d_down: Idle, damage:Damage,a_down: Idle, d_up: Idle, a_up: Idle, shift_downL: Run, g_down: Punch,
                       j_down: Kick,dead:Dead },
                Run: { d_up: Idle, a_up: Idle, d_down: Idle, a_down: Idle, g_down: Punch,
                      j_down: Kick, h_down: RunKick,damage:Damage,dead:Dead},
                Punch: {d_down: Walk, a_down: Walk, j_down: Kick, time_out: Idle,damage:Damage,dead:Dead},
                Kick: {d_down: Walk, a_down: Walk, g_down: Punch, time_out: Idle,damage:Damage,dead:Dead},
                RunKick: {time_out: Idle,damage:Damage,dead:Dead},
                Damage:{time_out:Idle},
                Dead:{}
            }
        elif boy.playernum == 2:
            self.transitions = {
                Idle: {right_down: Walk, left_down: Walk, left_up: Idle, right_up: Idle, num5_down: Idle,
                       num4_down: Punch, num6_down: Kick,damage:Damage,dead:Dead},
                Walk: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, shift_downR: Run, num4_down: Punch,
                       num6_down: Kick,damage:Damage,dead:Dead },
                Run: { right_up: Idle, left_up: Idle,right_down: Idle, left_down: Idle, num4_down: Punch,
                      num6_down: Kick
                    , num5_down: RunKick,damage:Damage,dead:Dead},
                Punch: {right_down: Walk, left_down: Walk, num6_down: Kick, time_out: Idle,damage:Damage,dead:Dead},
                Kick: {right_down: Walk, left_down: Walk, num4_down: Punch, time_out: Idle,damage:Damage,dead:Dead},
                RunKick: {time_out: Idle}
                ,Damage:{time_out:Idle},
                Dead: {}
            }


    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)

    def handle_event(self, e):
        if shift_downR(e):
            StateMachine.isdash2=True
        elif shift_upR(e):
            StateMachine.isdash2 = False

        if shift_downL(e):
            StateMachine.isdash1 = True
        elif shift_upL(e):
            StateMachine.isdash1 = False

        # if a_down(e):
        #     StateMachine.ispunch = True
        if g_up(e):
            StateMachine.ispunch1 = True
        if num4_up(e):
            StateMachine.ispunch2 = True


        if h_down(e):
            StateMachine.isspace1=True
        elif h_up(e):
            StateMachine.isspace1 = False

        if num5_down(e):
            StateMachine.isspace2 = True
        elif num5_up(e):
            StateMachine.isspace2 = False

        if j_up(e):
            StateMachine.iskick1 = True
        if num6_up(e):
            StateMachine.iskick2 = True


        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.boy)


class Mars:
    def __init__(self):
        self.x, self.y = 500,200
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.image_WALK = load_image('resource/mars/marsWalk.png')
        self.image_IDLE = load_image('resource/mars/marsIdle.png')
        self.image_RUN = load_image('resource/mars/marsRun.png')
        self.image_PUNCH = load_image('resource/mars/marsPunch.png')
        self.image_KICK=load_image('resource/mars/marsKick.png')
        self.image_HPUI=load_image('resource/ui/hpUI2.png')
        self.image_jupiterUI=load_image('resource/ui/marsUI.png')
        self.image_RUNKICK=load_image('resource/mars/marsRunKick.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.item = None
        self.hp=100

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        # for i in range(self.hp//10) :

        self.state_machine.draw()
        self.image_jupiterUI.clip_draw(0, 0, 157, 75, 105,640,    160,70)

        for i in range(self.hp//10):
            self.image_HPUI.clip_draw(0, 0,  549, 41,    59+(38*i), 600,    38, 30)