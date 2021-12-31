# Create a program that prompts user to input his or her height in feet
# and inches. Then, convert the height to meters.

#convert to inches!!!
#prompt for height in feet
user_height = float(input ('Enter your height in feet: '))
#convert feet to inches
user_height *= 12
#rounding the converted values to 2 decimal
user_height = round(user_height, 2)
print('You are', user_height, 'inches')

#convert to meters!!!
user_height *= 0.0254
user_height = round(user_height, 2)
print('You are', user_height, 'meters')


