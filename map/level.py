import random

from assets.actors.enemy import Enemy
from assets.item import Item
from data.enemy_data import enemies
from data.item_data import environment_items, key_items, weapons_and_armors
from map.maze import Maze

START = (0, 0)
GOAL = (4, 4)


class Level:
    def __init__(self, level: int):
        self.level = level
        self.enemies = [Enemy(self.level, **enemy) for enemy in enemies]
        self.generate_enemy_locations()
        self.items = {Item(**random.choice(key_items + weapons_and_armors)) for _ in range(GOAL[0])}
        self.set_items_positions()
        self.items.update([Item(**item) for item in environment_items])
        self.maze = Maze(*(GOAL[0] + 1, GOAL[1] + 1), self.items, self.enemies)

