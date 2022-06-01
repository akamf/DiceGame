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
            'double shield'
        ]

    def roll_dices(self, num_of_dices: int) -> list:
        """
        Method to simulate the dices results
        :param num_of_dices: int, number of dices to roll
        :return: list
        """
        sleep(1)
        return [self.dice[random.randrange(0, 6)] for _ in range(num_of_dices)]
