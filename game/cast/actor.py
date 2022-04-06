import constants
from cast.point import Point
import random

class Actor:
        def __init__(self, image):

            self._image = image
            self._position = Point(0,0)
            self._font_size = constants.CELL_SIZE

        def get_image(self, image):
            return self._image

        def get_position(self):
            return self._position

        def set_image(self, image):
            self._image = image

        def set_position(self, position):
            self._position = position

        def get_font_size(self):
            return self._font_size

        def reset(self, position):
            self.set_position(position)

             



