import random

from newfiles.cell import Cell


class Maze:
    def __init__(self, num_of_cells_x, num_of_cells_y, start_cell_x=0, start_cell_y=0):
        """
        :param num_of_cells_x: Number of Cell objects in x
        :param num_of_cells_y: Number of Cell objects in y
        :param start_cell_x: X-coordinate for the staring Cell
        :param start_cell_y: Y-coordinate for the starting Cell
        """
        self.num_of_cells_x, self.num_of_cells_y = num_of_cells_x, num_of_cells_y
        self.start_x, self.start_y = start_cell_x, start_cell_y
        self.maze = [[Cell(x, y) for y in range(num_of_cells_y)] for x in range(num_of_cells_x)]

    def get_cell(self, x, y):
        return self.maze[x][y]

    def __str__(self):
        """
        For debug only
        :return: A string representation of the maze
        """
        rows = ['-' * self.num_of_cells_x * 2]
        for y in range(self.num_of_cells_y):
            row = ['|']
            for x in range(self.num_of_cells_x):
                if self.maze[x][y].walls['E']:
                    row.append(' |')
                else:
                    row.append('  ')
            rows.append(''.join(row))
            row = ['|']
            for x in range(self.num_of_cells_x):
                if self.maze[x][y].walls['S']:
                    row.append('-+')
                else:
                    row.append(' +')
            rows.append((''.join(row)))
        return '\n'.join(rows)

    def get_valid_neighbours(self, cell):
        delta = [
            ('W', (-1, 0)),
            ('E', (1, 0)),
            ('S', (0, 1)),
            ('N', (0, -1))
        ]
        neighbours = []

        for direction, (dx, dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if 0 <= x2 < self.num_of_cells_x and 0 <= y2 < self.num_of_cells_y:
                neighbour = self.get_cell(x2, y2)
                if neighbour.surrounded_by_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def create_maze(self):
        total_cells = self.num_of_cells_x * self.num_of_cells_y
        cell_stack = []
        current_cell = self.get_cell(self.start_x, self.start_y)
        created_cells = 1

        while created_cells < total_cells:
            neighbours = self.get_valid_neighbours(current_cell)

            if not neighbours:
                current_cell = cell_stack.pop()
                continue

            direction, next_cell = random.choice(neighbours)
            current_cell.remove_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            created_cells += 1
