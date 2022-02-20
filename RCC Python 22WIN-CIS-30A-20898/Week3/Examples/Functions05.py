#Functions

###################################################
#using multiple arguments for function
def calculateTotalSum(*arguments):
    calculateTotalSum = 0
    for number in arguments:
        calculateTotalSum += number
    print(calculateTotalSum)

calculateTotalSum(5,4,3,2,1)

########################################################
#using **argument
#variable number of keyword arguments passed
#function definition
def displayArgument(**arguments):
    for arg in arguments.items():
        print(arg)

#function call
displayArgument(argument1 = 'Hello', argument2 = 4, argument3 = 'Hi')


