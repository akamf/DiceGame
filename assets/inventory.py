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
        Check whether or not the inventory is full.
        The pouch can't hold more than it's max limit and the hands can only contain one item each.
        :param hand: The hand the player wants to pick up the item with
        :param item:
        :return: True if the pouch or the hands are full, else False
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
                        print('Your left hand is full, but you can pick it up with your right hand or drop the item in your left.')
                        return True
                case 'right' | 'right hand':
                    if self.right_hand:
                        print('Your right hand is full, but you can pick it up with your left hand or drop the item from your right.')
                        return True
                case _:
                    print('Invalid command')
                    return True
        return False

    def item_in_inventory(self, label: str) -> bool:
        """
        Search in player inventory for a certain item
        :param label: The label for the item to search for
        :return: True if the item is found, else False
        """
        if self.right_hand or self.left_hand:
            if label == self.right_hand.__dict__['label'] or label == self.right_hand.__dict__['description'] or\
                    label == self.left_hand.__dict__['label'] or label == self.left_hand.__dict__['description']:
                match label:
                    case 'lantern':
                        return True
                    case 'sword':
                        return True
                    case 'shield':
                        return True

        for item in self.pouch:
            if label == item.__dict__['label'] or label == item.__dict__['description']:
                match label:
                    case 'golden key':
                        return True
                    case 'rusty key':
                        return True
                    case 'dice':
                        return True
        return False

    def process_item_pickup(self, item, current_location, chest=None):
        if 'get' not in item.__dict__['actions']:
            print(f'It seems impossible to pick up the {item.__dict__["description"]}')

        elif item.__dict__['storage'] == 'pouch' and not self.inventory_full(item):
            print(f'You pick up the {item.__dict__["description"]}!')
            self.pouch.append(item)

            if chest:
                chest['contains'].remove(item)
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
                    chest['contains'].remove(item)
                else:
                    current_location.item = None
                    current_location.got_item = False

    def print_inventory(self):
        """Display the players inventory"""
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
                print(f'Right hand:  None')

            if self.left_hand:
                print(f'Left hand:  {self.left_hand.__dict__["description"]}')
            else:
                print(f'Left hand:  None')

