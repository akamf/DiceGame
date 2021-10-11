class Player:
    def __init__(self):
        self.__name = None
        self.__position = PlayerPosition(0, 0)
        self.inventory = []
        self.attack_points = 0
        self.defend_points = 0
        self.health_points = 10

    def set_player_name(self, name: str):
        self.__name = name

    def get_player_name(self) -> str:
        return self.__name

    def get_player_position(self) -> tuple:
        return self.__position.x_coord, self.__position.y_coord

    def go(self, direction: str):
        """
        Moves the player between the mazes cells
        :param direction: The direction to move
        """
        match direction:
            case 'north':
                self.__position.y_coord -= 1
            case 'south':
                self.__position.y_coord += 1
            case 'east':
                self.__position.x_coord += 1
            case 'west':
                self.__position.x_coord -= 1


class PlayerPosition:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
