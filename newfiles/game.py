from newfiles.dice import Dice
from newfiles.maze import Maze
from newfiles.player import Player


class Game:
    def __init__(self):
        self.player = Player()
        self.maze = Maze(5, 5)
        self.dice = Dice()

    def run(self):
        pass

    def set_up_game(self):
        self.maze.create_maze()
        self.player.set_player_name(input("Please enter your name: "))

