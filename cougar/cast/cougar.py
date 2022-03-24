from actor import Actor
import random
from point import Point

class Cougar(Actor):

        def __init__(self, image):
            super().__init__(self)
            self._image = self.get_draw()
            self._roar = ""

        def get_draw(self):
            return self._image

        def set_draw(self):
            self._image = "i am a cougar"
            return self._image

        def reset(self):
            self._points = random.randint(1, 8)
            x = random.randint(1, 40 - 1)
            y = random.randint(1, 20 - 1)
            position = Point(x, y)
            self.set_position(position)
