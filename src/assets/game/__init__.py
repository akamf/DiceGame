from assets.actor.player import Player
from assets.game.level import GameLevel


class Game:
    def __init__(self) -> None:
        self.player = Player()
        self.game_level = None
        self.difficulty_level = 0

    def run(self) -> None:
        while self.player.alive:
            self.difficulty_level += 1
            self.game_level = GameLevel(self.difficulty_level, self.player)
            self.game_level.run()
            self.player.update_stats()
