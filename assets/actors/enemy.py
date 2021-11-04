from assets.actors.actor import Actor


class Enemy(Actor):
    def __init__(self, maze_level: int, **enemy: dict):
        self.__dict__ = enemy
        self.__dict__['level'] += maze_level
        self.__dict__['ap'] += int(maze_level / 2) if maze_level > 1 else 1
        self.__dict__['hp'] *= int(maze_level / 3) if maze_level > 1 else 1
        super().__init__(**self.__dict__)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
