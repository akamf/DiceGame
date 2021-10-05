from game import Game


def main():
    game = Game()
    game.dice_result()
    game.process_saved_dices()
    game.update_active_player()
    game.dice_result()
    game.process_saved_dices()
    game.print_result()
    game.win()


if __name__ == "__main__":
    main()
