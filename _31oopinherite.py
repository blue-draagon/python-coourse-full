class Person:
    def walk(self):
        print('Person is walking')


# an Student is an spécifique person
class Student(Person):
    pass


# an ItStudent is an spécifique student
class ITStudent(Student):
    pass


person1 = Person()
person1.walk()
student1 = Student()
student1.walk()
student2 = ITStudent()
student2.walk()


#
class User:
    def login(self):
        print('user login')

    def attack(self):
        print('user trying to attack')


class Wizard(User):
    def __init__(self, name, power) -> None:
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows) -> None:
        self.name = name
        self.arrows = arrows

    def attack(self):
        User.attack(self)
        self.arrows = self.arrows - 1
        print('attacking with arows : arows left : {self.arrows}')


wizard = Wizard('Merlin', 50)
wizard.login()
wizard.attack()
archer = Archer('Robin', 150)
archer.login()
archer.attack()

# checking instance of class
print(isinstance(wizard, Wizard))
print(isinstance(wizard, User))
print(isinstance(wizard, Archer))
print(isinstance(wizard, object))
# check subclass
print(issubclass(Wizard, object))
print(issubclass(Wizard, Archer))
print(issubclass(Archer, User))

# all class inherite to object base class

# polymorphisme
# diffenrent actions of same called method
for char in [wizard, archer]:
    char.attack()


# multiple inheritance
class User:
    def login(self):
        print('user login')


class Wizard(User):
    def __init__(self, name, power) -> None:
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows) -> None:
        self.name = name
        self.arrows = arrows

    def check_arows(self):
        print(f'{self.arrows} arrows remining')

    def run(self):
        print(f'{self.name} is running')


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows) -> None:
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb = Hybrid('borgie', 50, 50)
hb.attack()
hb.run()
hb.check_arows()
