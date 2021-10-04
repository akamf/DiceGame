import random


def roll_dice(dice: list) -> str:
    return dice[random.randrange(0, 6)]


def main():
    player1 = []
    player2 = []

    # Shield = 1Dp, double shield = 2Dp etc. Sword = 1Ap, double sword = 2Ap etc. Draw card = draw bonus card
    dice_defender = ["shield", "double shield", "double shield", "triple shield", "sword", "double sword"]
    dice_invader = ["sword", "double sword", "triple sword", "triple sword", "draw card", "draw card"]
    cards = {"battering ram", "fortified wall", "the plague"}

    num_of_dices = 3
    for i in range(3):

        results = []
        for _ in range(num_of_dices):
            results.append(roll_dice(dice_defender))

        if len(results) == 3:
            keep = input(f"1. {results[0]}\n2. {results[1]}\n3. {results[2]}\n\nDo you want to keep any? ")
        elif len(results) == 2:
            keep = input(f"1. {results[0]}\n2. {results[1]}\n\nDo you want to keep any? ")
        elif len(results) == 1:
            keep = input(f"1. {results[0]}\n\nDo you want to keep any? ")

        if keep.lower() == "y":
            num = input("Enter the number(s) of the dices to keep: ")
            num = num.split()
            if len(num) > 1:
                for j in range(len(num)):
                    player1.append(results[int(num[j])])
                num_of_dices -= len(player1)
            else:
                player1.append(results[0])

        if len(player1) == 3 or num_of_dices == 0:
            break

    for j in player1:
        print(j)


if __name__ == "__main__":
    main()
