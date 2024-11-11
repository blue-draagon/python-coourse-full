# starting with oop

class PlayerCharacter(object):
    """ This class is a representation of player """

    country = 'Senegal'  # class object attribute

    def __init__(self, name):
        self.name = name  # attribute

    def run(self):
        print(f'{self.name} is running')

    def walk(self):
        print(f'{self.name} is walking')


toto = PlayerCharacter('Toto')
print(toto)
toto.run()

arno = PlayerCharacter('Arno')
arno.walk()
arno.age = 10  # outclass attribute
print(arno.age)

# getting class info
# help(PlayerCharacter)

print(arno.country)
arno.country = 'Gambia'
print(arno.country)
print(toto.country)
print(PlayerCharacter.country)
