import pyray
from raylib import DrawTexture, DrawTextureV, GetMousePosition, IsKeyPressed, IsMouseButtonDown, LoadTexture
import constants
from services.video_service import VideoService
from services.sound_service import SoundService
from cast.cougar import Cougar
from cast.duck import Duck
import constants
from cast.point import Point
import threading


class Director:

    def __init__(self):

        self._window = VideoService()
        self._sound = SoundService()
        self._cougar = Cougar("game/images/cougar.png")
        self._duck = Duck("game/images/duck.png")

    def start_game(self):

        #TODO: Find out how to load image cougar = LoadTexture("images/cougar.png")
        self._cougar.set_position = Point(constants.WIDTH/2, constants.HEIGHT/2)

        self._window.open_window()  
            # DrawTextureV(cougar, constants.WIDTH/2, constants.HEIGHT/2)self._window.draw_actor(self._cougar)
            # self._window._draw_grid()
        cougar = pyray.load_texture(self._cougar.get_image())
            
        while self._window.is_window_open():
            self._window._draw_grid()
            # DrawTextureV(cougar, constants.WIDTH/2, constants.HEIGHT/2)
            self._window.draw_actor(self._cougar)
            self._window.draw_actor(self._duck)
            self._window.clear_buffer()
            self._window.flush_buffer()
            threading.Timer(3.0, self._cougar.reset).start()
            threading.Timer(1.0, self._duck.reset).start()

        