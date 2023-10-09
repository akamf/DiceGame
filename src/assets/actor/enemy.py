from assets.actor import Actor


class Enemy(Actor):
    def __init__(self, maze_level: int, **enemy: dict) -> None:
        self.__dict__ = enemy

        if 'type' in self.__dict__:
            del self.__dict__['type']

        self.__dict__['position'] = (0, 0)
        self.__dict__['level'] += maze_level
        self.__dict__['attack_points'] += 1 if maze_level % 3 == 0 else 0
        self.__dict__['health_points'] += 1 if maze_level % 2 == 0 else 0

        super().__init__(**self.__dict__)

    def __setattr__(self, key, value) -> None:
        object.__setattr__(self, key, value)
