'''
1.	Write a Python script that prompts the user to enter their name and password. 
Use exception handling to validate the username is in alphabet and the password is alphanumeric. 
'''
try:
    name = input('Enter your username: ')
    password = input('Enter your password: ')
    assert name.isalpha()
    assert password.isalnum()
    #assert password.isalpha()
except:
    raise ValueError('You did not enter a correct username or password!')
else:
    print('Your name: ', name)
    print('Your password:  ', password)
finally:
    print('Thank you!')

print("Your name is " + name + ' and your password is ' + password)

