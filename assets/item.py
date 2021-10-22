import random

from data.item_data import key_items, environment_items, weapons_and_armors


class Item:
    def __init__(self, **item):
        self.__dict__ = item

    def __setattr__(self, key, value):
        print(key, value)
        object.__setattr__(self, key, value)

    @staticmethod
    def get_key_item(label: str) -> dict:
        for item in key_items:
            if label == item['label'] or label == item['description']:
                return item

    @staticmethod
    def get_weapon_or_armor(label: str) -> dict:
        for item in weapons_and_armors:
            if label == item['label'] or label == item['description']:
                return item

    @staticmethod
    def get_environment_item(label: str) -> dict:
        for item in environment_items:
            if label == item['label'] or label == item['description']:
                return item


