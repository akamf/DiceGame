from assets.actors.actor import Actor
from assets.inventory import Inventory
from data.item_data import weapons_and_armors
from maze.map import DIRECTIONS

STARTING_POINT = (0, 0)


class Player(Actor):
    def __init__(self):
        super().__init__('player', STARTING_POINT, 0, 0, 10)
        self.inventory = Inventory()
        self.in_battle = False

    def go(self, direction: str):
        """Update player position, based on a constant value from DIRECTIONS"""
        for value in DIRECTIONS:
            if value[0] == direction:
                self.set_actor_position(value[1])

    def pick_up_item(self, item_label: str, current_location, chest=None):
        """
        Pick up an item from the current location, or from a chest, and append it to the players inventory
        :param item_label: The item to get
        :param current_location: The players current location
        :param chest: Chest to get item from, None as default
        """
        item = None
        if chest:
            if item_label in chest['contains']:
                for i in weapons_and_armors:
                    if i['label'] == item_label:
                        item = i
                self.inventory.process_item_pickup(item, current_location, chest)
            else:
                print(f'There is no {item_label} in the chest')

        elif not current_location.item or item_label != current_location.item['label']:
            print(f'There is no {item_label} here')

        elif item_label == current_location.item['label']:
            self.inventory.process_item_pickup(current_location.item, current_location)

    def drop_item(self, item_label: str, current_location):
        """
        Drop an item from the players inventory
        :param item_label: The item to drop
        :param current_location: The players current location
        """
        item = None
        if not current_location.got_item:
            for item_to_find in self.inventory.pouch:
                if item_label == item_to_find['label']:
                    item = item_to_find
                    break

            if item:
                if 'drop' in item['actions']:
                    print(f'You drop the {item_label}')
                    self.inventory.pouch.remove(item)
                    current_location.item = item
                    current_location.got_item = True
                else:
                    print(f'You can\'t drop the {item_label}, you should have thought of this earlier')
            else:
                print(f'There is no {item_label} in your inventory!')

        else:
            print(f'This room isn\'t empty! You can\'t drop the {item_label}')
