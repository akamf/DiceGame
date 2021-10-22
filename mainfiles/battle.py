from assets.dice import Dice


class Battle:
    def __init__(self, current_location, player):
        self.location = current_location
        self.player = player
        self.dice = Dice()

    def print_battle_stats(self):
        print(f'\n{self.player.get_actor_name().upper()} STATS:\nAP - {self.player.attack_points}\n'
              f'HP - {self.player.health_points}\nDP - {self.player.defend_points}\n'
              f'\n{self.location.enemy.get_actor_name().upper()} Stats:\nAP - {self.location.enemy.attack_points}\n'
              f'HP - {self.location.enemy.health_points}\n')

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

    def battle(self, current_location):
        while current_location.enemy.health_points > 0 and self.player.health_points > 0:
            command = input('>> ')
            match command.lower():
                case 'roll':
                    self.set_player_stats()
                case ['use', item]:
                    pass
                case ['run', direction]:
                    pass

            current_location.enemy.health_points -= self.player.attack_points\
                if current_location.enemy.health_points > 0 else 0
            self.player.health_points += self.player.defend_points
            self.player.health_points -= current_location.enemy.attack_points if self.player.health_points > 0 else 0
            print(f'You strike the enemy with {self.player.attack_points} attack points! The enemy has '
                  f'{current_location.enemy.health_points} health points remaining')

            if current_location.enemy.health_points <= 0:
                print(f'You defeated {current_location.enemy.get_actor_name()}!')
                current_location.enemy = None
                break

            print(f'The {current_location.enemy.get_actor_name()}'
                  f' strikes back!\nIt attacks with {current_location.enemy.attack_points}'
                  f' attack points!')
            if self.player.defend_points > 0:
                print(f'You block {self.player.defend_points} points from the attack')
                if self.player.inventory.item_in_inventory('shield'):
                    print(f'Thanks to your {self.player.inventory.get_item_from_pouch("shield")}'
                          f' you were able to block extra!')

            if self.player.health_points <= 0:
                print(f'The {current_location.enemy.get_actor_name()} defeated you!\nGAME OVER!')
                quit()

    # def battle_outcome(self, current_location):
    #     current_location.enemy.health_points -= self.player.attack_points if current_location.enemy.health_points > 0 else 0
    #     self.player.health_points += self.player.defend_points
    #     self.player.health_points -= current_location.enemy.attack_points if self.player.health_points > 0 else 0
