import random
from assets.actors.actor import Actor


class Enemy(Actor):
    def __init__(self):
        super().__init__('skeleton', (0, 4), 3, 0, 5)
        self.level = 1
        self.enemies = []

    def set_enemy_locations(self, locations: list):
        for i in self.enemies:
            self.enemies[i].set_actor_postion(locations[i])

    def generate_enemy_locations(self) -> list:
        locations = []

        for _ in range(len(self.enemies)):
            (x, y) = (random.randrange(0, 5), random.randrange(0, 5))
            while True:
                if not (x, y) in locations:
                    break
                (x, y) = (random.randrange(0, 5), random.randrange(0, 5))
            locations.append((x, y))

        return locations
