from pico2d import load_image


class HPUI:
    def __init__(self):
        self.hpui1_image=load_image('resource/ui/hpUI1.png')
        self.mid_image = load_image('resource/ui/midUI.png')

    def draw(self):
        self.mid_image.draw(500, 620)
        #주인공쪽
        self.hpui1_image.clip_draw(0,0,549,41,  230,600,    380,30)
        self.hpui1_image.clip_draw(0,0,549,41,  770,600,    380,30)

    def update(self):
        pass
