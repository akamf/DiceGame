class Actor:
    def __init__(self, name: str, pos: tuple, ap: int, dp: int, hp: int, level: int):
        self.__name = name
        self.__position = ActorPosition(*pos)
        self.attack_points = ap
        self.defend_points = dp
        self.health_points = hp
        self.level = level

    def set_actor_name(self, name: str):
        self.__name = name

    def get_actor_name(self) -> str:
        return self.__name

    def set_actor_position(self, new_position: tuple):
        self.__position.x_coord += new_position[0]
        self.__position.y_coord += new_position[1]

    def get_actor_position(self) -> tuple:
        return self.__position.x_coord, self.__position.y_coord


class ActorPosition:
    def __init__(self, x: int, y: int):
        self.x_coord = x
        self.y_coord = y
