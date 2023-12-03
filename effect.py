from pico2d import draw_rectangle, load_image

import game_world

class Effect:
    def __init__(self,type,dir,x,y):
        self.basicEffect = load_image('resource/ui/basicEffect.png')
        self.strongEffect = load_image('resource/ui/StrongEffect.png')


        self.time=0
        if type == 'punch':
            self.dir=dir
            self.type=type
            self.x=x+self.dir*30
            print("self.dir")
            print(self.dir)
            self.y = y + 70
        if type == 'kick':
            self.dir=dir
            self.type=type
            self.x=x+dir*30
            self.y = y + 60
        # if type == 'runpunch':
        #     self.dir=dir
        #     self.type=type
        #     self.x=x+dir*80
        #     self.y = y + 20


        self.type=type
        pass

    # def get_bb(self):
    #     if self.type=='punch':
    #         return self.x - 20, self.y - 20, self.x + 20, self.y + 20  # 값 4개짜리 튜플 1
    #     if self.type=='kick':
    #         return self.x - 40, self.y - 20, self.x + 40, self.y + 20  # 값 4개짜리 튜플 1개
    #     if self.type == 'runpunch':
    #         return self.x - 20, self.y - 20, self.x + 20 ,self.y + 20  # 값 4개짜리 튜플 1개
    def update(self):
            self.time+=1

            if self.time == 300:
             game_world.remove_object(self)

    def draw(self):
        self.basicEffect.clip_draw(0, 0, 78, 84, self.x, self.y, 70, 80)

