from assets.actors.actor import Actor
from assets.inventory import Inventory
from map.maze import DIRECTIONS


class Player(Actor):
    def __init__(self):
        super().__init__('player', (0, 0), 0, 0, 10, 1)
        self.inventory = Inventory()
        self.alive = True

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
        if chest:
            for item in chest.__dict__['contains']:
                if item_label == item.__dict__['label']:
                    self.inventory.process_item_pickup(item, current_location, chest)
                else:
                    print(f'There is no {item_label} in the chest')

        elif not current_location.item or item_label != current_location.item.__dict__['label']:
            print(f'There is no {item_label} here')

        elif item_label == current_location.item.__dict__['label']:
            self.inventory.process_item_pickup(current_location.item, current_location)

    def drop_item(self, label: str, current_location):
        """
        Drop an item from the players inventory
        :param label: The label of the item to drop
        :param current_location: The players current location
        """
        item = None
        if not current_location.got_item:
            for item_to_find in self.inventory.pouch:
                if label == item_to_find.__dict__['label']:
                    item = item_to_find
                    break

            if item:
                if 'drop' in item.__dict__['actions']:
                    print(f'You drop the {label}')
                    self.inventory.pouch.remove(item)
                    current_location.item = item
                    current_location.got_item = True
                else:
                    print(f'You can\'t drop the {label}, you should have thought of this earlier')

            else:
                print(f'There is no {label} in your inventory!')
        else:
            print(f'This space isn\'t empty! You can\'t drop the {label}')

    # def swap_items(self, items: list, current_location, chest=None):
    #     item1, item2 = None, None
    #
    #     if current_location.got_item:
    #         for item in self.inventory.pouch:
    #             for i in items:
    #                 if item.__dict__['label'] == i or item.__dict__['description'] == i:
    #                     item1 = item
    #                     self.inventory.pouch.remove(item)
    #         for i in items:
    #             if i == current_location.item.__dict__['label'] or i == current_location.item.__dict__['description']:
    #                 item2 = current_location.item
    #
    #     if item1 and item2:
    #         item1, item2 = item2, item1
    #         self.inventory.pouch.append(item1)
    #         current_location.item = item2
    #         print(f'You swapped {item2.__dict__["description"]} for a {item1.__dict__["description"]}!')
    #     else:
    #         print('You can\'t swap that')


