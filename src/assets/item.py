class Item:
    def __init__(self, **item) -> None:
        self.__dict__ = item

    def __setattr__(self, key, value) -> None:
        object.__setattr__(self, key, value)
