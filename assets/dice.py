import random


class Dice:
    def __init__(self):
        self.dice = [
            'sword',
            'sword',
            'double sword',
            'double sword',
            'shield',
            'shield'
        ]

    def roll_dices(self, num_of_dices: int) -> list:
        return [self.dice[random.randrange(0, 6)] for _ in range(num_of_dices)]
