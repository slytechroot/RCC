'''
1.	Given prod = {'tomato': 'red', 'squash': 'yellow', 'potato': 'brown', 'avocado': 'green'}. 
Complete the following tasks:
A.	Use a function to display each key and its value. Example: ‘tomato’: ‘red’
B.	Include globals() and locals() to display container details.
'''
prod = {'tomato': 'red', 'squash': 'yellow', 'potato': 'brown', 'avocado': 'green'}

#print('Here is a list of each key with value: ')
for key in prod:
    print(key + ':' + prod[key])

print('\nTHE END.')





