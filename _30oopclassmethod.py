# starting with oop

class Student(object):
    """ This class is a representation of player """

    country = 'Senegal'

    def __init__(self, name='Toto', age=12):
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name} is walking')

    @classmethod
    def change_country(cls, name):
        cls.country = name

    @classmethod
    def with_age(cls, age):
        return cls(age=age)

    @staticmethod
    def countries():
        print('Countries list : Senegal:Mali:Burkina Faso: Niger')

# self is reference to object
# cls is reference to class


toto = Student()
print(toto.country)
toto.change_country('Gambia')
print(toto.country)
arno = Student()
print(arno.country)
# class method update the value of class attribute

# instanciate object with classmethod
modou = Student.with_age(18)
print(modou.age)

# static method is use when action do not
# have direct relation with the class
Student.countries()


# encapsulation
# grouping variables and actions in the same object

# abstraction
# using attributes and method without know what happen in
# the background

# underscore mean private
# __init__ build in python

# overriding private our dunded is a bad practice
