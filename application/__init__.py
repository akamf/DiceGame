from dotenv import load_dotenv
from application.game import Game


if __name__ == '__main__':
    load_dotenv()
    game = Game()
    game.run()
