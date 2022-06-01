from src.database.init_db import init_db
from src.game import Game
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    init_db()
    Game().run()
