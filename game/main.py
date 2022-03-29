from director import Director
from cast.cast import Cast
from cast.cougar import Cougar

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("cougar", Cougar("game/images/cougar.png"))
    cast.add_actor("duck", Cougar("game/images/duck.png"))

main()

game = Director()
game.start_game()
