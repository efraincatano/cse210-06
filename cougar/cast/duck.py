from actor import Actor

class Duck(Actor):

        def __init__(self, image):
            super().__init__(self)
            self._image = image

        def get_draw(self):
            return self._image

        def set_draw(self):
            self._image = "i am a duck"
            return self._image
