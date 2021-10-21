from assets.actors.actor import Actor


class Enemy(Actor):
    def __init__(self):
        self.level = 1
        super().__init__('skeleton', (0, 0), 3 + self.level, 0, 5)

