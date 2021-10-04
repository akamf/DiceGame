import random

from Player.defender import Defender
from Player.invader import Invader

NUMBER_OF_ROLLS = 3


def roll_dice(dice: list) -> int:
    return dice[random.randrange(0, 6)]


class Game:
    def __init__(self):
        self.invader = Invader("Invader")
        self.defender = Defender("Defender")
        self.active_player = self.defender.name

    def dice_result(self):
        def defender_roll():
            for i in range(NUMBER_OF_ROLLS):
                dice_roll = []
                for _ in range(self.defender.number_of_dices):
                    dice_roll.append(roll_dice(self.defender.dice))

                if i == NUMBER_OF_ROLLS - 1:
                    for dice in dice_roll:
                        self.defender.dices.append(dice)
                    break

                else:
                    if self.defender.number_of_dices == 3:
                        keep = input(f"1. {roll_dice[0]}\n2. {roll_dice[1]}\n3. {roll_dice[2]}"
                                     f"\n\nDo you want to keep any? ")
                    elif self.defender.number_of_dices == 2:
                        keep = input(f"1. {roll_dice[0]}\n2. {roll_dice[1]}\n\nDo you want to keep any? ")
                    elif self.defender.number_of_dices == 1:
                        keep = input(f"1. {roll_dice[0]}\n\nDo you want to keep any? ")

                if keep.lower() == "y":
                    num = input("Enter the number(s) of the dices to keep: ")
                    for i in num.split():
                        self.defender.dices.append(roll_dice[int(i) - 1])
                    self.defender.number_of_dices -= len(self.defender.dices)

                if len(self.defender.dices) == 3 or self.defender.number_of_dices == 0:
                    break
