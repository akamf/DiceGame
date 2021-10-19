from assets.actors.actor import Actor
from assets.inventory import Inventory
from data.item_data import weapons_and_armors
from maze.map import DIRECTIONS


class Player(Actor):
    def __init__(self):
        super().__init__('player', (0, 0), 0, 0, 10)
        self.inventory = Inventory()
        self.in_battle = False

    def go(self, direction: str):
        """Update player position, based on a constant value from DIRECTIONS"""
        for value in DIRECTIONS:
            if value[0] == direction:
                self.set_actor_position(value[1])

    def get_item(self, item_label: str, current_location, chest=None):
        """
        Get an item from the current player location or from a chest
        :param item_label: The item to get
        :param current_location: The players current location
        :param chest: Chest to get item from, None as default
        """
        item = None

        if chest:
            item = chest.get_chest_content(item_label)
        elif item_label == current_location.item['label']:
            item = current_location.item

        if item:
            if 'get' not in item['actions']:
                print(f'It seems impossible to pick up the {item["label"]}')
            elif not self.inventory.inventory_full():
                print(f'You pick up the {item_label}!')
                self.inventory.inventory.append(item)
                if chest:
                    chest['contains'].remove(item_label)
                else:
                    current_location.item = None
                    current_location.got_item = False
            else:
                print(f'You can\'t pick up {item_label} before you drop something from your inventory')
        else:
            print(f'There is no {item_label} here')

    def drop_item(self, item_label: str, current_location):
        """
        Drop an item from the players inventory
        :param item_label: The item to drop
        :param current_location: The players current location
        """
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

