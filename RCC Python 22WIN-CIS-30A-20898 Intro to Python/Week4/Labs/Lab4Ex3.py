'''
Write a Python program that asks for your name. 
Use Assert to validate that the name is alphabetic, 
and raise an exception when the user inputs numbers. 
'''
try:
    name = input('Enter your name: ')
    assert name.isalpha()
except:
    raise ValueError('You did not enter a correct name.')
else:
    print('Your name: ', name)
finally:
    print('Thank you!')

