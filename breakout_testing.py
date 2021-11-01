import random
from assets.dice import Dice
from assets.item import Item

from mainfiles.game import Game
from map.cell import Cell
from map.maze import Maze
from data.item_data import key_items, usable_items
from assets.actors.actor import Actor

"""
.py-file to break-out and test functionality, without messing with the main.py-file and/or any classes
"""


def item_generator():
    items = [Item(**item) for item in usable_items]
    return {random.choice(items) for _ in range(3)}


def main():
    new_set = item_generator()
    new_set.update({Item(**item) for item in key_items})

    for i in new_set:
        print(i.__dict__['description'])


if __name__ == '__main__':
    main()
