from assets.actors.actor import Actor


class Enemy(Actor):
    def __init__(self):
        super().__init__('skeleton', (0, 0), 3, 0, 5)
        self.level = 1

