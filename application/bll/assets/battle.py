from time import sleep
from application.bll.assets.dice import Dice


class Battle:
    def __init__(self, current_location, former_location, player):
        self.in_battle = True
        self.dice = Dice()
        self.battle(current_location, former_location, player)

    @staticmethod
    def player_in_battle(current_location, player) -> bool:
        """
        Method to check whether the player is in a battle situation or not
        :param current_location: Cell instance, the players current location
        :param player: Player instance
        :return: bool
        """
        if current_location.enemy.health_points <= 0:
            print(f'You defeated the {current_location.enemy.get_actor_name()}!')
            player.score += (10 * current_location.enemy.level)
            current_location.enemy = None
            return False
        elif player.health_points <= 0:
            print(f'The {current_location.enemy.get_actor_name()} defeated you!\nGAME OVER!')
            player.alive = False
            return False
        return True

    def battle_round(self, current_location, player):
        """
        Set and print the outcome of each battle round
        :param current_location: Cell instance, the players current location
        :param player: Player instance
        return: None
        """
        current_location.enemy.health_points = current_location.enemy.health_points - player.attack_points\
            if current_location.enemy.health_points - player.attack_points > 0 else 0
        print(f'You strike the {current_location.enemy.get_actor_name()} with {player.attack_points} attack points! '
              f'The enemy has {current_location.enemy.health_points} health points remaining')
        self.in_battle = self.player_in_battle(current_location, player)

        if self.in_battle:
            player.health_points += player.defend_points
            player.health_points = player.health_points - current_location.enemy.attack_points\
                if player.health_points - current_location.enemy.attack_points > 0 else 0

            print(f'The {current_location.enemy.get_actor_name()} strikes back and attack you with '
                  f'{current_location.enemy.attack_points} attack points!')
            if player.defend_points > 0:
                print(f'You block the attack with {player.defend_points} defend points!')
                if player.inventory.item_in_inventory('shield'):
                    print(f'And thanks to your {player.inventory.item_in_inventory("shield")}'
                          f' you were able to block extra much!')
            print(f'You have {player.health_points} health points remaining.')
            self.in_battle = self.player_in_battle(current_location, player)

    @staticmethod
    def print_battle_stats(current_location, player):
        print(f'\n{player.get_actor_name().upper()} STATS:\nAttack Points - {player.attack_points}\n'
              f'Health Points - {player.health_points}\nDefend Points - {player.defend_points}\n\n'
              f'{current_location.enemy.get_actor_name().upper()} STATS:\nAttack Points - '
              f'{current_location.enemy.attack_points}\nHealth Points - {current_location.enemy.health_points}\n')

    def set_battle_stats(self, current_location, player):
        """
        Set and print the player attack/defend points based on the result of the dices
        :param current_location: Cell instance, the players current location
        :param player: Player instance
        :return None
        """
        player.attack_points = 0
        player.defend_points = 0

        print('\nYou roll the following dices:')
        for dice in self.dice.roll_dices(4 if player.inventory.item_in_inventory('dice') else 3):
            print(f'* {dice.upper()}')
            match dice:
                case 'shield':
                    player.defend_points += 1 * 2 if player.inventory.item_in_inventory('shield') else 1
                case 'double shield':
                    player.defend_points += 2 * 2 if player.inventory.item_in_inventory('shield') else 2
                case 'sword':
                    player.attack_points += 1 * 2 if player.inventory.item_in_inventory('sword') else 1
                case 'double sword':
                    player.attack_points += 2 * 2 if player.inventory.item_in_inventory('sword') else 2

        sleep(1)
        self.print_battle_stats(current_location, player)
        sleep(2)

    def battle(self, current_location, last_direction: str, player):
        """
        Main battle method.
        :param current_location: Cell instance, the players current location
        :param last_direction: str, the direction where the player came from
        :param player: Player instance
        return: None
        """
        while self.in_battle and current_location.enemy.health_points > 0 and player.health_points > 0:
            command = input('\n>> ')
            match command.lower().split():
                case ['roll'] | ['roll', 'dice'] | ['roll', 'dices']:
                    self.set_battle_stats(current_location, player)
                    self.battle_round(current_location, player)
                case ['use', item]:
                    player.use_battle_item(item, current_location.enemy)
                    player.attack_points = 0
                    player.defend_points = 0
                    self.print_battle_stats(current_location, player)
                    self.battle_round(current_location, player)
                case ['run'] | ['run', 'back'] | ['run', 'away'] | ['escape']:
                    self.escape_battle(last_direction, player)
                case _:
                    print('I don\'t understand!')

    def escape_battle(self, last_direction: str, player):
        """
        Method to escape the battle
        :param last_direction: str, the direction where the player came from
        :param player: Player instance
        :return None
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