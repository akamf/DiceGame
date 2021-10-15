import random
from assets.dice import Dice
from assets.items import Items
from mainfiles.game import Game
from maze.cell import Cell
from maze.map import Maze
from data.item_data import usable_items
from assets.actors.actor import Actor

"""
.py-file to break-out and test functionality, without messing with the main.py-file and/or any classes
"""


def main():
    inventory = []

    # def print_chest():
    #     ids = []
    #     for item in usable_items:
    #         if item['container']:
    #             for i in item['contains']:
    #                 ids.append(i)
    #     for item in usable_items:
    #         for id in ids:
    #             if item['id'] == id:
    #                 print(f'* {item["name"]}')
    #
    # def open_chest():
    #     chest_open = True
    #     while chest_open:
    #         print_chest()
    #         pick = input("What do you want pick up:")
    #
    #         if pick == 'none':
    #             chest_open = False
    #         else:
    #             for item in usable_items:
    #                 if item['name'] == pick:
    #                     pick = item['id']
    #
    #             for item in usable_items:
    #                 if item['container']:
    #                     for id in item['contains']:
    #                         if id == pick:
    #                             item['contains'].remove(id)
    #                             inventory.append(id)
    #                             if len(item['contains']) == 0:
    #                                 item['visible'] = False
    #                                 chest_open = False
    #                                 print('It\'s gone!')
    #

if __name__ == '__main__':
    main()
