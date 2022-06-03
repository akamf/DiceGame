import random


def print_battle_stats(current_location, player) -> None:
    from time import sleep

    sleep(1)
    print(f'\n{player.name.upper()} STATS:\nAttack Points - {player.attack_points}\n'
          f'Health Points - {player.health_points}\nDefend Points - {player.defend_points}\n\n'
          f'{current_location.enemy.name.upper()} STATS:\nAttack Points - '
          f'{current_location.enemy.attack_points}\nHealth Points - {current_location.enemy.health_points}\n')
    sleep(2)


def set_battle_stats(player) -> None:
    """
    Set and print the player attack/defend points based on the result of the dices
    :param player: Player obj
    :return None
    """
    player.attack_points = 0
    player.defend_points = 0

    print('\nYou roll the following dices:')
    for dice in player.dices:
        result = dice.roll()
        print(f'* {result}')
        match result:
            case 'shield':
                player.defend_points += 1 * 2 if player.inventory.item_in_inventory('shield') else 1
            case 'double shield':
                player.defend_points += 2 * 2 if player.inventory.item_in_inventory('shield') else 2
            case 'sword':
                player.attack_points += 1 * 2 if player.inventory.item_in_inventory('sword') else 1
            case 'double sword':
                player.attack_points += 2 * 2 if player.inventory.item_in_inventory('sword') else 2


def battle(current_location, last_direction: str, player) -> None:
    """
    Main battle method.
    :param current_location: Cell instance, the players current location
    :param last_direction: str, the direction where the player came from
    :param player: Player instance
    return: None
    """
    while player.in_battle(current_location):
        command = input('\n>> ')
        match command.lower().split():
            case ['roll'] | ['roll', 'dice'] | ['roll', 'dices']:
                set_battle_stats(player)
                print_battle_stats(current_location, player)
                battle_round(current_location, player)
            case ['use', item]:
                player.use_battle_item(item, current_location.enemy)
                player.attack_points = 0
                player.defend_points = 0
                print_battle_stats(current_location, player)
                battle_round(current_location, player)
            case ['run'] | ['run', 'back'] | ['run', 'away'] | ['escape']:
                escape_battle(last_direction, player)
            case _:
                print('I don\'t understand!')


def escape_battle(last_direction: str, player) -> None:
    """
    Method to escape the battle
    :param last_direction: str, the direction where the player came from
    :param player: Player instance
    :return None
    """
    from src.assets.level import OPPOSITE_DIRECTION

    for direction in OPPOSITE_DIRECTION:
        if last_direction == direction[0]:
            player.move(direction[1])
            print(f'You escaped back {direction[1]}')


def battle_over(current_location, player) -> bool:
    """
    Method to check whether the player is in a battle situation or not
    :param current_location: Cell obj, the players current location
    :param player: Player obj
    :return: bool
    """
    if current_location.enemy.health_points <= 0:
        print(f'You defeated the {current_location.enemy.name}!')
        player.score += (10 * current_location.enemy.level)
        current_location.enemy = None
        return True
    elif player.health_points <= 0:
        print(f'The {current_location.enemy.name} defeated you!\nGAME OVER!')
        player.alive = False
        return True

    return False


def battle_round(current_location, player) -> None:
    """
    Set and print the outcome of each battle round
    :param current_location: Cell obj, the players current location
    :param player: Player obj
    return: None
    """
    current_location.enemy.health_points = current_location.enemy.health_points - player.attack_points\
        if current_location.enemy.health_points - player.attack_points > 0 else 0
    print(f'You strike the {current_location.enemy.name} with {player.attack_points} attack points! '
          f'The enemy has {current_location.enemy.health_points} health points remaining')

    if not battle_over(current_location, player):
        player.health_points += player.defend_points
        player.health_points = player.health_points - current_location.enemy.attack_points\
            if player.health_points - current_location.enemy.attack_points > 0 else 0

        print(f'The {current_location.enemy.name} strikes back and attack you with '
              f'{current_location.enemy.attack_points} attack points!')
        if player.defend_points > 0:
            print(f'You block the attack with {player.defend_points} defend points!')
            if player.inventory.item_in_inventory('shield'):
                print(f'And thanks to your {player.inventory.item_in_inventory("shield")}'
                      f' you were able to block extra much!')
        print(f'You have {player.health_points} health points remaining.')


def use_item_in_battle(player, label: str, enemy):
    """
    Method to use items in a battle situation
    :param player: Player obj, current player
    :param label: str, the label of the item
    :param enemy: Enemy instance, current enemy
    :return: None
    """
    if player.inventory.item_in_inventory(label):
        match label:
            case 'potion':
                print(f'You drank the health potion and gained 10 health points!')
                player.health_points += 10
                player.inventory.remove_pouch_item(label)

            case 'pill':
                effect = random.choice(['cursed', 'lucky'])
                print(f'You consume the dark pill and you\'re {effect}!')
                player.inventory.remove_pouch_item(label)

                match effect:
                    case 'lucky':
                        print('You gain 15 health points!')
                        player.health_points += 15
                    case 'cursed':
                        print(f'You faint for a moment and the {enemy.name} takes advantage!\n'
                              f'You lose {enemy.attack_points} health points!')
                        player.health_points -= enemy.attack_points


def engaged_in_battle(direction: str, player, current_location) -> None:
    """
    Check if the player is engaged in battle after it's movement, aka if there's a enemy in the new cell
    :param direction: str, the direction the player moved
    :param player: Player obj
    :param current_location: Cell obj
    :return: None
    """
    print(f'You bumped into a {current_location.enemy.name}'
          f'\nTime to roll those dices!\nRemember: "Each SHIELD gets you 1 defend point and '
          f'each SWORD gets you 1 attack point"', end='')
    battle(current_location, direction, player)
