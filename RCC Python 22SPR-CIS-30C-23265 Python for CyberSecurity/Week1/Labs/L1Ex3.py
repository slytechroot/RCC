'''
1.	Write a Python script that prompts the user to enter their name and password. 
Use exception handling to validate the username is in alphabet and the password is alphanumeric. 
'''
try:
    name = input('Enter your username: ')
    assert name.isalpha()
except:
    raise ValueError('You did not enter a correct username!')
else:
    print('Your name: ', name)
finally:
    print('Thank you!')

try:
    password = input('Enter your password: ')
    assert password.isalpha()
except:
    raise ValueError('You did not enter a correct password!')
else:
    print('Your password:  ', password)
finally:
    print('Thank you!')

print("Your name is " + name + ' and your password is ' + password)

