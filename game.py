from time import sleep
from Player.defender import Defender
from Player.invader import Invader
from Player.player import Player
from dice import Dice


class Game:
    def __init__(self):
        self.dice = Dice()
        self.player1 = None
        self.player2 = None
        self.active_player = None
        self.dices = []

    def run(self):
        self.set_up_game()
        self.dice.dice_roll(self.active_player)
        self.update_active_player()
        self.dice.dice_roll(self.active_player)
        self.process_saved_dices(self.player1 if self.player1.get_player_label() == "invader" else self.player2,
                                 self.player2 if self.player2.get_player_label() == "defender" else self.player1)
        self.print_result()
        self.win()

    def set_up_game(self):
        self.player1.set_player_name(input("Enter your name, Player One: "))
        self.player2.set_player_name(input("Enter your name, Player Two: "))
        print(f"Let's see who shall select your roles in the game. {self.player1.get_player_name()} roll please. ")
        while True:
            x = self.dice.roll([1, 2, 3, 4, 5, 6])
            print(f"A {x}!\n{self.player2.get_player_name()}, you're up!")
            y = self.dice.roll([1, 2, 3, 4, 5, 6])
            if x > y:
                print(f"A {y}, that means {self.player1.get_player_name()} will choose your roles.")
                self.active_player = self.player1
                break
            elif x < y:
                print(f"A {y}, that means {self.player2.get_player_name()} will choose your roles.")
                self.active_player = self.player2
                break
            else:
                print(f"Tie!{self.player1.get_player_name()} roll again.")
        self.set_player_role(self.player1.get_player_name(), self.player2.get_player_name())

    def set_player_role(self, player1: str, player2: str):
        """
        Set which part in the game player one and player will have
        :param role: Input from the active player, what role they want to play as
        :param player1: Name of Player One
        :param player2: Name of Player Two
        :return:
        """
        role = input(f"{self.active_player.get_player_name()}, type 'invader' if you want to invade the castle or 'defender' if you want to defend: ")
        if self.active_player == self.player1:
            match role.lower():
                case "invader":
                    self.player1 = Invader(player1)
                    self.player2 = Defender(player2)
                    self.active_player = self.player2
                case "defender":
                    self.player1 = Defender(player1)
                    self.player2 = Invader(player2)
        else:
            match role.upper():
                case "invader":
                    self.player1 = Defender(player1)
                    self.player2 = Invader(player2)
                    self.active_player = self.player2
                case "defender":
                    self.player1 = Invader(player1)
                    self.player2 = Defender(player2)

    def update_active_player(self):
        self.active_player = self.player2 if self.active_player == self.player1 else self.player1

    def print_result(self):
        print("\nPRINTING RESULTS...\n")
        sleep(2)
        print(f"Saved dices for {self.player1.get_player_name()}:\n")
        for i in self.player1.saved_dices:
            print(i.upper())
        print(f"\nThis results in:\nDefendpoints: {self.player1.defend_points}\nAttackpoints: {self.player1.attack_points}\n")
        print(f"\nSaved dices for {self.player2.get_player_name()}:\n")
        for j in self.player2.saved_dices:
            print(j.upper())
        print(f"\nThis results in:\nDefendpoints: {self.player2.defend_points}\nAttackpoints: {self.player2.attack_points}\n")

    @staticmethod
    def process_saved_dices(invader: Invader, defender: Defender):
        for dice in invader.saved_dices:
            match dice:
                case "shield":
                    invader.defend_points += 1
                case "double shield":
                    invader.defend_points += 2
                case "sword":
                    invader.attack_points += 1
                case "double sword":
                    invader.attack_points += 2
                case "triple sword":
                    invader.attack_points += 3
                case "draw card":
                    invader.number_of_cards += 1

        for dice in defender.saved_dices:
            match dice:
                case "shield":
                    defender.defend_points += 1
                case "double shield":
                    defender.defend_points += 2
                case "triple shield":
                    defender.defend_points += 3
                case "sword":
                    defender.attack_points += 1
                case "double sword":
                    defender.attack_points += 2

    # def process_saved_cards(self):
    #     self.invader.draw_cards()
    #     for card in self.invader.cards:
    #         sleep(1)
    #         print(f"You draw the {card.upper()} card!\nIt has the following effect:\n")
    #         match card:
    #             case "battering ram":
    #                 print(f"{self.invader.name}'s army successfully get their battering ram to the front gate!\n"
    #                       f"5 is added to {self.invader.name}'s attackpoints.")
    #                 self.invader.attack_points += 5
    #             case "fortified wall":
    #                 print(f"{self.defender.name} barricades the front gate!\n5 is added to {self.defender.name}'s defendpoints.")
    #                 self.defender.defend_points += 5
    #             case "the plague":
    #                 print("A plague ravage the battlefield and obliterates a large part of the armies!\n"
    #                       "Both players loses their points and needs to re-roll with only TWO dices each!\n"
    #                       f"{self.defender.name} will start!")
    #                 self.clear_player_stats()
    #                 self.active_player = self.defender
    #                 self.dice.dice_result(2)
    #                 self.update_active_player()
    #                 self.dice.dice_result(2)
    #                 self.process_saved_dices()
    #             case "reinforcement":
    #                 print(f"A nearby village joins {self.invader.name}'s army!\n{self.invader.name} doubles their attackpoints.")
    #                 self.invader.attack_points *= 2
    #             case "the spy":
    #                 print("A spy finds a weakness in the wall!")
    #                 while True:
    #                     x = input(f"{self.invader.name}, choose if your the defender will re-roll their dices "
    #                               "(I for invader or D for defender): ")
    #                     if x.upper() == "I":
    #                         self.invader.saved_dices.clear()
    #                         self.dice_result()
    #                         break
    #                     elif x.upper() == "D":
    #                         self.update_active_player()
    #                         self.defender.saved_dices.clear()
    #                         self.dice_result()
    #                         break
    #                 self.process_saved_dices()

    def win(self):
        if self.player1.attack_points > self.player2.defend_points:
            print(f"{self.player1.get_player_name()} WINS!")
        else:
            print(f"{self.player2.get_player_name()} WINS!")

    def clear_player_stats(self):
        self.player1.saved_dices.clear()
        self.player1.attack_points = 0
        self.player1.defend_points = 0
        self.player2.saved_dices.clear()
        self.player2.attack_points = 0
        self.player2.defend_points = 0


