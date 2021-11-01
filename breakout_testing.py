import random
from assets.dice import Dice

from mainfiles.game import Game
from map.cell import Cell
from map.maze import Maze
from data.item_data import environment_items
from assets.actors.actor import Actor

"""
.py-file to break-out and test functionality, without messing with the main.py-file and/or any classes
"""


def open_chest(chest: dict):
    print(f'The {chest["label"]} contains: {chest["contains"]}')


def chest(game):
    if game.maze.get_cell(game.player.get_actor_position()).got_item() \
            and game.maze.get_cell(game.player.get_actor_position()).item['label'] == 'chest':
        command = input('What to do: ')

        if command == 'open':
            open_chest(game.maze.get_cell(game.player.get_actor_position()).item)


def main():
    self.equipment = Equipment()
    if item_name == i.name and i.equippable:
        match i.slot:
            case 'hands':
                self.equipment.hands.equip(item)


if __name__ == '__main__':
    main()
