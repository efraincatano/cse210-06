from cast.actor import Actor
import random
from cast.point import Point

class Cougar(Actor):

        def __init__(self, image):
            super().__init__(self)
            self._image = image
            self._roar = ""

        def get_image(self):
            return self._image

        def set_image(self, image):
            self._image = image

        def reset(self):
            x = random.randint(1, 40 - 1)
            y = random.randint(1, 20 - 1)
            position = Point(x, y)
            self.set_position(position)

        def get_position(self):
            return super().get_position()
