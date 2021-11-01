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
            if self.current_level % 2 == 0:
                self.maze_size[0] += 2
                self.maze_size[1] += 2
            self.level = Level(self.current_level, self.maze_size, self.player)
            self.level.run()
            self.player.reset_player_stats()
