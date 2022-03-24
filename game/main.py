from director import Director
from cougar.cast import Cast
from cougar.cast import Cougar

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("cougar", Cougar())

main()

game = Director()
game.start_game()
