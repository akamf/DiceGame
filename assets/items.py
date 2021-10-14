import random
from data.item_data import usable_items


class Items:
    def __init__(self, **item):
        self.set_item_position()
        self.__dict__ = item

    @staticmethod
    def set_item_position():
        positions = []
        for i in range(len(usable_items)):
            (x, y) = (random.randrange(0, 5), random.randrange(0, 5))
            while (x, y) in positions:
                (x, y) = (random.randrange(0, 5), random.randrange(0, 5))
            positions.append((x, y))

        cnt = 0
        for item in usable_items:
            item['position'] = positions[cnt]
            cnt += 1
