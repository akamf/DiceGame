class Player:
    def __init__(self, name: str, label: str):
        self.__name = name
        self.__label = label
        self.number_of_dices = 3
        self.saved_dices = []
        self.attack_points = 0
        self.defend_points = 0
        # self.computer_player = False

    def set_player_name(self, name: str):
        self.__name = name

    def get_player_name(self) -> str:
        return self.__name

    def get_player_label(self) -> str:
        return self.__label

    def save_dices(self, remaining_dices: int, dices: list) -> int:
        num = input("Enter the number(s) of the dices to keep: ")
        for i in num.split():
            self.saved_dices.append(dices[int(i) - 1])
        return remaining_dices - len(num.split())
