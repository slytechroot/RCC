""" 19.
Given: animals = [‘dogs’, ‘cats’, ‘birds’]. Write a Python program that fulfills
the following criteria:
A.Add ‘rabbits’ to the list. Display the updated list.
B.Add ‘hamster’, ‘turtles’, ‘fishes’ to the list. Display the updated list.
C.Use (+) operator to include ‘birds’, ‘snakes’ in output. 
D.Display the updated list 3 times.
"""
animals = ['dogs', 'cats', 'birds']
print('Initial list.\n', animals)

#A.Add ‘rabbits’ to the list with append. Display the updated list. 
animals.append('rabbits')
print(animals)

#B.Add ‘hamster’, ‘turtles’, ‘fishes’ to the list. Display the updated list. 
animals.extend(['hamster', 'turtles', 'fishes'])
print(animals)

#C.Use (+) operator to include ‘birds’, ‘snakes’ in output.
include = ['birds', 'snakes']
final_list = animals + include
print(final_list)

#D.Display the updated list 3 times.
print('Print 3 times updated list.')
result = final_list * 3
print(result)







