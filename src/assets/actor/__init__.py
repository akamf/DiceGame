from abc import ABC


class Actor(ABC):
    def __init__(self, name: str, pos: tuple, attack_points: int, defend_points: int, health_points: int, level: int):
        self.__name = name
        self.__position = ActorPosition(*pos)
        self.attack_points = attack_points
        self.defend_points = defend_points
        self.health_points = health_points
        self.level = level

    def set_actor_name(self, name: str):
        self.__name = name

    def get_actor_name(self) -> str:
        return self.__name

    def set_actor_position(self, new_position: tuple):
        if new_position == (0, 0):
            self.__position = ActorPosition(0, 0)
        else:
            self.__position.x_coord += new_position[0]
            self.__position.y_coord += new_position[1]

    def get_actor_position(self) -> tuple:
        return self.__position.x_coord, self.__position.y_coord


class ActorPosition:
    def __init__(self, x: int, y: int):
        self.x_coord = x
        self.y_coord = y