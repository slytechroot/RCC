#Unit 1 - part 2
#Class - user defined, set of attributes we can use for the class
# we can use variables
#we will use the . operator to access those functions

class Employee:
    'Common base class for all employees'
    empCount = 0

    #class constructor - with the __init__ method to instantiate
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    #define member methods
    def displayCount(self):
        print('Total employees: ', Employee.empCount)

    def displayEmployee(self):
        print('Name: ', self.name, ", Salary: ", self.salary)

#create instances by calling Employee()
"This would create first object of Employee class"
emp1 = Employee('Lisa', 2000)
"This would create second object of Employee class"
emp1 = Employee('Richard', 5000)

