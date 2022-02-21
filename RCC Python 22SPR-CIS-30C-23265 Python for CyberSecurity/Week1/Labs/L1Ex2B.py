#class inheritance
'''
2.	Write a Python script that uses class inheritance to display device information such as 
name, IP address and location. The program should fulfill the below requirements:
A.	The program should contain a parent and a child class. 
B.	The child class should inherit attributes from the parent class to add additional 
information about the device, such as location.

'''
class Dev:
    def __init__(self, name, IPaddress):
        self.name = name
        self.IPaddress = IPaddress
        print("Device name: ", name)
        print("IP address: ", IPaddress)

#class Loc uses inherited information. 
#this is a subclass of Dev (parent)
class Loc(Dev):

    def __init__(self, name, IPaddress, location):
        super().__init__(name, IPaddress)           #this will access the super class
        print("Location of device: ", location)

c = Loc('Cisco Switch', '10.0.0.17', 'HQ')

