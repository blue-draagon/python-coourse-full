class User:
    def __init__(self, email: str) -> None:
        self.email = email

    def login(self):
        print('user login')

    def attack(self):
        print('user trying to attack')


class Wizard(User):
    def __init__(self, email: str,  name: str, power: int) -> None:
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


# python typing is available on python 3.5
# the super keyword refer to the method
merlin = Wizard('merlin@gmail.com', 'Merlin', 60)
print(merlin.email)


# introspection
print(dir(merlin))
