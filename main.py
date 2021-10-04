from game import Game


def main():
    game = Game()
    dice_result(player1, 3)
    dice_result(player2, 2)
    print("Defender dices: ")
    for j in player1:
        print(j)
    print("Invader dices: ")
    for j in player2:
        print(j)


if __name__ == "__main__":
    main()
