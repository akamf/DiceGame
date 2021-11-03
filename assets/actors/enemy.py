from assets.actors.actor import Actor


class Enemy(Actor):
    def __init__(self, maze_level: int, **enemy: dict):
        self.__dict__ = enemy
        self.__dict__['level'] += maze_level
        super().__init__(**self.__dict__)

    def __setattr__(self, key, value):
        print(key, value)
        object.__setattr__(self, key, value)
