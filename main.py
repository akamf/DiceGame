from assets.dice import Dice
from game import Game
from maze.map import Maze


def main():
    game = Game()
    dice = Dice()
    dices = dice.roll_dices(3)

    for i in dices:
        print(i)
    maze = Maze(5, 5)
    maze.create_maze()
    print(maze)
    game.set_up_game()


if __name__ == '__main__':
    main()
