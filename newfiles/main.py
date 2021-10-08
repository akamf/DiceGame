from newfiles.dice import Dice
from newfiles.maze import Maze


def main():
    # dice = Dice()
    # dices = dice.roll_dices(3)
    #
    # for i in dices:
    #     print(i)
    maze = Maze(5, 5)
    maze.create_maze()
    print(maze)


if __name__ == '__main__':
    main()
