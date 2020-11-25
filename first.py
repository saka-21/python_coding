s = 'fasdjfa'
print(s.capitalize())

class Person():
    def __init__(self, name):
        self.name = name
        print(self.name)
    def say_something(self):
        print('hello')

person = Person('Mike')
person.say_something()
