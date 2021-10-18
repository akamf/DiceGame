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
        if len(self.inventory) >= self.max_limit:
            print('Your inventory is full.')
            return True
        return False
