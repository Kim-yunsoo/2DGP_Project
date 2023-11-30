from pico2d import draw_rectangle, load_image

import game_world

class StrongEffect:
    def __init__(self,type,dir,x,y):
        self.strongEffect = load_image('resource/ui/StrongEffect.png')


        self.time=0
        self.dir=dir
        self.type=type
        self.x=x+dir*30
        self.y = y + 60
    def update(self):
            self.time+=1

            if self.time == 300:
             game_world.remove_object(self)
    def draw(self):
        self.strongEffect.clip_draw(0,0,51,57,self.x,self.y,80,80)




