import random

from assets.actors.actor import Actor


class Enemy(Actor):
    def __init__(self):
        self.level = 1
        super().__init__('skeleton', (0, 0), 3 + self.level, 0, 5)

    @staticmethod
    def generate_enemy_locations(enemies: list):
        locations = []

        for _ in range(len(enemies)):
            (x, y) = (random.randrange(0, 5), random.randrange(0, 5))
            while True:
                if not (x, y) in locations and (x, y) != (4, 4):
                    break
                (x, y) = (random.randrange(0, 5), random.randrange(0, 5))
            locations.append((x, y))

        for i in range(len(enemies)):
            enemies[i].set_actor_position(locations[i])
