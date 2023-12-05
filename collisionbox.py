from pico2d import draw_rectangle, load_image, load_wav

import game_world

class Collision:

    def __init__(self,type,dir,x,y):
        print("loglog")


        self.time=0
        if type == 'punch':
            self.dir=dir
            self.type=type
            self.x=x+dir*60
            self.y = y + 40
        if type == 'kick':
            self.dir=dir
            self.type=type
            self.x=x+dir*80
            self.y = y + 20
        if type == 'runpunch':
            self.dir=dir
            self.type=type
            self.x=x+dir*80
            self.y = y + 20



        self.type=type
        pass

    def get_bb(self):
        if self.type=='punch':
            return self.x - 20, self.y - 20, self.x + 20, self.y + 20  # 값 4개짜리 튜플 1
        if self.type=='kick':
            return self.x - 40, self.y - 20, self.x + 40, self.y + 20  # 값 4개짜리 튜플 1개
        if self.type == 'runpunch':
            return self.x - 20, self.y - 20, self.x + 20 ,self.y + 20  # 값 4개짜리 튜플 1개
    def update(self):
            self.time+=1
            if self.type=='punch' or self.type=='kick':
                self.y+=1
            if self.type == 'punch' or self.type == 'runpunch':
                self.x +=(self.dir)*1
            if self.time == 30:
             game_world.remove_object(self)




    def draw(self):
        draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 각각 인자로 전달해준다.


    def handle_collision(self, group, other):

        if group == 'player2:punch' or group == 'player1:punch'or group == 'player1:kick' or group == 'player2:kick'or group == 'player2:runpunch'or group == 'player1:runpunch':
            game_world.remove_object(self)




