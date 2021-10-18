from assets.actors.enemy import Enemy
from assets.dice import Dice
from assets.items import Items
from data.item_data import enviroment_items
from maze.map import Maze
from assets.actors.player import Player


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
        self.enemy = Enemy()
        self.maze = Maze(4, 4)
        self.dice = Dice()
        self.items = Items()
        self.set_up_game()

    def run(self):
        """Main game method. Sequence of all main methods"""
        while True:
            self.print_maze_info()
            print_player_location_in_maze(self)
            self.process_user_input()
            self.maze.get_cell(*self.player.get_actor_position())
            self.engaged_in_battle()
            # if self.player.get_actor_position() == (4, 4):
            #     print('Winner!')
            #     break

    def set_up_game(self):
        """Creates game settings when the game is initialized"""
        # self.items = Items()
        self.maze.create_maze()
        # self.maze.write_map('maze')
        # self.player.set_actor_name(input('Please enter your name: '))  # Still uncertain if this is necessary or not

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
                self.player.get_item(item, current_location)
            case ['drop', item]:
                self.player.drop_item(item, current_location)

            case ['open', item]:
                self.open(item)
            case ['inventory']:
                self.player.print_inventory()

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
        if self.player.get_actor_position() == self.enemy.get_actor_position():
            print(f'You bumped into a {self.enemy.get_actor_name()}\nPREPARE TO FIGHT!')
            while self.enemy.health_points > 0 and self.player.health_points > 0:
                command = input('>> ')
                match command.lower():
                    case 'roll':
                        self.set_player_stats()
                    case ['use', item]:
                        pass
                    case ['run', direction]:
                        pass
                self.battle()

    def battle(self):

        self.battle_outcome()
        print(f'You strike the enemy with {self.player.attack_points} attack points! The enemy has '
              f'{self.enemy.health_points} health points remaining')

        if self.enemy.health_points <= 0:
            print(f'You defeated {self.enemy.get_actor_name()}!')

        print(f'The {self.enemy.get_actor_name()} strikes back!\nIt attacks with {self.enemy.attack_points} attack points!')
        if self.player.defend_points > 0:
            print(f'You block {self.player.defend_points} points from the attack')
            if self.player.inventory.item_in_inventory('shield'):
                print(f'Thanks to your {self.player.inventory.get_inventory_item("shield")}'
                      f' you were able to block extra!')

        if self.player.health_points <= 0:
            print(f'The {self.enemy.get_actor_name()} defeated you!\nGAME OVER!')
            quit()

    def battle_outcome(self):
        self.enemy.health_points -= self.player.attack_points
        if self.enemy.health_points < 0:
            self.enemy.health_points = 0

        self.player.health_points += self.player.defend_points
        self.player.health_points -= self.enemy.attack_points

        if self.player.health_points < 0:
            self.player.health_points = 0

    def print_maze_info(self):
        if self.player.inventory.item_in_inventory('lantern'):
            print('You\'ve got the lantern. It lights up your surroundings.\nYou can go: ')
            for direction in self.maze.get_cell(*self.player.get_actor_position()).walls:
                if not self.maze.get_cell(*self.player.get_actor_position()).walls[direction]:
                    print(f'* {direction}')
        else:
            print('You\'re in a dark space.')

        if self.maze.get_cell(*self.player.get_actor_position()).got_item:
            print(f'In this room there is a {self.maze.get_cell(*self.player.get_actor_position()).item["label"]}')

    def print_battle_stats(self):
        print(f'\n{self.player.get_actor_name().upper()} STATS:\nAP - {self.player.attack_points}\n'
              f'HP - {self.player.health_points}\nDP - {self.player.defend_points}\n'
              f'\n{self.enemy.get_actor_name().upper()} Stats:\nAP - {self.enemy.attack_points}\n'
              f'HP - {self.enemy.health_points}\n')

    def open(self, chest: str):
        current_location = self.maze.get_cell(*self.player.get_actor_position())
        if current_location.got_item() and chest == 'chest':
            for item in enviroment_items:
                if item['label'] == 'chest':
                    self.open_chest(item, self.maze.get_cell(*self.player.get_actor_position()))
        else:
            print("There is nothing to open here!")

    def open_chest(self, chest: dict, current_location: tuple):
        chest['open'] = True
        print(f'The {chest["label"]} contains the following: ')
        for i in chest['contains']:
            print(f'* {i}')
        print('What do you want to do?')
        command = input('>> ')

        match command:
            case ['get', item]:
                self.player.get_item(item, current_location, chest)
            # case ['drop', item]:
            #     self.player.drop_item(item, current_location)
