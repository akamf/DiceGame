class Inventory:
    def __init__(self):
        self.inventory = []

    def get_inventory_item(self, label: str):
        for item in self.inventory:
            if label == item['label']:
                return item['description']
