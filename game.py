from assets.dice import Dice
from maze.map import Maze
from assets.player import Player


class Game:
    def __init__(self):
        self.player = Player()
        self.maze = Maze(5, 5)
        self.dice = Dice()

    def run(self):
        pass

    def set_up_game(self):
        self.maze.create_maze()
        # self.player.set_player_name(input('Please enter your name: '))
        # self.set_player_points()

    def print_info(self):
        if 'lantern' in self.player.inventory:
            print('You\'ve got the lantern. It lights up your surroundings.\nYou can go: ')
            for direction in self.maze.get_cell(*self.player.get_player_position()).walls:
                if not self.maze.get_cell(*self.player.get_player_position()).walls[direction]:
                    print(f'* {direction}')
        else:
            print('You\'re in a dark space.')

        if self.maze.get_cell(*self.player.get_player_position()).got_item:
            print(f'In this room there is a {self.maze.get_cell(*self.player.get_player_position()).item["name"]}')

    def process_user_input(self):
        """Process the user input, and through a matching pattern decide what method(s) to call"""
        command = input('>> ')
        current_location = self.maze.get_cell(*self.player.get_player_position())

        match command.lower().split():
            case ['go', direction] if direction in current_location.walls and not current_location.walls[direction]:
                print('You go further in the maze!\n')
                self.player.go(direction)
            case ['go', *bad_direction]:
                print(f'You can\'t go in that direction: {" ".join(bad_direction)}')

    def set_player_points(self):
        """Set the player attack/defend points, based on the result of the rolled dices"""
        self.player.attack_points = 0
        self.player.defend_points = 0
        for dice in self.dice.roll_dices(3):
            print(dice)
            match dice:
                case 'shield':
                    self.player.defend_points += 1
                case 'sword':
                    self.player.attack_points += 1
                case 'double sword':
                    self.player.attack_points += 2

