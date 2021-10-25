class Item:
    def __init__(self, **item):
        self.__dict__ = item

    def __setattr__(self, key, value):
        print(key, value)
        object.__setattr__(self, key, value)
