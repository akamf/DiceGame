from src.database.repositories import enemy_repository


def add_enemy(et: str, n: str, ap: int, dp: int, hp: int, l: int) -> None:
    """
    Add enemy to db
    :param et: str, enemy type
    :param n: str, enemy name
    :param ap: int, attack points
    :param dp: int, defend points
    :param hp: int, health points
    :param l: int, level
    :return: None
    """
    enemy = {
        'type': et,
        'name': n,
        'attack_points': ap,
        'defend_points': dp,
        'health_points': hp,
        'level': l
    }

    enemy_repository.add_enemy(enemy)


def get_enemy(**kwargs):
    return enemy_repository.get_enemy(**kwargs)


def get_all_enemies():
    return enemy_repository.get_all_enemies()

