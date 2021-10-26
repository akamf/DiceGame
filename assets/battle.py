from assets.dice import Dice


class Battle:
    def __init__(self, current_location, former_location, player):
        self.in_battle = True
        self.dice = Dice()
        self.battle(current_location,former_location, player)

    @staticmethod
    def print_battle_stats(current_location, player):
        print(f'\n{player.get_actor_name().upper()} STATS:\nAP - {player.attack_points}\n'
              f'HP - {player.health_points}\nDP - {player.defend_points}\n\n'
              f'{current_location.enemy.get_actor_name().upper()} Stats:\nAP - {current_location.enemy.attack_points}\n'
              f'HP - {current_location.enemy.health_points}\n')

    @staticmethod
    def battle_outcome(current_location, player) -> bool:
        print(f'You strike the enemy with {player.attack_points} attack points! The enemy has '
              f'{current_location.enemy.health_points} health points remaining')

        if current_location.enemy.health_points <= 0:
            print(f'You defeated {current_location.enemy.get_actor_name()}!')
            current_location.enemy = None
            return False

        print(f'The {current_location.enemy.get_actor_name()}'
              f' strikes back!\nIt attacks with {current_location.enemy.attack_points}'
              f' attack points!')
        if player.defend_points > 0:
            print(f'You block {player.defend_points} points from the attack')
            if player.inventory.item_in_inventory('shield'):
                print(f'Thanks to your {player.inventory.get_item_from_pouch("shield")}'
                      f' you were able to block extra!')

        if player.health_points <= 0:
            print(f'The {current_location.enemy.get_actor_name()} defeated you!\nGAME OVER!')
            player.alive = False
            return False

        return True

    @staticmethod
    def update_health_points(current_location, player):
        current_location.enemy.health_points -= player.attack_points \
            if current_location.enemy.health_points > 0 else 0

        player.health_points += player.defend_points
        player.health_points -= current_location.enemy.attack_points if player.health_points > 0 else 0

    def set_battle_stats(self, current_location, player):
        """
        Set the player attack/defend points based on the result of the dices, and then print the stats.
        Finally it update the player and enemy health points.
        :param current_location: The players current location
        :param player: Game player
        """
        player.attack_points = 0
        player.defend_points = 0

        print('The dices shows:')
        for dice in self.dice.roll_dices(4 if player.inventory.item_in_inventory('dice') else 3):
            print(f'* {dice}')
            match dice:
                case 'shield':
                    player.defend_points += 1 * 2 if player.inventory.item_in_inventory('shield') else 1
                case 'sword':
                    player.attack_points += 1 * 2 if player.inventory.item_in_inventory('sword') else 1
                case 'double sword':
                    player.attack_points += 2 * 2 if player.inventory.item_in_inventory('sword') else 2

        self.print_battle_stats(current_location, player)
        self.update_health_points(current_location, player)

    def battle(self, current_location, former_location, player):
        while self.in_battle and current_location.enemy.health_points > 0 and player.health_points > 0:
            command = input('>> ')
            match command.lower().split():
                case ['roll'] | ['roll', 'dice'] | ['roll', 'dices']:
                    self.set_battle_stats(current_location, player)
                    self.in_battle = self.battle_outcome(current_location, player)
                case ['use', item]:
                    player.use_battle_item(item)
                    self.set_battle_stats(current_location, player)
                    self.in_battle = self.battle_outcome(current_location, player)
                case ['run'] | ['run', 'back'] | ['run', 'away'] | ['escape']:
                    self.escape(former_location, player)
                case _:
                    print('I don\'t understand!')

    def escape(self, former_location: str, player):
        """
        Escape battle method. It checks where the player came from and move it back there.
        :param former_location: The direction which the player came from
        :param player: Game player
        """
        self.in_battle = False
        opposite_direction = ''

        match former_location:
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
