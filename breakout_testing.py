import random
from assets.dice import Dice
from assets.item import Item
from mainfiles.game import Game
from maze.cell import Cell
from maze.map import Maze
from data.item_data import usable_items
from assets.actors.actor import Actor

"""
.py-file to break-out and test functionality, without messing with the main.py-file and/or any classes
"""


def main():
    item = Item()
    print()
    for item in usable_items:
        print(item['name'], *item['position'])


if __name__ == '__main__':
    main()
