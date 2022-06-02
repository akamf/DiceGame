class Inventory:
    def __init__(self) -> None:
        self.pouch = []
        self.max_limit = 3
        self.right_hand = None
        self.left_hand = None

    def get_item_from_pouch(self, label: str) -> str:
        for item in self.pouch:
            if label == item['label']:
                return item['description']

    def inventory_full(self, item, hand=None) -> bool:
        """
        Method to check whether the inventory is full
        :param item: Item instance, the item to pick up
        :param hand: str, the hand to pick up with
        :return: bool
        """
        if item['storage'] == 'pouch' and len(self.pouch) >= self.max_limit:
            print(f'Your pouch is full.\n'
                  f'You can\'t pick up {item["description"]} before you drop something from your pouch!')
            return True
        elif item['storage'] == 'hand' and hand:
            if self.left_hand and self.right_hand:
                print(f'Your hands are full.\n'
                      f'You can\'t pick up {item["description"]} before you drop something from your hands!')
                return True
            match hand:
                case 'left' | 'left hand':
                    if self.left_hand:
                        print(f'Your left hand is full!\nBut you can pick the {item["description"]} '
                              f'up with your right hand or drop the item in your left hand.')
                        return True
                case 'right' | 'right hand':
                    if self.right_hand:
                        print(f'Your right hand is full!\nBut you can pick the {item["description"]} '
                              f'up with your left hand or drop the item in your right hand.')
                        return True
                case _:
                    print('Invalid command')
                    return True
        return False

    def pick_up_item(self, label: str, current_location, chest=None) -> None:
        """
        Pick up an item from the current location, or from a chest, and append it to the players inventory
        :param label: str, label of the item to get
        :param current_location: Cell instance, the players current location
        :param chest: Item instance, chest to get an item from
        :return None
        """
        if chest:
            for item in chest.__dict__['contains']:
                if label == item.__dict__['label']:
                    self.process_item_pickup(item.__dict__, current_location, chest)
                else:
                    print(f'There is no {label} in the chest')

        elif not current_location.item or label != current_location.item.__dict__['label']:
            print(f'There is no {label} here')

        elif label == current_location.item.__dict__['label']:
            self.process_item_pickup(current_location.item.__dict__, current_location)

    def drop_item(self, label: str, current_location) -> None:
        """
        Drop an item from the players inventory
        :param label: str, the label of the item to drop
        :param current_location: Cell instance, the players current location
        :return None
        """
        found_item = None
        if not current_location.got_item:
            for item in self.pouch:
                if label == item.__dict__['label']:
                    found_item = item
                    break
        else:
            print(f'This space isn\'t empty! You can\'t drop the {label}')

        if found_item and 'drop' in found_item.__dict__['actions']:
            print(f'You drop the {label}')
            self.pouch.remove(found_item)
            current_location.item = found_item
            current_location.got_item = True
        else:
            print(f'You can\'t drop the {label}, you should have thought of this earlier')

    def item_in_inventory(self, label: str) -> bool:
        """
        Search in player inventory for a certain item
        :param label: str, the label of the item to search for
        :return: bool
        """
        if self.right_hand:
            if label == self.right_hand.__dict__['label']\
                    or label == self.right_hand.__dict__['description']:
                return True

        if self.left_hand:
            if label == self.left_hand.__dict__['label']\
                    or label == self.left_hand.__dict__['description']:
                return True

        for item in self.pouch:
            if label == item.__dict__['label'] or label == item.__dict__['description']:
                return True

        return False

    def process_item_pickup(self, item, current_location, chest=None) -> None:
        """
        Process the pickup method
        :param item: Item instance, the item to pick up
        :param current_location: Cell instance, the players current location
        :param chest: Item instance
        :return None
        """
        if 'get' not in item['actions']:
            print(f'It seems impossible to pick up the {item["description"]}')

        elif item['storage'] == 'pouch' and not self.inventory_full(item):
            print(f'You pick up the {item["description"]}!')
            self.pouch.append(item)

            if chest:
                chest['contains'].remove(item)
            else:
                current_location.item = None
                current_location.got_item = False

        elif item['storage'] == 'hand':
            hand = input(f'Which hand do you want to pick up the {item["description"]} with?\n>> ')

            if not self.inventory_full(item, hand):
                print(f'You pick up the {item["description"]} in your {hand} hand!')
                if hand == 'right' or hand == 'right hand':
                    self.right_hand = item
                elif hand == 'left' or hand == 'left hand':
                    self.left_hand = item

                if chest:
                    chest['contains'].remove(item)
                else:
                    current_location.item = None
                    current_location.got_item = False
        else:
            print('Your inventory is full!')

    def print_inventory(self) -> None:
        """
        Display the players inventory
        return: None
        """
        if len(self.pouch) == 0 and not self.right_hand and not self.left_hand:
            print('Yor inventory is empty')
        else:
            print(f'\tINVENTORY')
            if len(self.pouch) == 0:
                print('Your pouch is empty\n')
            else:
                for item in sorted(self.pouch, key=lambda i: i['description']):
                    print(f'* {item["description"]}')
                print()

            if self.right_hand:
                print(f'Right hand:  {self.right_hand["description"]}')
            else:
                print(f'Right hand:  {self.right_hand}')

            if self.left_hand:
                print(f'Left hand:  {self.left_hand["description"]}')
            else:
                print(f'Left hand:  {self.left_hand}')

    def remove_pouch_item(self, label: str) -> None:
        """
        Remove an item from the pouch, if it's a consumable item (Health potion etc.)
        :param label: str, the item label
        return: None
        """
        for item in self.pouch:
            if label == item['label']:
                self.pouch.remove(item)

