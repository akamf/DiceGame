from os import environ
from pymongo import MongoClient

client = None
db = None


def add_db_user(mongo_client: MongoClient, username: str, password: str, database: str) -> None:
    mongo_client.DiceGameDatabase.command(
        'createUser', username,
        pwd=password,
        roles=[{'role': 'readWrite', 'init_db': database}]
    )


def init_db():
    """
    Set environment variables for the database in .env file in the project root
    folder.
    :return: None
    """
    global client, db

    database = environ.get('DB_NAME')
    username = environ.get('DB_USER')
    password = environ.get('DB_PASSWORD')
    host = environ.get('DB_HOST')
    port = environ.get('DB_PORT')

    client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
    db = client[database]

    # add_db_user(client, username, password, database)

