import random

from assets.actors.enemy import Enemy
from assets.dice import Dice
from assets.item import Item
from data.item_data import environment_items, key_items, weapons_and_armors
from maze.map import Maze
from assets.actors.player import Player

START = (0, 0)
MAX = (4, 4)


def print_player_location_in_maze(game):
    """
    Debug function to see the players position
    The maze is dynamic and changes for every run, which makes this very handy!
    """
    print('X Y')
    print(*game.player.get_actor_position())


class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = [Enemy() for _ in range(0)]
        self.items = [Item(**random.choice(key_items + weapons_and_armors)) for _ in range(MAX[0])]
        self.set_items_positions()
        self.items.extend([Item(**item) for item in environment_items])
        self.maze = Maze(*(MAX[0] + 1, MAX[1] + 1), self.items)
        self.dice = Dice()

    def run(self):
        """Main game method. Sequence of all main methods"""
        while True:
            self.print_maze_info()
            print_player_location_in_maze(self)
            self.process_user_input()
            self.maze.get_cell(*self.player.get_actor_position())
            # self.engaged_in_battle()

    def process_user_input(self):
        """Process the user input, and through a matching pattern decide what method(s) to call"""
        command = input('>> ')
        current_location = self.maze.get_cell(*self.player.get_actor_position())

        match command.lower().split():
            case ['go', direction] if direction in current_location.walls and not current_location.walls[direction]:
                print('You go further in the maze!\n')
                self.player.go(direction)
            case ['go', *bad_direction]:
                print(f'You can\'t go in that direction: {" ".join(bad_direction)}')

            case ['get', item]:
                self.player.pick_up_item(item, current_location)
            case ['swap']:
                print(f'You have to type in two items to continue swapping or "cancel" to cancel')
                while len(command.split()) != 2 and command != 'cancel':
                    command = input('>> ')
                self.player.swap_items(command.split(), current_location)
            case ['drop', item]:
                self.player.drop_item(item, current_location)
            case ['check', item]:
                print(f'You pick up and look at the {item}\n{self.check_item()}')
            case ['investigate', item]:
                print(f'{self.investigate_item(item)}')

            case ['open', item]:
                if not current_location.got_item or current_location.item.__dict__ not in environment_items:
                    print('There is nothing to open here!')
                elif item == current_location.item.__dict__['label']:
                    if self.player.inventory.item_in_inventory('rusty key') or\
                            self.player.inventory.item_in_inventory('golden key'):
                        match item:
                            case 'chest':
                                self.open_chest(current_location.item)
                            case 'door':
                                print('Winner!')
                                quit()
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

    def set_player_stats(self):
        """Set the player attack/defend points, based on the result of the rolled dices"""
        self.player.attack_points = 0
        self.player.defend_points = 0
        print('The dices shows:')
        for dice in self.dice.roll_dices(4 if self.player.inventory.item_in_inventory('dice') else 3):
            print(f'* {dice}')
            match dice:
                case 'shield':
                    self.player.defend_points += 1 * 2 if self.player.inventory.item_in_inventory('shield') else 1
                case 'sword':
                    self.player.attack_points += 1 * 2 if self.player.inventory.item_in_inventory('sword') else 1
                case 'double sword':
                    self.player.attack_points += 2 * 2 if self.player.inventory.item_in_inventory('sword') else 2

    def engaged_in_battle(self):
        if self.get_enemy(self.player.get_actor_position()):
            print(f'You bumped into a {self.get_enemy(self.player.get_actor_position()).get_actor_name()}\nPREPARE TO FIGHT!')
            self.battle()

    def battle(self):
        while self.get_enemy(self.player.get_actor_position()).health_points > 0 and self.player.health_points > 0:
            command = input('>> ')
            match command.lower():
                case 'roll':
                    self.set_player_stats()
                case ['use', item]:
                    pass
                case ['run', direction]:
                    pass

            self.battle_outcome()
            print(f'You strike the enemy with {self.player.attack_points} attack points! The enemy has '
                  f'{self.get_enemy(self.player.get_actor_position()).health_points} health points remaining')

            if self.get_enemy(self.player.get_actor_position()).health_points <= 0:
                print(f'You defeated {self.get_enemy(self.player.get_actor_position()).get_actor_name()}!')
                self.enemies.remove(self.get_enemy(self.player.get_actor_position()))
                break

            print(f'The {self.get_enemy(self.player.get_actor_position()).get_actor_name()}'
                  f' strikes back!\nIt attacks with {self.get_enemy(self.player.get_actor_position()).attack_points}'
                  f' attack points!')
            if self.player.defend_points > 0:
                print(f'You block {self.player.defend_points} points from the attack')
                if self.player.inventory.item_in_inventory('shield'):
                    print(f'Thanks to your {self.player.inventory.get_item_from_pouch("shield")}'
                          f' you were able to block extra!')

            if self.player.health_points <= 0:
                print(f'The {self.get_enemy(self.player.get_actor_position()).get_actor_name()} defeated you!\nGAME OVER!')
                quit()

    def battle_outcome(self):
        self.get_enemy(self.player.get_actor_position()).health_points -= self.player.attack_points
        if self.get_enemy(self.player.get_actor_position()).health_points < 0:
            self.get_enemy(self.player.get_actor_position()).health_points = 0

        self.player.health_points += self.player.defend_points
        self.player.health_points -= self.get_enemy(self.player.get_actor_position()).attack_points

        if self.player.health_points < 0:
            self.player.health_points = 0

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

    def print_battle_stats(self):
        print(f'\n{self.player.get_actor_name().upper()} STATS:\nAP - {self.player.attack_points}\n'
              f'HP - {self.player.health_points}\nDP - {self.player.defend_points}\n'
              f'\n{self.get_enemy(self.player.get_actor_position()).get_actor_name().upper()} Stats:\nAP - {self.get_enemy(self.player.get_actor_position()).attack_points}\n'
              f'HP - {self.get_enemy(self.player.get_actor_position()).health_points}\n')

    def open_chest(self, chest):
        if chest.__dict__['label'] == 'chest':
            chest.__dict__['open'] = True

            print(f'The {chest.__dict__["description"]} contains the following: ')
            for i in chest.__dict__['contains']:
                print(f'* {i["description"]}')
            print('What do you want to do?')

            while chest.__dict__['open']:
                command = input('>> ')
                match command.lower().split():
                    case ['get', item]:
                        self.player.pick_up_item(item, self.maze.get_cell(*self.player.get_actor_position()), chest)
                    case ['close'] | ['close', 'chest']:
                        print(f'You close the {chest.__dict__["description"]}')
                        chest.__dict__['open'] = False
                    # case ['drop', item]:
                    #     self.player.drop_item(item, current_location)

    def check_item(self) -> str:
        item = self.maze.get_cell(*self.player.get_actor_position()).item
        if item and 'check' in item.__dict__['actions']:
            return f'It\'s a {item.__dict__["description"]}'

        return f'Can\'t check it out!'

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


    def get_enemy(self, current_location: tuple):
        for enemy in self.enemies:
            if enemy.get_actor_position() == current_location:
                return enemy

    def set_items_positions(self):
        positions = []
        for i in range(len(self.items)):
            (x, y) = (random.randrange(0, MAX[0]), random.randrange(0, MAX[0]))
            while (x, y) in positions or (x, y) == (MAX[0] - 1, MAX[0] - 1):
                (x, y) = (random.randrange(0, MAX[0]), random.randrange(0, MAX[0]))
            positions.append((x, y))

        cnt = 0
        for item in self.items:
            item.position = positions[cnt]
            cnt += 1
