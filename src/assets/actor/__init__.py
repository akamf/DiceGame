from abc import ABC


class Actor(ABC):
    """Base class for Player and Enemy"""
    def __init__(self, name: str, position: tuple, attack_points: int, defend_points: int, health_points: int, level: int) -> None:
        self.__name = name
        self.__position = ActorPosition(*position)
        self.attack_points = attack_points
        self.defend_points = defend_points
        self.health_points = health_points
        self.level = level

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def position(self) -> tuple:
        return self.__position.x_coord, self.__position.y_coord

    @position.setter
    def position(self, new_position: tuple) -> None:
        if new_position == (0, 0):
            self.__position = ActorPosition(0, 0)
        else:
            self.__position.x_coord += new_position[0]
            self.__position.y_coord += new_position[1]


class ActorPosition:
    def __init__(self, x: int, y: int) -> None:
        self.x_coord = x
        self.y_coord = y
