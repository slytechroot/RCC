'''
Write a Python program accepts user input between 1 – 10, 
and raises an exception when the input is not within the given range
'''
num = int(input("Enter a number: "))

if num > 0 and num < 11:
    print('The number is: ', num)
else:
    raise Exception('Invalid number.')

