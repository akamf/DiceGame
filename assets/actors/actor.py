class Actor:
    def __init__(self, name: str, position: tuple, ap: int, dp: int, hp: int):
        self.__name = name
        self.position = ActorPosition(*position)
        self.attack_points = ap
        self.defend_points = dp
        self.health_points = hp

    def set_actor_name(self, name: str):
        self.__name = name

    def get_actor_name(self) -> str:
        return self.__name

    def get_actor_position(self) -> tuple:
        return self.position.x_coord, self.position.y_coord

    # def set_actor_position(self, new_position: tuple):
    #     self.__position.x_coord += new_position.index(0)
    #     self.__position.y_coord += new_position.index(1)


class ActorPosition:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
