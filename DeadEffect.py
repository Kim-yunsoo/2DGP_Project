from pico2d import load_image

import game_world


class DeadEffect:
    def __init__(self, type, dir, x, y):
        self.DeadEffect = load_image('resource/ui/DeadEffect.png')

        self.time = 0
        self.dir = dir
        self.type = type
        self.x = x + self.dir * 30
        self.y = y + 70

        self.type = type
        pass

    def update(self):
        self.time += 1
        if self.time == 300:
            game_world.remove_object(self)


    def draw(self):
        self.DeadEffect.clip_draw(0, 0, 78, 84, self.x, self.y, 90, 110)


