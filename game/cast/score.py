from actor import Actor

class Score(Actor):

    def __init__(self, player):
        super().__init__()
        self._player = player

