import random
from assets.dice import Dice
from assets.items import Item
from mainfiles.game import Game
from maze.cell import Cell
from maze.map import Maze
from data.item_data import usable_items
from assets.actors.actor import Actor

"""
.py-file to break-out and test functionality, without messing with the main.py-file and/or any classes
"""


# def get_item(item_name, current_cell, player):
#     found_item = None
#     for item in current_cell.item:
#         if item.name == item_name:
#             found_item = item
#             break
#     if found_item:
#         if 'get' in found_item.actions:
#             print(f'You pick up the {item_name}!')
#             current_cell.item = None
#             current_cell.got_item = False
#             player.inventory.append(found_item)
#
#
# def drop_item(item, current_cell):
#     found_item = None
#     for item in current_cell.item:
#         if item.name == item_name:
#             found_item = item
#             break
#     if found_item:
#         if 'get' in found_item.actions:
#             print(f'You pick up the {item_name}!')
#             current_cell.item = None
#             current_cell.got_item = False
#             player.inventory.append(found_item)


def main():
    item = Item()
    print()
    for item in usable_items:
        print(item['name'], *item['position'])


if __name__ == '__main__':
    main()
