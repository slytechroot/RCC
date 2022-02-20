"""
1.Write a Python program that contains 3 variables: user_name, user_age, user_address.
Assign values to the variables and complete the following tasks:

A.Use isalpha() to check if the user_name contains only alphabets. 
B.Use isdigit() to check if the user_age contains only numbers.
C.Use isalnum() to check if the user_address contains alphanumeric values.

"""
user_name = input('Enter your name: ')
if user_name.isalpha():
    print('You entered: ', user_name)
else:
    user_name = input('Re-enter your name: ')
    

user_age = input('Enter your age: ')
if user_age.isdigit():
    print('You entered: ', user_age)
else:
    user_age = input('Re-enter your age: ')
    
    
user_address = input('Enter your address: ')
if user_address.isalnum():
    print('You entered: ', user_address)
else:
    user_address = input('Re-enter your address: ')

print('Summary:', user_name, user_age, user_address)
    
print('Thank you!')