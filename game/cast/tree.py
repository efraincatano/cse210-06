from email.mime import image
from actor import Actor

class Cougar(Actor):

        def __init__(self):
            super().__init__(self)
            self._image = image

        def get_draw(self):
            return self._image

        def set_draw(self):
            self._image = "i am a tree"
            return self._image
