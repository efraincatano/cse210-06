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

            if IsMouseButtonDown(0):
                mouse_x = pyray.get_mouse_x()
                mouse_y = pyray.get_mouse_y()

                if mouse_x or mouse_y == cougar.get_position():
                    print("Gotcha!")
                    print(f"Mouse x = {mouse_x}")
                    print(f"Mouse y = {mouse_y}")
               
            pyray.begin_drawing()
            WHITE = (255, 255, 255)
            pyray.draw_text("Score", 10, 10, 50, WHITE)

            pyray.clear_background((0,0,0))
            pyray.draw_texture_ex(cougar, (300, 300), 0, 1, (255,255,255))
            
            threading.Timer(3.0, self._cougar.reset()).start()
            threading.Timer(1.0, self._duck.reset()).start()
            pyray.end_drawing()

        pyray.unload_texture(cougar)
            

        