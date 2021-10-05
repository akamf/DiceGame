import random

from Player.defender import Defender
from Player.invader import Invader

NUMBER_OF_ROLLS = 3


def dice_roll(dice: list) -> int:
    return dice[random.randrange(0, 6)]


class Game:
    def __init__(self):
        self.invader = Invader("Invader")
        self.defender = Defender("Defender")
        self.active_player = self.defender
        self.dices = []

    def update_active_player(self):
        if self.active_player == self.defender:
            self.defender = self.active_player
            self.active_player = self.invader
        else:
            self.invader = self.active_player
            self.active_player = self.defender

    def set_dices(self):
        self.dices.clear()
        for _ in range(self.active_player.number_of_dices):
            self.dices.append(dice_roll(self.active_player.dice))

    def print_result(self):
        print(f"\nSaved dices for {self.defender.name}:\n")
        for k in self.defender.saved_dices:
            print(k.upper())
        print(f"\nThis results in:\nDefendpoints: {self.defender.defend_points}\nAttackpoints: {self.defender.attack_points}\n")
        print(f"\nSaved dices for {self.invader.name}:\n")
        for k in self.invader.saved_dices:
            print(k.upper())
        print(f"\nThis results in:\nDefendpoints: {self.invader.defend_points}\nAttackpoints: {self.invader.attack_points}\n")

    def print_dices(self):
        print(f"{self.active_player.name} rolling the dices...\n\nThe dices shows the following:")
        for i in range(len(self.dices)):
            print(f"{i + 1}. {self.dices[i]}")

    def dice_result(self):
        for i in range(NUMBER_OF_ROLLS):
            self.set_dices()
            if (i + 1) == NUMBER_OF_ROLLS:
                print("This is your last roll, now you have to keep all this dices...")
                self.print_dices()
                for dice in self.dices:
                    self.active_player.saved_dices.append(dice)
                break
            else:
                self.print_dices()
                keep = input("\nDo you want to keep any? ")

            if keep.lower() == "y":
                num = input("Enter the number(s) of the dices to keep: ")
                for j in num.split():
                    self.active_player.saved_dices.append(self.dices[int(j) - 1])
                self.active_player.number_of_dices -= len(num.split())

            if len(self.active_player.saved_dices) == 3 or self.active_player.number_of_dices == 0:
                break

    def process_saved_dices(self):
        for dice in self.active_player.saved_dices:
            if dice == "shield":
                self.active_player.defend_points += 1
            elif dice == "double shield":
                self.active_player.defend_points += 2
            elif dice == "triple shield":
                self.active_player.defend_points += 3
            elif dice == "sword":
                self.active_player.attack_points += 1
            elif dice == "double sword":
                self.active_player.attack_points += 2
            elif dice == "triple sword":
                self.active_player.attack_points += 3
            elif dice == "draw card":
                pass

    def win(self):
        if self.invader.attack_points > self.defender.defend_points:
            print(f"{self.invader.name} WINS!")
        else:
            print(f"{self.defender.name} WINS!")
