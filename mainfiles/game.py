from assets.actors.enemy import Enemy
from assets.dice import Dice
from assets.items import Items
from maze.map import Maze
from assets.actors.player import Player

DIRECTIONS = {
    'north': (0, -1),
    'south': (0, 1),
    'east': (1, 0),
    'west': (-1, 0)
}


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
        self.maze = Maze(5, 5)
        self.dice = Dice()
        self.items = None
        self.set_up_game()

    def run(self):
        """Main game method. Sequence of all main methods"""
        while True:
            self.print_info()
            print_player_location_in_maze(self)
            self.process_user_input()
            self.maze.get_cell(*self.player.get_actor_position())
            self.engaged_battle()
            if self.player.get_actor_position() == (4, 4):
                print('Winner!')
                break

    def set_up_game(self):
        """Sets up the game when it's initialized"""
        # self.items = Items()
        self.maze.create_maze()
        self.maze.write_map('maze')
        # self.player.set_actor_name(input('Please enter your name: '))  # Still uncertain if this is necessary or not

    def print_info(self):
        if self.player.got_item('lantern'):
            print('You\'ve got the lantern. It lights up your surroundings.\nYou can go: ')
            for direction in self.maze.get_cell(*self.player.get_actor_position()).walls:
                if not self.maze.get_cell(*self.player.get_actor_position()).walls[direction]:
                    print(f'* {direction}')
        else:
            print('You\'re in a dark space.')

        if self.maze.get_cell(*self.player.get_actor_position()).got_item:
            print(f'In this room there is a {self.maze.get_cell(*self.player.get_actor_position()).item["label"]}')

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

            case ['inventory']:
                self.player.print_inventory()

            case _:
                print(f'I don\'t understand command: {command}')

    def set_player_stats(self):
        """Set the player attack/defend points, based on the result of the rolled dices"""
        self.player.attack_points = 0
        self.player.defend_points = 0
        print('The dices shows:')
        for dice in self.dice.roll_dices(4 if self.player.got_item('dice') else 3):
            print(f'* {dice}')
            match dice:
                case 'shield':
                    self.player.defend_points += 1 * 2 if self.player.got_item('shield') else 1
                case 'sword':
                    self.player.attack_points += 1 * 2 if self.player.got_item('sword') else 1
                case 'double sword':
                    self.player.attack_points += 2 * 2 if self.player.got_item('sword') else 2

    def engaged_battle(self):
        if self.player.get_actor_position() == self.enemy.get_actor_position():
            print(f'You bumped into a {self.enemy.get_actor_name()}\nPREPARE TO FIGHT!')
            while self.enemy.health_points > 0 and self.player.health_points > 0:
                command = input('>> ')
                match command.lower():
                    case 'roll':
                        self.set_player_stats()
                    case ['use', item]:
                        pass
                self.battle()

    def battle(self):
        if self.player.got_item('shield') and self.player.defend_points > 0:
            print(f'Your {self.player.inventory.get_inventory_item("shield")} blocks {self.player.defend_points}'
                  f' in the attack!')
            self.player.health_points += self.player.defend_points

        print(f'P-AP\tP-HP\tE-AP\tE-HP\n{self.player.attack_points}\t{self.player.health_points}\t'
              f'{self.enemy.attack_points}\t{self.enemy.health_points}')
        self.player.health_points -= self.enemy.attack_points
        self.enemy.health_points -= self.player.attack_points
        print(f'{self.enemy.get_actor_name()} strikes!\nYou lose {self.enemy.attack_points} hp!')
        print(f'You strike the enemy with {self.player.attack_points} points!')
        print(f'Your HP\tEnemy HP\n{self.player.health_points}\t{self.enemy.health_points}')
