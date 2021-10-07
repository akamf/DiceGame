import random
from Player.player import Player
from game_data import invader_cards


class Invader(Player):
    def __init__(self, name):
        super().__init__(name)
        self.number_of_cards = 0
        self.cards = []

    def draw_cards(self):
        for _ in range(self.number_of_cards):
            self.cards.append(invader_cards[random.randrange(0, len(invader_cards))])
