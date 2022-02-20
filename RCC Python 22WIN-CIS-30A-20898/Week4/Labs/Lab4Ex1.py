#Lab4Ex1
'''
1.	Write a Python program that asks for user age. 
Use exception for input validation. The user age must be between 1 – 120. 
The program should prompt the user to re-enter the information if the 
information is invalid.
'''
age = int(input('Enter your age: '))
def getage():
    #global age
    while True:
        try:
            assert age >= 120 and age <= 1
            #if age < 1 or age > 120:
            print('Invalid input, try again from the try.')
                #age = int(input('Enter your age: ))
            #else: return age
        except ValueError:
            print('Invalid input, try again from the except.')
            break
        except AssertionError:
            print('Assertion error occurs.')
            break

print("Your age is: " + str(age))

age = getage()

