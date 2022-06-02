import unittest
from src.assets import Player
from src.assets.map import Cell


class TestMovement(unittest.TestCase):
    def test_player_movement(self):
        player = Player()
        start_cell = Cell(0, 0)
        east_cell = Cell(1, 0)
        south_cell = Cell(0, 1)

        start_cell.remove_wall(east_cell, 'east')

        direction = 'east'
        if direction in start_cell.walls and not start_cell.walls[direction]:
            player.move(direction)

        self.assertEqual(player.get_actor_position(), (east_cell.x, east_cell.y))

        player.set_actor_position((start_cell.x, start_cell.y))

        direction = 'south'
        if direction in start_cell.walls and not start_cell.walls[direction]:
            player.move(direction)

        self.assertNotEqual(player.get_actor_position(), (south_cell.x, south_cell.y))


if __name__ == '__main__':
    unittest.main()
