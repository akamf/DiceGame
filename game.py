import random
import game_data

from time import sleep
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

    def run(self):
        pass

    def update_active_player(self):
        if self.active_player == self.defender:
            self.defender = self.active_player
            self.active_player = self.invader
        else:
            self.invader = self.active_player
            self.active_player = self.defender

    def set_dices(self, remaining_dices: int):
        dice = game_data.defender_dice if self.active_player == self.defender else game_data.invader_dice
        self.dices.clear()
        print(f"\n{self.active_player.name} rolling {remaining_dices} dices...\n")
        sleep(1)
        for i in range(remaining_dices):
            self.dices.append(dice_roll(dice))
            print(f"Dice {i + 1}: {self.dices[i].upper()}")

    def print_result(self):
        print("\nPRINTING RESULTS...\n")
        sleep(2)
        print(f"Saved dices for {self.defender.name}:\n")
        for i in self.defender.saved_dices:
            print(i.upper())
        print(f"\nThis results in:\nDefendpoints: {self.defender.defend_points}\nAttackpoints: {self.defender.attack_points}\n")
        print(f"\nSaved dices for {self.invader.name}:\n")
        for j in self.invader.saved_dices:
            print(j.upper())
        print(f"\nThis results in:\nDefendpoints: {self.invader.defend_points}\nAttackpoints: {self.invader.attack_points}\n")

    def dice_result(self, remaining_dices=3):
        for i in range(NUMBER_OF_ROLLS):
            if (i + 1) == NUMBER_OF_ROLLS:
                print("\nThis is your last roll, now you have to keep all this dices...")
                self.set_dices(remaining_dices)
                for dice in self.dices:
                    self.active_player.saved_dices.append(dice)
                break
            else:
                self.set_dices(remaining_dices)
                keep = input("\nDo you want to keep any? ")
                if keep.lower() == "y":
                    remaining_dices = self.save_dices(remaining_dices)

            if len(self.active_player.saved_dices) == 3 or remaining_dices == 0:
                break

    def save_dices(self, remaining_dices: int) -> int:
        num = input("Enter the number(s) of the dices to keep: ")
        for i in num.split():
            self.active_player.saved_dices.append(self.dices[int(i) - 1])
        return remaining_dices - len(num.split())

    def process_saved_dices(self):
        for dice in self.invader.saved_dices:
            match dice:
                case "shield":
                    self.invader.defend_points += 1
                case "double shield":
                    self.invader.defend_points += 2
                case "sword":
                    self.invader.attack_points += 1
                case "double sword":
                    self.invader.attack_points += 2
                case "triple sword":
                    self.invader.attack_points += 3
                case "draw card":
                    self.invader.number_of_cards += 1

        for dice in self.defender.saved_dices:
            match dice:
                case "shield":
                    self.defender.defend_points += 1
                case "double shield":
                    self.defender.defend_points += 2
                case "triple shield":
                    self.defender.defend_points += 3
                case "sword":
                    self.defender.attack_points += 1
                case "double sword":
                    self.defender.attack_points += 2

    def process_saved_cards(self):
        self.invader.draw_cards()
        for card in self.invader.cards:
            sleep(1)
            print(f"You draw the {card.upper()} card!\nIt has the following effect:\n")
            match card:
                case "battering ram":
                    print(f"{self.invader.name}'s army successfully get their battering ram to the front gate!\n"
                          f"5 is added to {self.invader.name}'s attackpoints.")
                    self.invader.attack_points += 5
                case "fortified wall":
                    print(f"{self.defender.name} barricades the front gate!\n5 is added to {self.defender.name}'s defendpoints.")
                    self.defender.defend_points += 5
                case "the plague":
                    print("A plague ravage the battlefield and obliterates a large part of the armies!\n"
                          "Both players loses their points and needs to re-roll with only TWO dices each!\n"
                          f"{self.defender.name} will start!")
                    self.clear_player_stats()
                    self.active_player = self.defender
                    self.dice_result(2)
                    self.update_active_player()
                    self.dice_result(2)
                    self.process_saved_dices()
                case "reinforcement":
                    print(f"A nearby village joins {self.invader.name}'s army!\n{self.invader.name} doubles their attackpoints.")
                    self.invader.attack_points *= 2
                case "the spy":
                    print("A spy finds a weakness in the wall!")
                    while True:
                        x = input(f"{self.invader.name}, choose if your the defender will re-roll their dices "
                                  "(I for invader or D for defender): ")
                        if x.upper() == "I":
                            self.invader.saved_dices.clear()
                            self.dice_result()
                            break
                        elif x.upper() == "D":
                            self.update_active_player()
                            self.defender.saved_dices.clear()
                            self.dice_result()
                            break
                    self.process_saved_dices()

    def win(self):
        if self.invader.attack_points > self.defender.defend_points:
            print(f"{self.invader.name} WINS!")
        else:
            print(f"{self.defender.name} WINS!")

    def clear_player_stats(self):
        self.invader.saved_dices.clear()
        self.invader.attack_points = 0
        self.invader.defend_points = 0
        self.defender.saved_dices.clear()
        self.defender.attack_points = 0
        self.defender.defend_points = 0
