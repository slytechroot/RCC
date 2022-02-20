'''
Write a program that contains multi-level inheritance, School (base or parent) class, 
which has school name attribute, Course (intermediate or child) class that has course 
name attribute, Room (derived or grandchildren) class that class room number attribute. 
Create an object that will display “Intro to Python”, “Room 16”, “MVC”. 
'''
class School:
    def __init__(self):
        self.school_name = None

    def showSchool(self):
        print(self.school_name)

class Course(School):
    def __init__(self):
        super().__init__()
        self.course_name = None

    def showCourse(self):
        print(self.course_name)

class Room(Course):
    def __init__(self):
        super().__init__()
        self.room_number = None

    def showRoom(self):
        print(self.room_number)

c1 = Room()
c1.school_name = 'MVC'
c1.course_name = 'Intro to Python'
c1.room_number = 16

c1.showSchool()
c1.showCourse()
c1.showRoom()

