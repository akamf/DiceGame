from map.level import Level
from assets.actors.player import Player


class Game:
    def __init__(self):
        self.player = Player()
        self.level = None
        self.current_level = 1

    def run(self):
        """Main game method. Sequence of all main methods"""
        while True:
            self.level = Level(self.current_level, self.player)
            self.level.run()
            self.update_level()

    def update_level(self):
        if self.player.alive:
            self.current_level += 1
        else:
            quit()
