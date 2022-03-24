from pyray import *
from raylib import DrawTexture, DrawTextureV, LoadTexture
import constants
from services.video_service import VideoService
class Director:

    def __init__(self):

        self._window = VideoService()

    def start_game(self):

        #TODO: Find out how to load image cougar = LoadTexture("images/cougar.png")
        

        self._window.open_window()
        while self._window.is_window_open():
            self._window._draw_grid()
            # DrawTextureV(cougar, constants.WIDTH/2, constants.HEIGHT/2)
            self._window.clear_buffer()
            self._window.flush_buffer()

        