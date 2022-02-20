#Python program to depict multiple inheritances
class Class1:
    def m1(self):
        print('In Class1.')

class Class2(Class1):
    def m2(self):
        print('In Class2.')

class Class3(Class1):
    def m3(self):
        print('In Class3.')

class Class4(Class2, Class3):
    def m4(self):
        print('In Class4.')

obj = Class4()
obj.m4()     #accessing method from Class1
obj.m3()    #accessing method from Class2
obj.m2()    #accessing method from Class3
obj.m1()    #accessing method from Class4