class Player:
    def __init__(self):
        self.__name = None
        self.attack_points = 0
        self.defend_points = 0
        self.health_points = 10
        self.position = PlayerPosition(0, 0)

    def set_player_name(self, name: str):
        self.__name = name

    def get_player_name(self) -> str:
        return self.__name


class PlayerPosition:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
