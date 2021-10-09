class Cell:
    # Directions where a wall separates the cells. A wall to the north in one cell is to the south for next cell etc.
    wall_pairs = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E'
    }

    def __init__(self, x, y):
        """:param x: Cell X-coordinate  :param y: Cell Y-coordinate"""
        self.x, self.y = x, y
        self.walls = {
            'N': True,
            'S': True,
            'E': True,
            'W': True,
        }

    def surrounded_by_walls(self):
        return all(self.walls.values())

    def remove_wall(self, other_cell, wall):
        self.walls[wall] = False
        other_cell.walls[wall] = False
