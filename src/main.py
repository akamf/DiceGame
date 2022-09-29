from src.db import init_db
from dotenv import load_dotenv
from config import DEVELOPMENT


if __name__ == '__main__':
    load_dotenv()
    init_db()

    if not DEVELOPMENT:
        from src.assets.game import Game
        Game().run()

    else:
        from test_environ import TestMaze
        game = TestMaze()
        game.run()
