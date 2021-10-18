import random

from data.item_data import key_items, enviroment_items


class Items:
    def __init__(self, **item):
        self.set_item_position()
        self.__dict__ = item

    @staticmethod
    def set_item_position():
        positions = []
        for i in range(len(key_items)):
            (x, y) = (random.randrange(0, 5), random.randrange(0, 5))
            while (x, y) in positions or (x, y) == (4, 4):
                (x, y) = (random.randrange(0, 5), random.randrange(0, 5))
            positions.append((x, y))

        cnt = 0
        for item in key_items:
            item['position'] = positions[cnt]
            cnt += 1

