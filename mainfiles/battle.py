from assets.dice import Dice


class Battle:
    def __init__(self, current_location, player):
        self.dice = Dice()
        self.battle(current_location, player)

    @staticmethod
    def print_battle_stats(current_location, player):
        print(f'\n{player.get_actor_name().upper()} STATS:\nAP - {player.attack_points}\n'
              f'HP - {player.health_points}\nDP - {player.defend_points}\n\n'
              f'{current_location.enemy.get_actor_name().upper()} Stats:\nAP - {current_location.enemy.attack_points}\n'
              f'HP - {current_location.enemy.health_points}\n')

    def set_player_stats(self, player):
        """Set the player attack/defend points, based on the result of the rolled dices"""
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

    def battle(self, current_location, player):
        while current_location.enemy.health_points > 0 and player.health_points > 0:
            command = input('>> ')
            match command.lower():
                case ['roll'] | ['roll', 'dice'] | ['roll', 'dices']:
                    self.set_player_stats(player)
                case ['use', item]:
                    pass
                case ['run', direction]:
                    pass

            current_location.enemy.health_points -= player.attack_points\
                if current_location.enemy.health_points > 0 else 0

            player.health_points += player.defend_points
            player.health_points -= current_location.enemy.attack_points if player.health_points > 0 else 0

            print(f'You strike the enemy with {player.attack_points} attack points! The enemy has '
                  f'{current_location.enemy.health_points} health points remaining')

            if current_location.enemy.health_points <= 0:
                print(f'You defeated {current_location.enemy.get_actor_name()}!')
                current_location.enemy = None
                break

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
                break
