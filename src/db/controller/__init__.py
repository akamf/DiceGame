import db.repository as repo


def get_enemy(**kwargs):
    return repo.get_enemy(**kwargs).__dict__


def get_all_enemies():
    enemies = [enemy.__dict__ for enemy in repo.get_all_enemies()]
    for enemy in enemies:
        del enemy['_id']

    return enemies


def get_all_enemies_from_type(t: str):
    return [enemy for enemy in get_all_enemies() if enemy['type'] == t]


def get_item(**kwargs):
    return repo.get_item(**kwargs).__dict__


def get_all_items():
    items = [item.__dict__ for item in repo.get_all_items()]
    for item in items:
        del item['_id']

    return items


def get_all_items_from_type(t: str):
    return [item for item in get_all_items() if item['type'] == t]
