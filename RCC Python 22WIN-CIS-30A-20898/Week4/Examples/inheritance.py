class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#use the Person class to create an object, and then execute the printname method:
x = Person('Marcus','Brown')
x.printname()

#define child class using pass to have same functionality as Parent
class Student(Person):
    pass

x = Student('Mike','Olsen') #use child class to create object and reprint
x.printname()

