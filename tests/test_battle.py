import unittest
from unittest.mock import patch

from assets.actors.enemy import Enemy
from assets.actors.player import Player
from assets.battle import Battle
from data.enemy_data import enemies
from mainfiles.level import Level


class TestBattle(unittest.TestCase):
    @patch('builtins.input', return_value='roll')
    def test_two_handed_sword(self, input):
        player = Player()

        level = Level(1, (5, 5), player)
        level.maze.get_cell(*player.get_actor_position())\
            .set_enemy([Enemy(1, **enemy) for enemy in enemies if enemy['name'] == 'skeleton'])

        level.battle = Battle(level.maze.get_cell(*player.get_actor_position()), 'east', player)
        while player.alive and level.maze.get_cell(*player.get_actor_position()).enemy:
            level.battle.battle(level.maze.get_cell(*player.get_actor_position()), 'east', player)

        self.assertFalse(level.battle.in_battle)


if __name__ == '__main__':
    unittest.main()
