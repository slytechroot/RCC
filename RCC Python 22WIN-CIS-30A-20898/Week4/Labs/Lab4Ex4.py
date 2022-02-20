'''
Write a program that asks the user to enter a ten-digit phone number, for example 9515716190. 
Use Assert and Except to check for input validation. 
Print ‘Good phone number’ when the user inputs a valid phone number.
'''
try:
    phone_no = int(input('Enter your phone #: '))
    assert phone_no.isdigits()
except:
    raise ValueError('You did not enter a 10 digit phone number.')
else:
    print('Good phone number.')
finally:
    print('Thanks!')

