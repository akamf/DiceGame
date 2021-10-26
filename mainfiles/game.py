from map.level import Level
from assets.actors.player import Player


class Game:
    def __init__(self):
        self.player = Player()
        self.level = None
        self.current_level = 0

    def run(self):
        while self.player.alive:
            self.current_level += 1
            self.level = Level(self.current_level, self.player)
            self.level.run()
