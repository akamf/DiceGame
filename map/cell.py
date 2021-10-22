class Cell:

    WALL_SEPARATES = {
        'north': 'south',
        'south': 'north',
        'east': 'west',
        'west': 'east'
    }

    def __init__(self, x, y):
        """:param x: Cell X-coordinate  :param y: Cell Y-coordinate"""
        self.x, self.y = x, y
        self.walls = {
            'north': True,
            'south': True,
            'east': True,
            'west': True
        }
        self.got_item = False
        self.item = None
        self.enemy = None

    def surrounded_by_walls(self) -> bool:
        return all(self.walls.values())

    def remove_wall(self, other_cell, wall):
        """
        Remove the wall between two cells
        :param other_cell: The wall between this cell and self will be removed
        :param wall: The wall direction to remove
        """
        self.walls[wall] = False
        other_cell.walls[Cell.WALL_SEPARATES[wall]] = False

    def set_item(self, items: list):
        """Set item to the cell with the same position"""
        for item in items:
            if item.__dict__['position'] == (self.x, self.y):
                self.item = item
                self.got_item = True

    def set_enemy(self, enemies: list):
        """Set enemy to the cell with the same position"""
        for enemy in enemies:
            if enemy.__dict__['pos'] == (self.x, self.y):
                self.enemy = enemy
