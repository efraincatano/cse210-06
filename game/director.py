from concurrent.futures import thread
import random
import pyray
import raylib
import constants
from services.video_service import VideoService
from services.sound_service import SoundService
from cast.cougar import Cougar
from cast.duck import Duck
import constants
from cast.point import Point
import time

class Director:

    def __init__(self):

        self._window = VideoService()
        self._sound = SoundService()
        self._cougar = Cougar("game/images/cougar.png")
        self._duck = Duck("game/images/duck.png")

    def start_game(self):

        self._window.open_window()  
        cougar = pyray.load_texture(self._cougar.get_image())
        duck = pyray.load_texture(self._duck.get_image())
        cougar_width = cougar.width
        cougar_height = cougar.height
            
        while self._window.is_window_open():

            gotcha = False

            while not gotcha:

                random_positon = (random.randint(600, 1000), random.randint(300, 600))

                pyray.begin_drawing()

                pyray.clear_background((0,0,0))
                pyray.draw_texture_ex(cougar, random_positon, 0, 0.2, (255,255,255))
                WHITE = (123, 255, 255)
                pyray.draw_text("Score", 100, 100, 50, WHITE)
                
                random_positon = Point(random.randint(600, 1000), random.randint(300, 600))

                self._cougar.reset(random_positon)
    
                pyray.end_drawing()

                if raylib.IsMouseButtonDown(0):
                    mouse_x = pyray.get_mouse_x()
                    mouse_y = pyray.get_mouse_y()
                    print(f"Cougar x = {self._cougar.get_position().get_x()}")

                    if mouse_x in range(self._cougar.get_position().get_x() - 200, self._cougar.get_position().get_x() + 200) and mouse_y in range(self._cougar.get_position().get_y() - 200, self._cougar.get_position().get_y() + 200):
                        print("Gotcha!")
                        print(f"Cougar x = {self._cougar.get_position().get_x()}")
                        print(f"Cougar y = {self._cougar.get_position().get_y()}")
                        gotcha = True

        pyray.unload_texture(cougar)
            

        