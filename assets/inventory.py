class Inventory:
    def __init__(self):
        self.inventory = [
            {
                'label': 'key',
                'description': 'rusty key',
                'actions': ['get', 'drop', 'check', 'investigate'],
                'bonus': 'This key can come in handy, if you ever need to unlock things.',
                'position': None
            }
        ]
        self.max_limit = 3
        self.right_hand = None
        self.left_hand = None

    def get_inventory_item(self, label: str) -> str:
        for item in self.inventory:
            if label == item['label']:
                return item['description']

    def inventory_full(self) -> bool:
        """Check whether or not the inventory is full"""
        if len(self.inventory) >= self.max_limit:
            print('Your inventory is full.')
            return True
        return False

    def item_in_inventory(self, label: str) -> bool:
        """
        Search in player inventory for a certain item
        :param label: The label for the item to search for
        :return: True if the item is found, else False
        """
        for item in self.inventory:
            if label == item['label'] or label == item['description']:
                match label:
                    case 'lantern':
                        return True
                    case 'sword':
                        return True
                    case 'shield':
                        return True
                    case 'golden key':
                        return True
                    case 'rusty key':
                        return True
        return False

    def process_item_pickup(self, item):
        if 'get' not in item['actions']:
            print(f'It seems impossible to pick up the {item["description"]}')
        elif not self.inventory_full():
            print(f'You pick up the {item["description"]}!')
            self.inventory.append(item)
        else:
            print(f'You can\'t pick up {item["description"]} before you drop something from your inventory')

    def print_inventory(self):
        """Display the players inventory"""
        if len(self.inventory) == 0:
            print('Yor inventory is empty')
        else:
            print(f'\tINVENTORY')
            for item in sorted(self.inventory, key=lambda i: i['description']):
                print(f'* {item["description"]}')
