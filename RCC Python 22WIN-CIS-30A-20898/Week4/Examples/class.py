#Classes
class Person:
    def __init__(self, name, age): #always use 'self' so we can self-address name, age
        self.name = name
        self.age = age

p1 = Person("Jane",30)

print(p1.name)
print(p1.age)

