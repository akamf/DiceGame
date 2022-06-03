from src.assets.battle import engaged_in_battle
from src.assets.inventory import drop_item, pick_up_item, open_chest, inspect_item
from src.assets.map.directions import OPPOSITE_DIRECTIONS


def process_user_input(level) -> None:
    """
    Main method. Process the users input, and through a matching pattern decide what method(s) to call
    :return: None
    """
    came_from = None
    current_location = level.maze.get_cell(*level.player.position)
    command = input('>> ')

    match command.lower().split():
        case ['go', direction] if direction in current_location.walls and not current_location.walls[direction]:
            print('You go further in the maze!')
            for key, value in OPPOSITE_DIRECTIONS.items():
                if direction == key:
                    came_from = value
                    break
            level.player.move(direction)
            current_location = level.maze.get_cell(*level.player.position)

            if current_location.enemy:
                engaged_in_battle(direction, level.player, current_location)
        case ['go', *bad_direction]:
            print(f'You can\'t go in that direction: {" ".join(bad_direction)}')

        case ['get', item]:
            pick_up_item(level.player, item, current_location)
        case ['drop', item]:
            drop_item(level.player, item, current_location)
        case ['check', item]:
            if current_location.item and 'check' in current_location.item.__dict__['actions']:
                print(f'You look at the {item}\nIt\'s a {current_location.item.__dict__["description"]}')
            else:
                print(f'You can\'t check that out.')
        case ['inspect', item]:
            print(f'{inspect_item(current_location, item)}')

        case ['open', item]:
            if not current_location.item or current_location.item.__dict__['label'] != item:
                print('There is nothing to open here!')
            elif item == current_location.item.__dict__['label']:
                if level.player.inventory.item_in_inventory(current_location.item.__dict__['requirements']):
                    match item:
                        case 'chest':
                            open_chest(level.player, current_location.item)
                        case 'door':
                            print('You open the door and move further!\n')
                            level.complete = True
                        case _:
                            print(f'I can\'t understand "open {item}"')
                else:
                    print(f'The {item} is locked, you need something to unlock it with!')
            else:
                print(f'I can\'t understand "open {item}"')

        case ['inventory']:
            level.player.inventory.print_inventory()
        case ['quit']:
            level.player.alive = False

        case _:
            print(f'I don\'t understand {command}...')

    if not level.complete and level.player.alive:
        level.print_maze_info(came_from)
