from time import sleep
from assets.dice import Dice


class Battle:
    def __init__(self, current_location, former_location, player):
        self.in_battle = True
        self.dice = Dice()
        self.battle(current_location, former_location, player)

    @staticmethod
    def print_battle_stats(current_location, player):
        print(f'\n{player.get_actor_name().upper()} STATS:\nAttack Points - {player.attack_points}\n'
              f'Health Points - {player.health_points}\nDefend Points - {player.defend_points}\n\n'
              f'{current_location.enemy.get_actor_name().upper()} STATS:\nAttack Points - '
              f'{current_location.enemy.attack_points}\nHealth Points - {current_location.enemy.health_points}\n')

    @staticmethod
    def battle_outcome(current_location, player) -> bool:
        """
        Set and print the outcome of each battle round
        :param current_location: The players current location
        :param player: Game player
        :return: True if the battle is over , else False
        """
        current_location.enemy.health_points -= player.attack_points if current_location.enemy.health_points > 0 else 0
        print(f'You strike the {current_location.enemy.get_actor_name()} with {player.attack_points} attack points! '
              f'The enemy has {current_location.enemy.health_points} health points remaining')

        if current_location.enemy.health_points <= 0:
            print(f'You defeated {current_location.enemy.get_actor_name()}!')
            current_location.enemy = None
            return False

        player.health_points += player.defend_points
        player.health_points -= current_location.enemy.attack_points if player.health_points > 0 else 0
        if player.defend_points > 0:
            print(f'You have {player.defend_points} defend points, and therefore block some of the '
                  f'{current_location.enemy.get_actor_name()}\'s attack')
            if player.inventory.item_in_inventory('shield'):
                print(f'And thanks to your {player.inventory.item_in_inventory("shield")}'
                      f' you were able to block extra much!')

        print(f'The {current_location.enemy.get_actor_name()}'
              f' strikes back and attack you with {current_location.enemy.attack_points} '
              f'attack points! You have {player.health_points} health points remaining.')

        if player.health_points <= 0:
            print(f'The {current_location.enemy.get_actor_name()} defeated you!\nGAME OVER!')
            player.alive = False
            return False

        return True

    def set_battle_stats(self, current_location, player):
        """
        Set the player attack/defend points based on the result of the dices, and then print the stats.
        :param current_location: The players current location
        :param player: Game player
        """
        player.attack_points = 0
        player.defend_points = 0

        print('\nYou roll the following dices:')
        for dice in self.dice.roll_dices(4 if player.inventory.item_in_inventory('dice') else 3):
            print(f'* {dice.upper()}')
            match dice:
                case 'shield':
                    player.defend_points += 1 * 2 if player.inventory.item_in_inventory('shield') else 1
                case 'sword':
                    player.attack_points += 1 * 2 if player.inventory.item_in_inventory('sword') else 1
                case 'double sword':
                    player.attack_points += 2 * 2 if player.inventory.item_in_inventory('sword') else 2

        sleep(1)
        self.print_battle_stats(current_location, player)
        sleep(3)

    def battle(self, current_location, last_direction: str, player):
        """
        Battle method with user input. This method settle whether the player wants to roll their dices,
        use an item from the inventory or run back where they came from.
        :param current_location: The players current location
        :param last_direction: The direction where the player came from
        :param player: Game player
        """
        while self.in_battle and current_location.enemy.health_points > 0 and player.health_points > 0:
            command = input('\n>> ')
            match command.lower().split():
                case ['roll'] | ['roll', 'dice'] | ['roll', 'dices']:
                    self.set_battle_stats(current_location, player)
                    self.in_battle = self.battle_outcome(current_location, player)
                case ['use', item]:
                    player.use_battle_item(item, current_location.enemy)
                    self.set_battle_stats(current_location, player)
                    self.in_battle = self.battle_outcome(current_location, player)
                case ['run'] | ['run', 'back'] | ['run', 'away'] | ['escape']:
                    self.escape(last_direction, player)
                case _:
                    print('I don\'t understand!')

    def escape(self, last_direction: str, player):
        """
        Escape battle method. It checks where the player came from and move it back there.
        :param last_direction: The direction which the player came from
        :param player: Game player
        """
        self.in_battle = False
        opposite_direction = None

        match last_direction:
            case 'north':
                opposite_direction = 'south'
            case 'south':
                opposite_direction = 'north'
            case 'east':
                opposite_direction = 'west'
            case 'west':
                opposite_direction = 'east'

        player.go(opposite_direction)
        print(f'You escaped back {opposite_direction}')