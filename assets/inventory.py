class Inventory:
    def __init__(self):
        self.inventory = []
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

    def item_in_inventory(self, item_label: str) -> bool:
        """
        Search in player inventory for a certain item
        :param item_label: The label for the item to search for
        :return: True if the item is found, else False
        """
        for item in self.inventory:
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

    def print_inventory(self):
        """Display the players inventory"""
        if len(self.inventory) == 0:
            print('Yor inventory is empty')
        else:
            print(f'\tINVENTORY')
            for item in sorted(self.inventory, key=lambda i: i['label']):
                print(f'* {item["label"]}')
