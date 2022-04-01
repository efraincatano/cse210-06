from cast.actor import Actor
import random
from cast.point import Point

class Duck(Actor):

        def __init__(self, image):
            super().__init__(self)
            self._image = image

        def get_image(self):
            return self._image

        def set_image(self, image):
            self._image = image

