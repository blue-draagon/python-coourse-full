# starting with oop

class PlayerCharacter(object):
    """ This class is a representation of player """

    country = 'Senegal'

    def __init__(self):
        print('initializing a new PlayerCharacter object')


player = PlayerCharacter()
# the __init__ method is call when creating new object
