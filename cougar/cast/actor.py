
class Actor:
        def __init__(self, image, position):

            self._image = self.get_image
            self._position = position

        def get_image(self, image):
            return self._image

        def get_position(self):
            return self._position

        def set_image(self, image):
            self._image = image

        def set_position(self):
            self._position = "some place ramdon"
            return self._position



