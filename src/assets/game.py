from src.assets.actor.player import Player
from src.assets.high_score import HighScoreBoard
from src.assets.level import Level


class Game:
    def __init__(self) -> None:
        self.player = Player()
        self.level = None
        self.current_level = 0
        self.__maze_size = (5, 5)
        self.high_score_board = None

    @property
    def maze_size(self) -> tuple:
        if self.current_level % 5 == 0:
            return self.__maze_size[0] + 2, self.__maze_size[1] + 2
        return self.__maze_size

    @maze_size.setter
    def maze_size(self, s: tuple) -> None:
        if self.current_level % 5 == 0:
            self.__maze_size = (s[0] + 2, s[1] + 2)
        else:
            self.__maze_size = s

    def run(self) -> None:
        while self.player.alive:
            self.current_level += 1
            self.maze_size = self.maze_size
            self.level = Level(self.current_level, self.maze_size, self.player)
            self.level.run_level()
            self.player.update_stats()

    def check_high_score(self) -> None:
        self.high_score_board = HighScoreBoard()
        self.high_score_board.load_high_score()
        self.high_score_board.update_high_score(input('Enter your name to save your score:\n>> '), self.player.score)
        self.high_score_board.save_high_score()
