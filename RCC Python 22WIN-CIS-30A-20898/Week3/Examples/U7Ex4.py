#Unit 7 assignment 4
#starts here. Next jumps to checkAge(user_age).
user_age = int(input('Enter your age: '))

def checkAge(user_age):
    if user_age < 65:
        print('Your are under 65.')
    else:
        print('Your age is 65 or higher. ')

#After asks for user to input age, this is the second line the compiler looks at. 
checkAge(user_age)

