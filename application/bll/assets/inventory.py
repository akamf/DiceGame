class Inventory:
    def __init__(self):
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
        Method to check whether or not the inventory is full
        :param item: Item instance, the item to pick up
        :param hand: str, the hand to pick up with
        :return: bool
        """
        if item.__dict__['storage'] == 'pouch' and len(self.pouch) >= self.max_limit:
            print(f'Your pouch is full.\n'
                  f'You can\'t pick up {item["description"]} before you drop something from your pouch!')
            return True
        elif item.__dict__['storage'] == 'hand' and hand:
            if self.left_hand and self.right_hand:
                print(f'Your hands are full.\n'
                      f'You can\'t pick up {item.__dict__["description"]} before you drop something from your hands!')
                return True
            match hand:
                case 'left' | 'left hand':
                    if self.left_hand:
                        print(f'Your left hand is full!\nBut you can pick the {item.__dict__["description"]} '
                              f'up with your right hand or drop the item in your left hand.')
                        return True
                case 'right' | 'right hand':
                    if self.right_hand:
                        print(f'Your right hand is full!\nBut you can pick the {item.__dict__["description"]} '
                              f'up with your left hand or drop the item in your right hand.')
                        return True
                case _:
                    print('Invalid command')
                    return True
        return False

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

    def process_item_pickup(self, item, current_location, chest=None):
        """
        Process the pickup method
        :param item: Item instance, the item to pick up
        :param current_location: Cell instance, the players current location
        :param chest: Item instance
        :return None
        """
        if 'get' not in item.__dict__['actions']:
            print(f'It seems impossible to pick up the {item.__dict__["description"]}')

        elif item.__dict__['storage'] == 'pouch' and not self.inventory_full(item):
            print(f'You pick up the {item.__dict__["description"]}!')
            self.pouch.append(item)

            if chest:
                chest.__dict__['contains'].remove(item)
            else:
                current_location.item = None
                current_location.got_item = False

        elif item.__dict__['storage'] == 'hand':
            hand = input(f'Which hand do you want to pick up the {item.__dict__["description"]} with?\n>> ')

            if not self.inventory_full(item, hand):
                print(f'You pick up the {item.__dict__["description"]} in your {hand} hand!')
                if hand == 'right' or hand == 'right hand':
                    self.right_hand = item
                elif hand == 'left' or hand == 'left hand':
                    self.left_hand = item

                if chest:
                    chest.__dict__['contains'].remove(item)
                else:
                    current_location.item = None
                    current_location.got_item = False
        else:
            print('Your inventory is full!')

    def print_inventory(self):
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
                for item in sorted(self.pouch, key=lambda i: i.__dict__['description']):
                    print(f'* {item.__dict__["description"]}')
                print()

            if self.right_hand:
                print(f'Right hand:  {self.right_hand.__dict__["description"]}')
            else:
                print(f'Right hand:  {self.right_hand}')

            if self.left_hand:
                print(f'Left hand:  {self.left_hand.__dict__["description"]}')
            else:
                print(f'Left hand:  {self.left_hand}')

    def remove_pouch_item(self, label: str):
        """
        Remove an item from the pouch, if it's a consumable item (Health potion etc.)
        :param label: str, the item label
        return: None
        """
        for item in self.pouch:
            if label == item.__dict__['label']:
                self.pouch.remove(item)
