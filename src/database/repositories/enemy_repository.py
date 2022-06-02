from src.database.models import EnemyCollection


def add_enemy(enemy) -> None:
    EnemyCollection(enemy).save()


def update_enemy(enemy) -> None:
    EnemyCollection.save(enemy)


def get_enemy(**kwargs) -> EnemyCollection:
    return EnemyCollection.find(**kwargs).first_or_none()


def get_all_enemies() -> EnemyCollection:
    return EnemyCollection.all()

