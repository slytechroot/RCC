'''
1.	Write a function that will display whether any given integer is even or odd. 
a.	Define function
i.	IF number is divisible by 2, it is even number
ii.	ELSE, it is odd number
b.	Function call
'''
num = int(input('Type a number from 0 -> 20 to find if even or odd: '))

def even_or_odd(num):
    if (num % 2) == 0:
        print('The number is even!')
    else:
        print('The number is odd.')

even_or_odd(num)