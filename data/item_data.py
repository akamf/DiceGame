import random
from assets.item import Item

usable_items = [
    {
        'label': 'lantern',
        'description': 'burning lantern',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'It has a good bit of wick left.\n'
                 'This lantern can light up the surroundings and you can see where to go.\n',
        'storage': 'hand',
        'battle': False,
        'position': None
    },
    {
        'label': 'dice',
        'description': 'dice',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'It has pictures of swords and shields instead of numbers.\n'
                 'With this you can roll an extra dice in battle situations.\n',
        'storage': 'pouch',
        'battle': False,
        'position': None
    },
    {
        'label': 'potion',
        'description': 'health potion',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'This glass bottle has a purple liquid inside, a health potion.\n'
                 'This will provide 10 health points when you drink it.\n',
        'storage': 'pouch',
        'battle': True,
        'position': None
    },
    {
        'label': 'ring',
        'description': 'golden ring',
        'actions': ['get', 'check', 'investigate'],
        'bonus': 'The ring emits a dark smoke.\nIt\'s very unclear what will happento the bearer of this ring. '
                 'But there is only one way to find out, right?\n',
        'storage': 'hand',
        'battle': False,
        'position': None
    },
    {
        'label': 'pill',
        'description': 'dark pill',
        'actions': ['get', 'check', 'investigate'],
        'bonus': 'It reeks of something rotten.\nIt may come in handy in a battle situation.\n',
        'storage': 'pouch',
        'battle': True,
        'position': None
    },
]

weapons_and_armors = [
    {
        'label': 'sword',
        'description': 'two-handed sword',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'This well crafted two-handed sword, with a dragon engraved on it\'s blade'
                 'It will give you double attack points. But it needs both your hands tho, '
                 'and can therefore not be paired with a shield!',
        'storage': 'hand',
        'position': None
    },
    {
        'label': 'shield',
        'description': 'old wooden shield',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'It\'s a wolf painted on it.\nThis shield will get you extra defend points, with a minimum of 1',
        'storage': 'hand',
        'position': None
    },
    {
        'label': 'knife',
        'description': 'short knife',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'This knife has a venomous tip.\n'
                 'It will poison your enemy and make it lose 1 health point per battle round',
        'storage': 'hand',
        'position': None
    },
    {
        'label': 'sword',
        'description': 'short sword',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'It\'s a rusty old sword.\nThe chance of a critical hit doubles with this sword',
        'storage': 'hand',
        'position': None
    },
    {
        'label': 'axe',
        'description': 'tree cutter\'s axe',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'It\'s an axe with a wooden shaft.\n'
                 'This axe will crack open any enemy armor, and deal damage directly on the enemy',
        'storage': 'hand',
        'position': None
    },
]

key_items = [

    {
        'label': 'key',
        'description': 'golden key',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'There is a tiny text engraved on it: "OSTIUM IN LONGITUDINEM X ET Y"\n'
                       'I wonder what that means..? It looks important tho!\n',
        'storage': 'pouch',
        'position': None
    },
    {
        'label': 'key',
        'description': 'rusty key',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'This key can come in handy, if you ever need to unlock things.\n',
        'storage': 'pouch',
        'position': None
    },
    {
        'label': 'door',
        'description': 'big hardwood door',
        'actions': ['unlock', 'check', 'investigate'],
        'bonus': 'It\'s locked!\nYou need something to unlock it.',
        'requirements': 'golden key',
        'position': None
    },
    {
        'label': 'chest',
        'description': 'large chest',
        'actions': ['open', 'close', 'check', 'investigate'],
        'bonus': 'It\'s locked!\nYou need a key to unlock it.',
        'open': False,
        'contains': [Item(**random.choice(weapons_and_armors))],
        'requirements': 'rusty key',
        'position': None
    }
]


