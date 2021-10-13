import random
from assets.actors.actor import Actor


class Enemy(Actor):
    def __init__(self):
        super().__init__(None, (random.randrange(0, 5), random.randrange(0, 5)), )
        self.level = 1
