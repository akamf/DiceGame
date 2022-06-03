from src.assets.actor import Actor
from src.assets.inventory import Inventory
from src.assets.map.maze import DIRECTIONS


class Dice:
    def __init__(self) -> None:
        self.dice = [
            'sword',
            'sword',
            'double sword',
            'double sword',
            'shield',
            'double shield'
        ]

    def __getitem__(self, dice_face):
        return self.dice[dice_face]

    def roll(self) -> str:
        """
        Method to simulate the dices results
        :return: list
        """
        import random

        return random.choice(self.dice)


class Player(Actor):
    def __init__(self) -> None:
        super().__init__(
            name='player',
            position=(0, 0),
            attack_points=0,
            defend_points=0,
            health_points=20,
            level=1
        )
        self.score = 0
        self.inventory = Inventory()
        self.dices = [Dice(), Dice(), Dice(), Dice(), Dice(), Dice(), Dice(), Dice()]
        self.alive = True

    def move(self, direction: str) -> None:
        """
        Move the player in a valid direction
        :param direction: str,
        :return None
        """
        for value in DIRECTIONS:
            if value[0] == direction:
                self.position = value[1]

    @staticmethod
    def in_battle(current_location) -> bool:
        """
        Method to check whether the player is in a battle situation or not
        :param current_location: Cell instance, the players current location
        :return: bool
        """
        return True if current_location.enemy else False

    def update_stats(self) -> None:
        """
        Update player stats and clear the pouch when the level is completed or reset the stats if the player dies
        :return: None
        """
        self.position = (0, 0)
        if self.alive:
            self.inventory.pouch.clear()
            self.health_points += 10
            self.level += 1
            self.score += (50 * self.level)
        else:
            self.inventory = Inventory()
            self.health_points = 20
            self.level = 1
            self.score = 0

