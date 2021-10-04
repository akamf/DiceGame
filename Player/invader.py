from Player.player import Player


class Invader(Player):
    def __init__(self, name):
        super().__init__(name, 2)
        # shield = 1Dp, double shield = 2Dp etc. sword = 1Ap, double sword = 2Ap etc. draw card = draw bonus card
        self.dice = ["sword", "double sword", "triple sword", "triple sword", "draw card", "draw card"]
        # self.cards = {"battering ram", "fortified wall", "the plague"}

