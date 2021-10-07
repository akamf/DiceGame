class Player:
    def __init__(self, name):
        self.name = name
        self.number_of_dices = 3
        self.saved_dices = []
        self.attack_points = 0
        self.defend_points = 0
        self.computer_player = False

    def set_player_name(self):
        self.name = input("Enter your name: ")
