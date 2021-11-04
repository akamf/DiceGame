from assets.actors.player import Player
from data.high_score import HighScoreBoard
from mainfiles.level import Level


class Game:
    def __init__(self):
        self.player = Player()
        self.level = None
        self.current_level = 0
        self.maze_size = (5, 5)
        self.high_score_board = None

    def run(self):
        while self.player.alive:
            self.current_level += 1
            self.maze_size = self.update_maze_size()
            self.level = Level(self.current_level, self.maze_size, self.player)
            self.level.run_level()
            self.player.update_player_stats()
        # self.check_high_score()

    def update_maze_size(self) -> tuple:
        if self.current_level % 5 == 0:
            return self.maze_size[0] + 2, self.maze_size[1] + 2
        return self.maze_size

    def check_high_score(self):
        self.high_score_board = HighScoreBoard()
        self.high_score_board.load_high_score()
        self.high_score_board.update_high_score(input('Enter your name to save your score:\n>> '), self.player.score)
        self.high_score_board.save_high_score()
