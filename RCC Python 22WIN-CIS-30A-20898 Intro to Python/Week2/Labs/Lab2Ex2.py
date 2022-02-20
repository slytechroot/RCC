"""
2.Write a Python program that contains a variable, state_name = “Indianapolis”,
use count() to show the number of ‘i’ in the string.
"""
state_name = "Indianapolis"

#Display the number of characters
print("Number of characters in my first name is: ", len(state_name [:]))
#or
print("Number of characters in my first name is: ", len(state_name))

print(state_name.count('i'))

#for ALL I or i - large and small
print(state_name.count('i') + state_name.count('I'))
