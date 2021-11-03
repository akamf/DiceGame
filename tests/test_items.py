import unittest

from assets.actors.player import Player
from map.level import Level


class TestItems(unittest.TestCase):
    def test_get_item(self):
        level = Level(1, (3, 3), Player())

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
