import random

from maze.cell import Cell


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

    def get_cell(self, x: int, y: int):
        return self.maze[x][y]

    def write_svg(self, filename):
        """Write an SVG image of the maze to filename."""
        aspect_ratio = self.num_of_cells_x / self.num_of_cells_y
        # Pad the maze all around by this amount.
        padding = 10
        # Height and width of the maze image (excluding padding), in pixels
        height = 500
        width = int(height * aspect_ratio)
        # Scaling factors mapping maze coordinates to image coordinates
        scy, scx = height / self.num_of_cells_y, width / self.num_of_cells_x

        def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
            """Write a single wall to the SVG image file handle f."""
            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'
                  .format(ww_x1, ww_y1, ww_x2, ww_y2), file=ww_f)

        # Write the SVG image file for maze
        with open(filename, 'w') as f:
            # SVG preamble and styles.
            print('<?xml version="1.0" encoding="utf-8"?>', file=f)
            print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
            print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
            print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
                  .format(width + 2 * padding, height + 2 * padding,
                          -padding, -padding, width + 2 * padding, height + 2 * padding),
                  file=f)
            print('<defs>\n<style type="text/css"><![CDATA[', file=f)
            print('line {', file=f)
            print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
            print('    stroke-width: 5;\n}', file=f)
            print(']]></style>\n</defs>', file=f)
            # Draw the "South" and "East" walls of each cell, if present (these
            # are the "North" and "West" walls of a neighbouring cell in
            # general, of course).
            for x in range(self.num_of_cells_x):
                for y in range(self.num_of_cells_y):
                    if self.get_cell(x, y).walls['south']:
                        x1, y1, x2, y2 = x * scx, (y + 1) * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
                    if self.get_cell(x, y).walls['east']:
                        x1, y1, x2, y2 = (x + 1) * scx, y * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
            # Draw the North and West maze border, which won't have been drawn
            # by the procedure above.
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
            print('</svg>', file=f)

    # def __str__(self):
    #     """
    #     For debug only
    #     :return: A string representation of the maze
    #     """
    #     rows = ['-' * self.num_of_cells_x * 2]
    #     for y in range(self.num_of_cells_y):
    #         row = ['|']
    #         for x in range(self.num_of_cells_x):
    #             if self.maze[x][y].walls['east']:
    #                 row.append(' |')
    #             else:
    #                 row.append('  ')
    #         rows.append(''.join(row))
    #         row = ['|']
    #         for x in range(self.num_of_cells_x):
    #             if self.maze[x][y].walls['south']:
    #                 row.append('-+')
    #             else:
    #                 row.append(' +')
    #         rows.append((''.join(row)))
    #     return '\n'.join(rows)

    def get_valid_neighbours(self, cell):
        delta = [
            ('west', (-1, 0)),
            ('east', (1, 0)),
            ('south', (0, 1)),
            ('north', (0, -1))
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

