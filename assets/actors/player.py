from assets.actors.actor import Actor
from assets.inventory import Inventory

DIRECTIONS = {
    'north': (0, -1),
    'south': (0, 1),
    'east': (1, 0),
    'west': (-1, 0)
}


class Player(Actor):
    def __init__(self):
        super().__init__('', (0, 0), 0, 0, 10)
        self.inventory = Inventory()
        self.in_battle = False

    def got_item(self, item_label: str) -> bool:
        """
        Search in player inventory for a certain item
        :param item_label: The label for the item to search for
        :return: True if the item is found, else False
        """
        for item in self.inventory.inventory:
            if item_label == item['label']:
                match item_label:
                    case 'lantern':
                        return True
                    case 'sword':
                        return True
                    case 'shield':
                        return True
                    case 'key':
                        return True
        return False

    def go(self, direction: str):
        self.set_actor_position(DIRECTIONS[direction])

    def get_item(self, item_label: str, current_location):
        item = None
        if item_label == current_location.item['label']:
            item = current_location.item

        if item:
            if 'get' in item['actions']:
                print(f'You pick up the {item_label}!')

                current_location.item = None
                current_location.got_item = False
                self.inventory.inventory.append(item)
            else:
                print(f'You can\'t pick up {item_label}')
        else:
            print(f'There is no {item_label} here')

    def drop_item(self, item_label: str, current_location):
        item = None
        if not current_location.got_item:
            for item_to_find in self.inventory.inventory:
                if item_label == item_to_find['label']:
                    item = item_to_find
                    break

            if item:
                if 'drop' in item['actions']:
                    print(f'You drop the {item_label}')
                    self.inventory.inventory.remove(item)
                    current_location.item = item
                    current_location.got_item = True
                else:
                    print(f'You can\'t drop the {item_label}, you should have thought of this earlier')
            else:
                print(f'There is no {item_label} in your inventory!')

        else:
            print(f'This room isn\'t empty! You can\'t the {item_label}')

    def print_inventory(self):
        if len(self.inventory.inventory) == 0:
            print('Yor inventory is empty')
        else:
            print(f'\tINVENTORY')
            for item in sorted(self.inventory.inventory, key=lambda i: i['label']):
                print(f'* {item["label"]}')
