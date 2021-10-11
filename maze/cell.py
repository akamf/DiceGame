class Cell:
    # Directions where a wall separates the cells. A wall to the north in one cell is to the south for next cell etc.
    wall_pairs = {
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

    def surrounded_by_walls(self):
        return all(self.walls.values())

    def remove_wall(self, other_cell, wall):
        self.walls[wall] = False
        other_cell.walls[Cell.wall_pairs[wall]] = False
