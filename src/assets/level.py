import random

from src.assets.actor.enemy import Enemy
from src.assets.item import Item
from src.assets.map.maze import Maze
from src.assets.battle import Battle

import src.db.controller as controller


OPPOSITE_DIRECTION = [
    ('north', 'south'),
    ('south', 'north'),
    ('east', 'west'),
    ('west', 'east'),
]


class Level:
    def __init__(self, level: int, maze_size: tuple, player) -> None:
        self.battle = None
        self.level_complete = False
        self.enemies = {Enemy(level, **random.choice(controller.get_all_enemies())) for _ in range(maze_size[0])}
        self.maze = Maze(*maze_size, self.level_items(), self.enemies)
        self.player = player

    def run_level(self):
        self.print_maze_info(None)
        while not self.level_complete and self.player.alive:
            self.process_user_input()

        if self.player.alive:
            print(f'You enter a new maze. Your current score is {self.player.score}, well done!\n\n'
                  f'FOR YOUR INFORMATION: You\'re pouch will lose it\'s belongings, but the items in your hands will'
                  f' remain. You will also gain some extra health points for your journey. Good luck!\n')

    @staticmethod
    def level_items() -> set:
        """
        Method to set which items to appear in the maze
        :return: set
        """
        items = [Item(**item) for item in controller.get_all_items_from_type('usable item')]
        level_items = {random.choice(items) for _ in range(3)}
        level_items.update({Item(**item) for item in controller.get_all_items_from_type('key item')})
        return level_items

    def process_user_input(self) -> None:
        """
        Main method. Process the users input, and through a matching pattern decide what method(s) to call
        :return: None
        """
        came_from = None
        current_location = self.maze.get_cell(*self.player.position)
        command = input('>> ')

        match command.lower().split():
            case ['go', direction] if direction in current_location.walls and not current_location.walls[direction]:
                print('You go further in the maze!')
                for i in OPPOSITE_DIRECTION:
                    if direction == i[0]:
                        came_from = i[1]
                        break
                self.player.go(direction)
                self.engaged_in_battle(direction)
            case ['go', *bad_direction]:
                print(f'You can\'t go in that direction: {" ".join(bad_direction)}')

            case ['get', item]:
                self.player.pick_up_item(item, current_location)
            case ['drop', item]:
                self.player.drop_item(item, current_location)
            case ['check', item]:
                if current_location.item and 'check' in current_location.item.__dict__['actions']:
                    print(f'You look at the {item}\nIt\'s a {current_location.item.__dict__["description"]}')
                else:
                    print(f'You can\'t check that out.')
            case ['investigate', item]:
                print(f'{self.investigate_item(item)}')

            case ['open', item]:
                if not current_location.item or current_location.item.__dict__['label'] != item:
                    print('There is nothing to open here!')
                elif item == current_location.item.__dict__['label']:
                    if self.player.inventory.item_in_inventory(current_location.item.__dict__['requirements']):
                        match item:
                            case 'chest':
                                self.open_chest(current_location.item)
                            case 'door':
                                print('You open the door and move further!\n')
                                self.level_complete = True
                            case _:
                                print(f'I can\'t understand "open {item}"')
                    else:
                        print(f'The {item} is locked, you need something to unlock it with!')
                else:
                    print(f'I can\'t understand "open {item}"')

            case ['inventory']:
                self.player.inventory.print_inventory()
            case ['quit']:
                self.player.alive = False

            case _:
                print(f'I don\'t understand {command}...')

        if not self.level_complete and self.player.alive:
            self.print_maze_info(came_from)

    def open_chest(self, chest):
        """
        Method to open a chest
        :param chest: Item instance
        :return: None
        """
        if chest.__dict__['label'] == 'chest':
            chest.__dict__['open'] = True
            print(f'The {chest.__dict__["description"]} is open and contains the following: ')
            for i in chest.__dict__['contains']:
                print(f'* {i.__dict__["description"]}')

        while chest.__dict__['open']:
            command = input('>> ')
            match command.lower().split():
                case ['get', item]:
                    self.player.pick_up_item(item, self.maze.get_cell(*self.player.position), chest)
                case ['close'] | ['close', 'chest']:
                    print(f'You close the {chest.__dict__["description"]}')
                    chest.__dict__['open'] = False
                case _:
                    print(f'I don\'t understand {command}...')

    def investigate_item(self, label: str) -> str:
        """
        Method to investigate an item further, if possible
        :param label: str, label of the item
        :return: str
        """
        if self.maze.get_cell(*self.player.position).got_item:
            item = self.maze.get_cell(*self.player.position).item
            if label == item.__dict__['label'] and 'investigate' in item.__dict__['actions']:
                return item.__dict__['bonus']
            elif 'investigate' not in item.__dict__['actions']:
                return f'Can\'t investigate {item.__dict__["description"]} further!'
            elif self.maze.get_cell(*self.player.position).got_item and label != item.__dict__['label']:
                return f'There is no {label} here, but something else!'
        else:
            return 'There is nothing to investigate here!'

    def engaged_in_battle(self, direction: str) -> None:
        """
        Check if the player is engaged in battle after it's movement, aka if there's a enemy in the new cell
        :param direction: str, the direction the player moved
        :return: None
        """
        if self.maze.get_cell(*self.player.position).enemy:
            print(f'You bumped into a {self.maze.get_cell(*self.player.position).enemy.name}'
                  f'\nTime to roll those dices!\nRemember: "Each SHIELD gets you 1 defend point and '
                  f'each SWORD gets you 1 attack point"', end='')
            self.battle = Battle(self.maze.get_cell(*self.player.position), direction, self.player)

    def print_maze_info(self, came_from: str) -> None:
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
