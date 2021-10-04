from Player.player import Player


class Defender(Player):
    def __init__(self, name):
        super().__init__(name, 3)
        # shield = 1Dp, double shield = 2Dp etc. sword = 1Ap, double sword = 2Ap etc.
        self.dice = ["shield", "double shield", "double shield", "triple shield", "sword", "double sword"]
