from src.db import db
from src.db.model import Document


class EnemyCollection(Document):
    collection = db.enemies


class ItemCollection(Document):
    collection = db.items


class SavedGame(Document):
    collection = db.savedgames


class HighScore(Document):
    collection = db.highscores


class Weapon(Document):
    collection = db.weapons

