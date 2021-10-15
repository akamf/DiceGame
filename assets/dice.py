import random
from time import sleep


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
        """
        Function to simulate the dice rolls
        :param num_of_dices: Number of dices to roll
        :return: A list of the dices results
        """
        sleep(1)
        return [self.dice[random.randrange(0, 6)] for _ in range(num_of_dices)]
