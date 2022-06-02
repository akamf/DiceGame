class Item:
    def __init__(self, **item) -> None:
        self.__dict__ = item

        if 'type' in self.__dict__:
            del self.__dict__['type']

    def __setattr__(self, key, value) -> None:
        object.__setattr__(self, key, value)
