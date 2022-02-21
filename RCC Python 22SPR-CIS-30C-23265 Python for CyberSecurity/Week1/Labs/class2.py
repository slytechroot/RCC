#class definition
class Employee:
    'Common base class for all employees'
    empCount = 0
	
	#class constructor - to create a blueprint for the class. 
    #You can have a Class without a constructor defined
    def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
	#define member methods
    def displayCount(self):
        print('Just counting...')
        #print("Total Employee:", Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

#This will print out the employee Name and Salary
#create instances by calling Employee()
#"This would create first object of Employee class"
emp1 = Employee('Zara', 20000)
#"This would create second object of Employee class"
emp2 = Employee('Manni', 50000)
emp3 = Employee('Manny', 40000)

#This will use declared variables emp1-3 to call on the function displayEmployee in class Employee
#access objects’ attributes
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

#This will count the number of employees
print("Total Employee: ", Employee.empCount)
