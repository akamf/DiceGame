
key_items = [
    {
        'label': 'lantern',
        'description': 'a burning lantern with a good bit of wick left',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'This lantern can light up the surroundings and you can see where to go.',
        'position': None
    },
    {
        'label': 'key',
        'description': 'A golden key with small text engraved: "OSTIUM IN LONGITUDINEM X ET Y"\n'
                       'I wonder what that means?',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'it looks important',
        'position': None
    }
]

enviroment_items = [
    {
        'label': 'door',
        'description': '',
        'actions': ['unlock'],
        'requirements': 'key',
        'position': (4, 4)
    },
    {
        'label': 'chest',
        'description': '',
        'actions': ['open', 'close', 'check'],
        'open': False,
        'contains': ['sword' or 'shield'],
        'position': (1, 1)
    }
]

weapons_and_armors = [
    {
        'label': 'sword',
        'description': 'a long sword. A dragon is seen on it\'s blade',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'This well crafted two-handed sword will give you double attack points. '
                 'It needs both your hands tho, and can therefore not be paired with a shield!',
        'position': None
    },
    {
        'label': 'shield',
        'description': 'an old wooden shield. It\'s a wolf painted on it',
        'actions': ['get', 'drop', 'check', 'investigate'],
        'bonus': 'this shield will get you extra defend points, with a minimum of 1',
        'position': None
    }
]