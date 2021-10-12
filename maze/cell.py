import random
import game
from data.item_data import usable_items


class Cell:
    # Directions where a wall separates the cells. A wall to the north in one cell is to the south for next cell etc.
    wall_pairs = {
        'north': 'south',
        'south': 'north',
        'east': 'west',
        'west': 'east'
    }

    def __init__(self, x, y):
        """:param x: Cell X-coordinate  :param y: Cell Y-coordinate"""
        self.x, self.y = x, y
        self.walls = {
            'north': True,
            'south': True,
            'east': True,
            'west': True
        }
        self.got_item = False
        self.item = {}

    def surrounded_by_walls(self):
        return all(self.walls.values())

    def remove_wall(self, other_cell, wall):
        self.walls[wall] = False
        other_cell.walls[Cell.wall_pairs[wall]] = False

    def set_item(self, item_id: int, position: tuple):
        if position == (self.x, self.y):
            for item in usable_items:
                if item['id'] == item_id:
                    self.item = item

    # def set_item_position(self):
    #     for item in usable_items:
    #         x, y = random.randrange(0, 4), random.randrange(0, 4)
    #         while game.maze.get_cell(x, y).got_item:
    #             x, y = random.randrange(0, 4), random.randrange(0, 4)
    #         item['maze position'] = (x, y)
    #