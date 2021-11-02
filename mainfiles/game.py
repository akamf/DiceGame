from map.level import Level
from assets.actors.player import Player


class Game:
    def __init__(self):
        self.player = Player()
        self.level = None
        self.current_level = 0
        self.maze_size = (5, 5)

    def run(self):
        while self.player.alive:
            self.current_level += 1
            self.maze_size = self.update_maze_size()
            self.level = Level(self.current_level, self.maze_size, self.player)
            self.level.run_level()
            self.player.reset_player_stats()

    def update_maze_size(self) -> tuple:
        if self.current_level % 5 == 0:
            return self.maze_size[0] + 2, self.maze_size[1] + 2
        return self.maze_size
