import random
from map.cell import Cell
from map.write_svg import write_map

DIRECTIONS = [
    ('north', (0, -1)),
    ('south', (0, 1)),
    ('east', (1, 0)),
    ('west', (-1, 0))
]


class Maze:
    def __init__(self, num_of_cells_x, num_of_cells_y, items, enemies, start_cell_x=0, start_cell_y=0):
        """
        :param num_of_cells_x: Number of Cell objects in x
        :param num_of_cells_y: Number of Cell objects in y
        :param start_cell_x: X-coordinate for the staring Cell
        :param start_cell_y: Y-coordinate for the starting Cell
        """
        self.num_of_cells_x, self.num_of_cells_y = num_of_cells_x, num_of_cells_y
        self.start_x, self.start_y = start_cell_x, start_cell_y
        self.maze_end = (self.num_of_cells_x - 1, self.num_of_cells_y - 1)

        self.generate_enemies_and_items_locations(items, enemies)
        self.maze = [[Cell(x, y) for y in range(num_of_cells_y)] for x in range(num_of_cells_x)]
        self.create_maze(items, enemies)
        write_map(self, 'maze')

    def get_cell(self, x: int, y: int):
        return self.maze[x][y]

    def get_valid_neighbours(self, cell: Cell):
        """
        Checks the current cells neighbours by decrement or increment it's x and y value
        If the neighbouring cell is inside the map, it appends to the neighbour list
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

    def create_maze(self, items, enemies):
        """
        Function to create the map.
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
            current_cell.set_item(items)
            current_cell.set_enemy(enemies)
            cell_stack.append(current_cell)
            current_cell = next_cell
            created_cells += 1

        current_cell.set_item(items)
        current_cell.set_enemy(enemies)

    def generate_enemies_and_items_locations(self, items: list, enemies: list):
        locations = []
        cnt = 0
        for _ in range(len(enemies) + len(items)):
            (x, y) = (random.randrange(0, self.num_of_cells_x), random.randrange(0, self.num_of_cells_y))
            while (x, y) in locations or (x, y) == self.maze_end or (x, y) == (self.start_x, self.start_y):
                (x, y) = (random.randrange(0, self.num_of_cells_x), random.randrange(0, self.num_of_cells_y))
            locations.append((x, y))

        for enemy in enemies:
            enemy.set_actor_position(locations[cnt])
            enemy.pos = locations[cnt]
            cnt += 1

        for item in items:
            if item.__dict__['label'] == 'door':
                item.position = self.maze_end
            else:
                item.position = locations[cnt]
                cnt += 1
