import random

import game
from maze.map import Maze


class Item:
    def __init__(self, **item):
        self.__dict__ = item

    def set_item_position(self, maze: Maze):
        for item in self.__dict__:
            item_id = item[0]
            x = random.randrange(0, 5)
            y = random.randrange(0, 5)
            if not Maze.get_cell(maze, x, y):
                Maze.get_cell(maze, x, y).set_item(item_id, (x, y))

