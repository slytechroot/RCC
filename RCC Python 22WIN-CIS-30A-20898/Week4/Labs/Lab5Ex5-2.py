'''
1.	Create a Student class with the following:
a.	attributes: Name, ID, Gender
b.	methods: register, addCourse, greet, printCourses, 
c.	each student should have a list of courses.
d.	Give each student unique attributes and courses.
'''
class Student():
    courses = [] #empty list

    def __init__(self):
        print("Thank you for being a student at MVC \n")
        self.name = input('What is your name: ')
        self.ID = int(input('Enter 4-digit ID: '))
        self.gender = input('What is your gender: ')

    def __init__(self, name, ID, gender):
        self.name = name
        self.ID = ID
        self.gender = gender

    def addCourse(self, course):
       self.courses.append(course)

    def register(self):
        num = int(input('\nHow many classes do you want to register for? (1-5): '))
        self.addCourse(num)

    def addCourse(self, num):
        for i in range(num):
            course = input('\nName of the class you want to add: ')
            self.courses.append(course)
    
    def printCourses(self):
        print('\nYou are enrolled in: ')
        for i in self.courses:
            print(i, 'class')
    
    def greet(self):
        print('\nHello', self.name)
        print('ID: ', self.ID)
        print('Gender: ', self.gender)

student1 = Student('John', 1234, 'Male')
student1.addCourse('Math')
student1.addCourse('English')

student1 = Student()
student1.register()
student1.greet()
student1.printCourses()

student2 = Student()
student2.register()
student2.greet()
student2.printCourses()

student3 = Student()
student3.register()
student3.greet()
student3.printCourses()

