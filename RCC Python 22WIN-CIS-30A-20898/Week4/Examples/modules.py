#Modules
#collections of code written by other people.
#standard modules allow for interaction with the OS, with the network and many more.
import math

def Main():
    try:
        number = float(input('Enter a number: '))
        number = math.fabs(number)
        print(number)

    except:
        print('You did NOT enter a float number!')

if __name__ == "__main__":
    Main()