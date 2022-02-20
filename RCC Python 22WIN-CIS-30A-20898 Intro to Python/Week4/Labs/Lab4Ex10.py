'''
10.	Write a program that contains a single inheritance, Person class (parent class), 
which has a name attribute and Employee (child class) that has an ID attribute. 
Create an Employee object, assign it a name and an ID, then display both properties. 
'''
#NO PARAMETERS: assign values after object creation.
class Person:
    def __init__(self):
        self.name = None

#inheriting from class Person above:
class Employee(Person):
    def __init__(self):
        super().__init__()
        self.ID = None

emp0 = Employee()
emp0.name = 'Abel'
emp0.ID = 9876
print('emp0 name: {}\nemp0 id: {}'.format(emp0.name, emp0.ID))
print('\r')

###Required PARAMETERS: assign values during object creation
class Person:
    def __init__(self, n):
        self.name = n
class Employee(Person):
    def __init__(self, x, i):
        super().__init__(x)
        self.ID = i

emp1 = Employee('Jane', 1234)
print('emp1 name: {}\nemp1 id: {}'.format(emp1.name, emp1.ID))

