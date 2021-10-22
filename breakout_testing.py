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
    # game = Game()
    #
    # game.run()
    def method():
        return 1, 2, 3, 4, 5, 6

    a, b = method()[2:None:3]
    c, d = method()[2::3]
    print(method())
    print(a, b)
    print(c, d)


if __name__ == '__main__':
    main()
