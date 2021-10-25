import random

from assets.actors.enemy import Enemy
from assets.item import Item
from data.enemy_data import enemies
from data.item_data import key_items, usable_items
from map.maze import Maze
from mainfiles.battle import Battle

START = (0, 0)
GOAL = (2, 2)


def print_player_location_in_maze(game):
    """
    Debug function to see the players position
    The map is dynamic and changes for every run, which makes this very handy!
    """
    print('X Y')
    print(*game.player.get_actor_position())


class Level:
    def __init__(self, level: int, player):
        self.battle = None
        self.level_complete = False
        self.enemies = [Enemy(level, **random.choice(enemies)) for _ in range(GOAL[0])]
        self.items = [Item(**random.choice(usable_items)) for _ in range(GOAL[0])]
        self.items.extend([Item(**item) for item in key_items])
        self.maze = Maze(*(GOAL[0] + 1, GOAL[1] + 1), self.items, self.enemies)
        self.player = player

    def run(self):
        """Main game method. Sequence of all main methods"""
        while not self.level_complete:
            self.print_maze_info()
            print_player_location_in_maze(self)
            self.process_user_input()
            self.maze.get_cell(*self.player.get_actor_position())
            self.engaged_in_battle()

    def process_user_input(self):
        """Process the user input, and through a matching pattern decide what method(s) to call"""
        command = input('>> ')
        current_location = self.maze.get_cell(*self.player.get_actor_position())

        match command.lower().split():
            case ['go', direction] if direction in current_location.walls and not current_location.walls[direction]:
                print('You go further in the map!\n')
                self.player.go(direction)
            case ['go', *bad_direction]:
                print(f'You can\'t go in that direction: {" ".join(bad_direction)}')

            case ['get', item]:
                self.player.pick_up_item(item, current_location)
            # case ['swap']:
            #     print(f'You have to type in two items to continue swapping or "cancel" to cancel')
            #     while len(command.split()) != 2 and command != 'cancel':
            #         command = input('>> ')
            #     self.player.swap_items(command.split(), current_location)
            case ['drop', item]:
                self.player.drop_item(item, current_location)
            case ['check', item]:
                if current_location.item and 'check' in current_location.item.__dict__['actions']:
                    print(f'You pick up and look at the {item}\n'
                          f'It\'s a {current_location.item.__dict__["description"]}')
                else:
                    print(f'You can\'t check that out.')
            case ['investigate', item]:
                print(f'{self.investigate_item(item)}')

            case ['open', item]:
                if not current_location.item or current_location.item.__dict__['label'] != item:
                    print('There is nothing to open here!')
                elif item == current_location.item.__dict__['label']:
                    if self.player.inventory.item_in_inventory('rusty key') or\
                            self.player.inventory.item_in_inventory('golden key'):
                        match item:
                            case 'chest':
                                self.open_chest(current_location.item)
                            case 'door':
                                print('Winner!')
                                self.level_complete = True
                            case _:
                                print(f'I can\'t understand "open {item}"')
                    else:
                        print(f'The {item} is locked, you need something to unlock it with!')
                else:
                    print(f'I can\'t understand "open {item}"')

            case ['inventory']:
                self.player.inventory.print_inventory()

            case _:
                print(f'I don\'t understand command: {command}')

    def open_chest(self, chest):
        if chest.__dict__['label'] == 'chest':
            chest.__dict__['open'] = True

            print(f'The {chest.__dict__["description"]} contains the following: ')
            for i in chest.__dict__['contains']:
                print(f'* {i.__dict__["description"]}')
            print('What do you want to do?')

            while chest.__dict__['open']:
                print('The chest is open')
                command = input('>> ')
                match command.lower().split():
                    case ['get', item]:
                        self.player.pick_up_item(item, self.maze.get_cell(*self.player.get_actor_position()), chest)
                    case ['close'] | ['close', 'chest']:
                        print(f'You close the {chest.__dict__["description"]}')
                        chest.__dict__['open'] = False
                    # case ['drop', item]:
                    #     self.player.drop_item(item, current_location)

    def investigate_item(self, label: str) -> str:
        if self.maze.get_cell(*self.player.get_actor_position()).got_item:
            item = self.maze.get_cell(*self.player.get_actor_position()).item
            if label == item.__dict__['label'] and 'investigate' in item.__dict__['actions']:
                return item.__dict__['bonus']
            elif 'investigate' not in item.__dict__['actions']:
                return f'Can\'t investigate {item.__dict__["description"]} further!'
            elif self.maze.get_cell(*self.player.get_actor_position()).got_item and label != item.__dict__['label']:
                return f'There is no {label} here, but something else!'
        else:
            return 'There is nothing to investigate here!'

    def engaged_in_battle(self):
        if self.maze.get_cell(*self.player.get_actor_position()).enemy:
            print(f'You bumped into a {self.maze.get_cell(*self.player.get_actor_position()).enemy.get_actor_name()}\nPREPARE TO FIGHT!')
            self.battle = Battle(self.maze.get_cell(*self.player.get_actor_position()), self.player)

    def print_maze_info(self):
        if self.player.inventory.item_in_inventory('lantern'):
            print('You\'ve got the lantern. It lights up your surroundings.\nYou can go: ')
            for direction in self.maze.get_cell(*self.player.get_actor_position()).walls:
                if not self.maze.get_cell(*self.player.get_actor_position()).walls[direction]:
                    print(f'* {direction}')
            if self.maze.get_cell(*self.player.get_actor_position()).got_item:
                print(f'There is a {self.maze.get_cell(*self.player.get_actor_position()).item.__dict__["description"]} here')
        else:
            print('You\'re in a dark space.')
            if self.maze.get_cell(*self.player.get_actor_position()).got_item:
                print(f'There is something in this room, maybe check it out?')

