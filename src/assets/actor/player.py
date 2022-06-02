import random
from src.assets.actor import Actor
from src.assets.inventory import Inventory
from src.assets.map.maze import DIRECTIONS


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
        self.alive = True

    def move(self, direction: str) -> None:
        """
        Update player position, based on a constant value from DIRECTIONS
        :param direction: str,
        :return None
        """
        for value in DIRECTIONS:
            if value[0] == direction:
                self.position = value[1]

    def pick_up_item(self, label: str, current_location, chest=None) -> None:
        """
        Pick up an item from the current location, or from a chest, and append it to the players inventory
        :param label: str, label of the item to get
        :param current_location: Cell instance, the players current location
        :param chest: Item instance, chest to get an item from
        :return None
        """
        if chest:
            for item in chest.__dict__['contains']:
                if label == item.__dict__['label']:
                    self.inventory.process_item_pickup(item.__dict__, current_location, chest)
                else:
                    print(f'There is no {label} in the chest')

        elif not current_location.item or label != current_location.item.__dict__['label']:
            print(f'There is no {label} here')

        elif label == current_location.item.__dict__['label']:
            self.inventory.process_item_pickup(current_location.item.__dict__, current_location)

    def drop_item(self, label: str, current_location) -> None:
        """
        Drop an item from the players inventory
        :param label: str, the label of the item to drop
        :param current_location: Cell instance, the players current location
        :return None
        """
        found_item = None
        if not current_location.got_item:
            for item in self.inventory.pouch:
                if label == item.__dict__['label']:
                    found_item = item
                    break
        else:
            print(f'This space isn\'t empty! You can\'t drop the {label}')

        if found_item and 'drop' in found_item.__dict__['actions']:
            print(f'You drop the {label}')
            self.inventory.pouch.remove(found_item)
            current_location.item = found_item
            current_location.got_item = True
        else:
            print(f'You can\'t drop the {label}, you should have thought of this earlier')

    def use_battle_item(self, label: str, enemy):
        """
        Method to use items in a battle situation
        :param label: str, the label of the item
        :param enemy: Enemy instance, current enemy
        :return: None
        """
        if self.inventory.item_in_inventory(label):
            match label:
                case 'potion':
                    print(f'You drank the health potion and gained 10 health points!')
                    self.health_points += 10
                    self.inventory.remove_pouch_item(label)

                case 'pill':
                    effect = random.choice(['cursed', 'lucky'])
                    print(f'You consume the dark pill and you\'re {effect}!')
                    self.inventory.remove_pouch_item(label)

                    match effect:
                        case 'lucky':
                            print('You gain 15 health points!')
                            self.health_points += 15
                        case 'cursed':
                            print(f'You faint for a moment and the {enemy.name} takes advantage!\n'
                                  f'You lose {enemy.attack_points} health points!')
                            self.health_points -= enemy.attack_points

    def update_player_stats(self):
        """
        Update player stats when the level is completed
        :return: None
        """
        self.position = (0, 0)
        self.inventory.pouch.clear()
        self.health_points += 10
        self.level += 1
        self.score += (50 * self.level)
