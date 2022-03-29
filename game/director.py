from pyray import *
from raylib import DrawTexture, DrawTextureV, LoadTexture
import constants
from services.video_service import VideoService
from services.sound_service import SoundService
from cast.cougar import Cougar
import constants
from cast.point import Point

class Director:

    def __init__(self):

        self._window = VideoService()
        self._sound = SoundService()
        self._cougar = Cougar("game/images/cougar.png")

    def start_game(self):

        #TODO: Find out how to load image cougar = LoadTexture("images/cougar.png")
        self._cougar.set_position = Point(constants.WIDTH/2, constants.HEIGHT/2)

        self._window.open_window()   
        while self._window.is_window_open():
            # DrawTextureV(cougar, constants.WIDTH/2, constants.HEIGHT/2)self._window.draw_actor(self._cougar)
            # self._window._draw_grid()
            self._window.draw_actor(self._cougar)
            self._sound.roar()
            self._window.clear_buffer()
            self._window.flush_buffer()

        