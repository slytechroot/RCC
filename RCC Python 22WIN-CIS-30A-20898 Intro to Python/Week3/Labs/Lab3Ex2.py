#Week 3 - Lab 3 - Exercise 2
'''	Write a Python program that includes the following tasks:
A.	Copy content of letters_1 to letters_3 set. Display letters_1 set.
B.	Add content of letters_2 to letters_1 set. Display updated letters_1 set.
C.	Display the difference between letters_1 and letters_2 set.
D.	Remove 'I' from letters_1 set.
E.	Print the number of items in letters_1 set.
F.	Use discard() to eliminate 'E' and 'I' from letters_1 set. 
Then print content of the set.
'''
letters_1 = {'D', 'E', 'F', 'G'}
letters_2 = {'H', 'I'}

#copy letters_1 to letters_3
letters_3 = letters_1.copy
print(letters_1)
print(letters_3)

#add 'H' and 'I' to letters_1
letters_1.add('H')
letters_1.add('I')
#letters_1.update(letters_2)
print(letters_1)

#difference between letters_1 and letters_2
print(letters_1.difference(letters_2))

#remove 'I' from letters_1
letters_1.remove('I')
print(letters_1)

#show amount of items in letters_1
print(len(letters_1))

#discarding 'E'
letters_1.discard('E')
print(letters_1)
letters_1.discard('I')
print(letters_1)