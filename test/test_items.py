import unittest
from unittest.mock import patch

from src.assets import Enemy
from src.assets import Player
from src.assets import Item
from src.db.data import enemies
from src.db.data import usable_items, key_items
from src.assets.map import Cell
from src.assets.level import Level


class TestItemFunctions(unittest.TestCase):
    def test_get_item(self):
        player = Player()
        cell = Cell(0, 0)
        cell.set_item([Item(**item) for item in usable_items if item['label'] == 'dice'])

        player.pick_up_item(cell.item.__dict__['label'], cell)
        self.assertTrue(player.inventory.item_in_inventory('dice'))

    def test_drop_item(self):
        player = Player()
        cell = Cell(0, 0)
        player.inventory.pouch.append(Item(**usable_items[1]))

        player.drop_item('dice', cell)
        self.assertEqual(cell.item.__dict__['label'], 'dice')


class TestItems(unittest.TestCase):
    def test_health_potion(self):
        player = Player()
        player.inventory.pouch.append(Item(**usable_items[2]))

        original_health_points = player.health_points
        player.use_battle_item('potion', Enemy(1, **enemies[0]))

        self.assertEqual((original_health_points + 10), player.health_points)

    def test_dark_pill(self):
        player = Player()
        player.inventory.pouch.append(Item(**usable_items[4]))
        enemy = Enemy(1, **enemies[0])

        original_health_points = player.health_points
        player.use_battle_item('pill', enemy)

        # I don't know if try-except is the correct way to go here,
        # but it worked and I don't know how to test this item otherwise (It has two different outcomes)
        try:
            self.assertEqual((original_health_points + 15), player.health_points)
        except:
            self.assertEqual((original_health_points - enemy.attack_points), player.health_points)

    @patch('builtins.input', return_value='open door')
    def test_golden_key(self, input):
        player = Player()
        player.inventory.pouch.append(Item(**key_items[0]))

        level = Level(1, (5, 5), player)
        level.maze.get_cell(*player.get_actor_position())\
            .set_item([Item(**item) for item in key_items if item['label'] == 'door'])
        level.process_user_input()

        self.assertTrue(level.level_complete)

    def test_lantern(self):
        player = Player()
        player.inventory.right_hand = Item(**usable_items[0])

        level = Level(1, (5, 5), player)

        self.assertNotEqual(level.print_maze_info(), 'The area is very dark!')


if __name__ == '__main__':
    unittest.main()
