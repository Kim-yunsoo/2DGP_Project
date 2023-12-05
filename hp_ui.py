from pico2d import load_image


class HPUI:
    def __init__(self,round):
        self.round=round
        self.hpui1_image=load_image('resource/ui/hpUI1.png')
        self.mid_image = load_image('resource/ui/midUI.png')

        if self.round == 1:
            self.round1_image=load_image('resource/ui/Round1.png')
        if self.round == 2:
            self.round2_image=load_image('resource/ui/Round2.png')
        if self.round == 3:
            self.round3_image=load_image('resource/ui/Round3.png')


    def draw(self):
        self.mid_image.draw(500, 620)
        #주인공쪽
        self.hpui1_image.clip_draw(0,0,549,41,  230,600,    380,30)
        self.hpui1_image.clip_draw(0,0,549,41,  770,600,    380,30)
        if self.round==1:
            self.round1_image.clip_draw(0,0,240,76, 520,550, 220,56 )
        if self.round == 2:
            self.round2_image.clip_draw(0, 0, 240, 76, 520, 550, 220, 56)
        if self.round == 3:
            self.round3_image.clip_draw(0, 0, 240, 76, 520, 550, 220, 56)



    def update(self):
        pass
