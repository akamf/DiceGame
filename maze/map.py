import random
from maze.cell import Cell

DIRECTIONS = [
    ('north', (0, -1)),
    ('south', (0, 1)),
    ('east', (1, 0)),
    ('west', (-1, 0))
]


class Maze:
    def __init__(self, num_of_cells_x, num_of_cells_y, items, start_cell_x=0, start_cell_y=0):
        """
        :param num_of_cells_x: Number of Cell objects in x
        :param num_of_cells_y: Number of Cell objects in y
        :param start_cell_x: X-coordinate for the staring Cell
        :param start_cell_y: Y-coordinate for the starting Cell
        """
        self.num_of_cells_x, self.num_of_cells_y = num_of_cells_x, num_of_cells_y
        self.start_x, self.start_y = start_cell_x, start_cell_y
        self.game_items = items
        self.maze = [[Cell(x, y) for y in range(num_of_cells_y)] for x in range(num_of_cells_x)]
        self.create_maze()
        self.write_map('maze')

    def get_cell(self, x: int, y: int):
        return self.maze[x][y]

    def get_valid_neighbours(self, cell: Cell):
        """
        Checks the current cells neighbours by decrement or increment it's x and y value
        If the neighbouring cell is inside the maze, it appends to the neighbour list
        :param cell: Current cell
        :return: A list of all valid neighbours
        """
        neighbours = []

        for direction, (direction_x, direction_y) in DIRECTIONS:
            neighbour_x, neighbour_y = cell.x + direction_x, cell.y + direction_y
            if 0 <= neighbour_x < self.num_of_cells_x and 0 <= neighbour_y < self.num_of_cells_y:
                neighbour = self.get_cell(neighbour_x, neighbour_y)
                if neighbour.surrounded_by_walls():
                    neighbours.append((direction, neighbour))

        return neighbours

    def create_maze(self):
        """
        Function to create the maze.
        The function checks the neighbouring cells and moves in random direction by removing the wall
        between the current and the next cell.
        If the neighbouring cell is a dead end, it backtrack to the last "unvisited" neighbouring cell
        """
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
            current_cell.set_item(self.game_items)
            cell_stack.append(current_cell)
            current_cell = next_cell
            created_cells += 1
        current_cell.set_item(self.game_items)

    def write_map(self, file_name: str):
        """
        Write an map, as an SVG (Scalable Vector Graphics) image, of the maze
        For debugging
        :param file_name: The file name for the output file
        """
        def write_wall(wall_f, wall_x1, wall_y1, wall_x2, wall_y2):
            """
            Write a single wall to the SVG image
            """
            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'
                  .format(wall_x1, wall_y1, wall_x2, wall_y2), file=wall_f)

        aspect_ratio = self.num_of_cells_x / self.num_of_cells_y
        padding = 10
        height = 500
        width = int(height * aspect_ratio)  # Height and width of the maze image in pixels
        scale_y, scale_x = height / self.num_of_cells_y, width / self.num_of_cells_x  # Scaling the maze coordinates

        with open(file_name + '.svg', 'w') as f:
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
            # Draw the "South" and "East" walls of each cell,
            # these are the "North" and "West" walls of the neighbouring cell
            for x in range(self.num_of_cells_x):
                for y in range(self.num_of_cells_y):
                    if self.get_cell(x, y).walls['south']:
                        x1, y1, x2, y2 = x * scale_x, (y + 1) * scale_y, (x + 1) * scale_x, (y + 1) * scale_y
                        write_wall(f, x1, y1, x2, y2)
                    if self.get_cell(x, y).walls['east']:
                        x1, y1, x2, y2 = (x + 1) * scale_x, y * scale_y, (x + 1) * scale_x, (y + 1) * scale_y
                        write_wall(f, x1, y1, x2, y2)
            # Draw the North and West maze border
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
            print('</svg>', file=f)
