import random

from assets.actor.enemy import Enemy
from assets.input import process_user_input
from assets.inventory import Item
from assets.map.maze import Maze

import db.controller as controller


class GameLevel:
    def __init__(self, difficulty: int,  player) -> None:
        self.__maze_size = (5, 5)
        self.complete = False
        self.difficulty = difficulty
        self.enemies = [Enemy(self.difficulty, **random.choice(controller.get_all_enemies())) for _ in range(self.maze_size[0])]
        self.maze = Maze(*self.maze_size, self.level_items(3), self.enemies)
        self.player = player

    @property
    def maze_size(self) -> tuple:
        if self.difficulty % 5 == 0:
            return self.__maze_size[0] + 2, self.__maze_size[1] + 2
        return self.__maze_size

    @maze_size.setter
    def maze_size(self, s: tuple) -> None:
        if self.difficulty % 5 == 0:
            self.__maze_size = (s[0] + 2, s[1] + 2)
        else:
            self.__maze_size = s

    @staticmethod
    def level_items(num_of_items: int) -> list:
        """
        Method to set which items to appear in the maze
        :return: set
        """
        items = [Item(**item) for item in controller.get_all_items_from_type('usable item')]
        level_items = {random.choice(items) for _ in range(num_of_items)}
        level_items.update({Item(**item) for item in controller.get_all_items_from_type('key item')})
        return list(level_items)

    def run(self):
        self.print_maze_info()
        while not self.complete and self.player.alive:
            process_user_input(self)

        if self.player.alive:
            print(f'You enter a new maze. Your current score is {self.player.score}, well done!\n\n'
                  f'FOR YOUR INFORMATION: You\'re pouch will lose it\'s belongings, but the items in your hands will'
                  f' remain. You will also gain some extra health points for your journey. Good luck!\n')

    def print_maze_info(self, came_from=None) -> None:
        if came_from:
            print(f'You came from {came_from}')

        if self.player.inventory.item_in_inventory('lantern'):
            print('You\'ve got the lantern. It lights up your surroundings.\nYou can go: ')
            for direction in self.maze.get_cell(*self.player.position).walls:
                if not self.maze.get_cell(*self.player.position).walls[direction]:
                    print(f'* {direction}')
            if self.maze.get_cell(*self.player.position).got_item:
                print(f'There is a '
                      f'{self.maze.get_cell(*self.player.position).item.__dict__["description"]} here')
        else:
            print('The area is very dark!')
            if self.maze.get_cell(*self.player.position).got_item:
                print('There is something in this room, maybe check it out?')
