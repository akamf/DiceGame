import random

from assets import item
from assets.dice import Dice
from game import Game
from maze.map import Maze


def print_debug(game):
    print('X Y')
    print(*game.player.get_player_position())


def main():
    # random.seed(1)
    # print(random.random())
    game = Game()
    game.maze.create_maze()
    game.maze.get_cell(4, 5)
    game.maze.write_svg('maze.svg')
    # # print(game.maze)
    game.print_info()
    print('X Y')
    print(*game.player.get_player_position())
    while True:
        # direction = input('>> ')
        # if not game.maze.get_cell(*game.player.get_player_position()).walls[direction]:
        #     game.player.go(direction)
        #     print('You go further in the maze!\n')
        #     game.print_info()
        # else:
        #     print('You can\'t go there!\n')

        game.process_user_input()
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
