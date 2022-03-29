import pyray


class SoundService:

    def __init__(self):

        self._roar = pyray.load_sound("game/sound/roar.mp3")


    def roar(self):

        return pyray.play_sound(self._roar)