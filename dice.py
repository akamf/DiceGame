import random
import game_data
from time import sleep

from Player.player import Player


class Dice:
    def __init__(self):
        self.dice_type = None
        self.dices = []

    @staticmethod
    def roll(dice: list) -> int:
        """
        Function to present a dice roll
        :param dice: The type of dice to use
        :return: The value of the side that the dice shows
        """
        return dice[random.randrange(0, 6)]

    def set_dice_value(self, remaining_dices: int, active_player):
        """
        Set and display the value of the dices rolled by the current players individual dice
        :param remaining_dices: An int between 0 and 3, to see how many dices the player currently has
        :param active_player: A Player object containing the current player
        """
        self.dice_type = game_data.defender_dice if active_player.get_player_label() == "defender" else game_data.invader_dice
        self.dices.clear()
        print(f"\n{active_player.get_player_name()} rolling {remaining_dices} dices...\n")
        sleep(1)
        for i in range(remaining_dices):
            self.dices.append(self.roll(self.dice_type))
            print(f"Dice {i + 1}: {self.dices[i].upper()}")

    def dice_roll(self, active_player, remaining_dices=3):
        for i in range(3):
            if i == 2:
                print("\nThis is your last roll, now you have to keep all this dices...")
                self.set_dice_value(remaining_dices, active_player)
                for dice in self.dices:
                    active_player.saved_dices.append(dice)
                break
            else:
                self.set_dice_value(remaining_dices, active_player)
                keep = input("\nDo you want to keep any? ")
                if keep.lower() == "y":
                    remaining_dices = active_player.save_dices(remaining_dices, self.dices)

            if len(active_player.saved_dices) == 3 or remaining_dices == 0:
                break
