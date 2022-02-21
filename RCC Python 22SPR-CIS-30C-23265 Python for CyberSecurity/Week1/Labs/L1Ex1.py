'''
1.	Write a Python script that displays network device information, such as IP address, and 
fulfill the below requirements.
A.	The program should define a class and instantiate objects to access attributes. 
B.	The class should consist of member variable(s), constructor, member methods and objects. 
C.	Test the program using at least 2 arguments that contain device information.
'''
class Devices:
    'Common base class for network devices'

    #varible - shared among instances
    devCount = 0

    #class constructor
    def __init__(self, name, IPaddress) -> None:
        self.name = name
        self.IPaddress = IPaddress
        Devices.devCount += 1

    #member methods
    def displayCount(self):
        print('Total devices: ', Devices.devCount)
    
    def displayDev(self):
        print('Name: ', self.name, ", IP address: ", self.IPaddress)

#create instances by calling Class()
'This would create first object of Devices class'
dev1 = Devices('Cisco Router', "10.10.0.1")

'This would create second object of Devices class'
dev2 = Devices('Netgear Switch', '10.10.0.21')

#access objects' attributes
dev1.displayDev()
dev2.displayDev()
print("Total devices: ", Devices.devCount)

