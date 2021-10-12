import random

from assets import item
from assets.dice import Dice
from assets.item import Item
from game import Game
from maze.map import Maze


def print_debug(game):
    """
    Debug tool to see the players position
    The maze is dynamic and changes for every run, which makes this very handy!
    """
    print('X Y')
    print(*game.player.get_player_position())


def main():
    # random.seed(1)
    # print(random.random())
    game = Game()
    game.set_up_game()
    game.maze.write_map('maze')
    game.print_info()
    print_debug(game)
    while True:
        game.process_user_input()
        game.maze.get_cell(*game.player.get_player_position())
        game.print_info()
        print_debug(game)
        if game.player.get_player_position() == (4, 4):
            print('WIN!')
            break
    # dice = Dice()
    # dices = dice.roll_dices(3)

    # for i in dices:
    #     print(i)
    # maze = Maze(5, 5)
    # maze.create_maze()
    # print(maze)
    # game.set_up_game()


if __name__ == '__main__':
    main()
