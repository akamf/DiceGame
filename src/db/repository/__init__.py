from src.db.model.collections import *


def add_enemy(enemy) -> None:
    EnemyCollection(enemy).save()


def get_enemy(**kwargs) -> dict:
    return EnemyCollection.find(**kwargs).first_or_none()


def get_all_enemies() -> list[dict]:
    return EnemyCollection.all()


def update_enemy(enemy) -> None:
    EnemyCollection.save(enemy)


def add_item(item) -> None:
    ItemCollection(item).save()


def get_item(**kwargs) -> dict:
    return ItemCollection.find(**kwargs).first_or_none()


def get_all_items() -> list[dict]:
    return ItemCollection.all()


def update_item(item) -> None:
    ItemCollection.save(item)
