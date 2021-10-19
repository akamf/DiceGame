import random

key_items = [
    {
        'label': 'lantern',
        'description': 'burning lantern',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'It has a good bit of wick left.\n'
                 'This lantern can light up the surroundings and you can see where to go.',
        'position': None
    },
    {
        'label': 'key',
        'description': 'golden key',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'There is a tiny text engraved on it: "OSTIUM IN LONGITUDINEM X ET Y"\n'
                       'I wonder what that means..? It looks important tho!',
        'position': None
    },
    {
        'label': 'key',
        'description': 'rusty key',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'This key can come in handy, if you ever need to unlock things.',
        'position': None
    },
    {
        'label': 'dice',
        'description': 'dice',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'It has pictures of swords and shields instead of numbers.\n'
                 'With this you can roll an extra dice in battle situations.',
        'position': None
    },
]

weapons_and_armors = [
    {
        'label': 'sword',
        'description': 'long sword',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'This well crafted two-handed sword, with a dragon engraved on it\'s blade'
                 'It will give you double attack points. But it needs both your hands tho, '
                 'and can therefore not be paired with a shield!',
        'position': None
    },
    {
        'label': 'shield',
        'description': 'old wooden shield',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'It\'s a wolf painted on it.\nThis shield will get you extra defend points, with a minimum of 1',
        'position': None
    }
]

enviroment_items = [
    {
        'label': 'door',
        'description': 'big hardwood door',
        'actions': ['unlock', 'check', 'investigate'],
        'bonus': 'It\'s locked!\nYou need something to unlock it.',
        'requirements': 'golden key',
        'position': (4, 4)
    },
    {
        'label': 'chest',
        'description': 'large chest',
        'actions': ['open', 'close', 'check', 'investigate'],
        'bonus': 'It\'s locked!\nYou need a key to unlock it.',
        'open': False,
        'contains': [random.choice(weapons_and_armors)['description']],
        'requirements': 'rusty key',
        'position': (1, 1)
    }
]

