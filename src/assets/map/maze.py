import random
from src.assets.map import write_map

DIRECTIONS = [
    ('north', (0, -1)),
    ('south', (0, 1)),
    ('east', (1, 0)),
    ('west', (-1, 0))
]
WALL_SEPARATES = {
    'north': 'south',
    'south': 'north',
    'east': 'west',
    'west': 'east'
}


class Cell:
    def __init__(self, x, y):
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

    def remove_wall(self, other_cell, wall: str):
        """
        Method to remove the wall between two cells
        :param other_cell: Cell instance
        :param wall: str, the wall-direction to remove
        return: None
        """
        self.walls[wall] = False
        other_cell.walls[WALL_SEPARATES[wall]] = False

    def set_item(self, items: list):
        """
        Set item to the cell with the same position
        :param items: list, list of maze items
        :return: None
        """
        for item in items:
            if item.__dict__['position'] == (self.x, self.y):
                self.item = item
                self.got_item = True

    def set_enemy(self, enemies: list):
        """
        Set enemy to the cell with the same position
        :param enemies: list, list of enemies for current maze
        :return: None
        """
        for enemy in enemies:
            if enemy.__dict__['pos'] == (self.x, self.y):
                self.enemy = enemy


class Maze:
    def __init__(self, num_of_cells_x, num_of_cells_y, items, enemies, start_cell_x=0, start_cell_y=0):
        self.num_of_cells_x, self.num_of_cells_y = num_of_cells_x, num_of_cells_y
        self.start_x, self.start_y = start_cell_x, start_cell_y
        self.maze_end = (self.num_of_cells_x - 1, self.num_of_cells_y - 1)
        self.maze = [[Cell(x, y) for y in range(num_of_cells_y)] for x in range(num_of_cells_x)]
        self.create_maze()
        self.set_item_and_enemies_in_location(self.generate_locations(items, enemies), items, enemies)
        write_map(self, 'maze')

    def get_cell(self, x: int, y: int) -> Cell:
        return self.maze[x][y]

    def get_valid_neighbours(self, cell: Cell) -> list[tuple]:
        """
        Checks the current cells neighbours by decrement or increment it's x and y value
        If the neighbouring cell is inside the map, it appends to the neighbour list
        :param cell: Cell instance, current cell
        :return: list[tuple], list of neighbours
        """
        neighbours = []

        for direction, (direction_x, direction_y) in DIRECTIONS:
            neighbour_x, neighbour_y = cell.x + direction_x, cell.y + direction_y
            if 0 <= neighbour_x < self.num_of_cells_x and 0 <= neighbour_y < self.num_of_cells_y:
                neighbour = self.get_cell(neighbour_x, neighbour_y)
                if neighbour.surrounded_by_walls():
                    neighbours.append((direction, neighbour))

        return neighbours

    def create_maze(self) -> None:
        """
        The method checks the neighbouring cells and moves in random direction by removing the wall between the current
        and the next cell. If the neighbouring cell is a dead end, it backtracks to the last "unvisited" neighbour
        :return None
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
            cell_stack.append(current_cell)
            current_cell = next_cell
            created_cells += 1

    def generate_locations(self, items: list, enemies: list) -> list[tuple]:
        """
        Method to generate random locations for items and enemies
        :param items: set, items for the current maze
        :param enemies: set, enemies in the current maze
        :return: list[tuple], locations for items and enemies
        """
        locations = []
        for _ in range(len(enemies) + len(items)):
            (x, y) = (random.randrange(0, self.num_of_cells_x), random.randrange(0, self.num_of_cells_y))
            while (x, y) in locations or (x, y) == self.maze_end or (x, y) == (self.start_x, self.start_y):
                (x, y) = (random.randrange(0, self.num_of_cells_x), random.randrange(0, self.num_of_cells_y))
            locations.append((x, y))

        return locations

    def set_item_and_enemies_in_location(self, locations: list, items: list, enemies: list) -> None:
        """
        Method to set items and enemies at their new locations
        :param locations: list, valid locations
        :param items: set, items for the current maze
        :param enemies: set, enemies in the current maze
        :return: None
        """
        cnt = 0

        for enemy in enemies:
            enemy.position = locations[cnt]
            enemy.pos = locations[cnt]
            cnt += 1

        for item in items:
            if item.__dict__['label'] == 'door':
                item.position = self.maze_end
            else:
                item.position = locations[cnt]
                cnt += 1

        for line in self.maze:
            for cell in line:
                cell.set_item(list(items))
                cell.set_enemy(list(enemies))
