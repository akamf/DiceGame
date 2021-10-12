import random

# This is a first test to set the items in a random position inside the maze
# I haven't decided where to put the function, so I just test it from here

# def set_item_position():
#     for item in usable_items:
#         x = random.randrange(0, 5)
#         y = random.randrange(0, 5)
#         item['position'] = (x, y)


usable_items = [
    {
        'id': 1,
        'name': 'lantern',
        'description': 'A burning lantern with a good bit of wick left',
        'actions': ['get', 'drop', 'look'],
        'bonus': 'the lantern lights up the dark corridor and you can finally see your surroundings!',
        'position': (0, 1)
    },
    {
        'id': 2,
        'name': 'two-handed sword',
        'description': 'A well crafted sword. A dragon is seen on it\'s blade',
        'actions': ['get', 'drop', 'look'],
        'bonus': 'you\'ll get double attack points with this. It can\'t be paired with a shield tho!',
        'position': (1, 4)
    },
    {
        'id': 3,
        'name': 'old wooden shield',
        'description': 'A round wooden shield. It\'s a wolf painted on it',
        'actions': ['get', 'drop', 'look'],
        'bonus': 'this shield will get you extra defend points, with a minimum of 1',
        'position': (2, 1)
    },
    {
        'id': 4,
        'name': 'golden key',
        'description': 'A golden key with small text engraved: "OSTIUM IN LONGITUDINEM X ET Y"\n'
                       'I wonder what that means?',
        'actions': ['get', 'drop', 'look'],
        'bonus': 'it looks important tho...',
        'position': (3, 3)
    }
]
