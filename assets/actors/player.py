from assets.actors.actor import Actor

DIRECTIONS = {
    'north': (0, -1),
    'south': (0, 1),
    'east': (1, 0),
    'west': (-1, 0)
}


class Player(Actor):
    def __init__(self):
        super().__init__('', (0, 0), 0, 0, 10)
        self.inventory = []
        self.in_battle = False

    def got_item(self, item: str) -> bool:
        """
        Search player inventory for a certain item
        :param item: The item to search for
        :return: True if the item is found, else False
        """
        if item in self.inventory:
            match item:
                case 'lantern':
                    return True
                case 'two-handed sword':
                    return True
                case 'old wooden shield':
                    return True
                case 'golden key':
                    return True
        return False

    def go(self, direction: str):
        self.position.x_coord += DIRECTIONS[direction][0]
        self.position.y_coord += DIRECTIONS[direction][1]
