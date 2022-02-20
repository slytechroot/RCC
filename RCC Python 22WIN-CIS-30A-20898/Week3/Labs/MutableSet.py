#Mutable set method
#set of vowels
vowels = {'a', 'e'}
print('Vowels are:', vowels)

#adding 'o'
vowels.add('o')
print('Vowels are:', vowels)

#adding 'a' again
vowels.add('a')
print('Vowels are:', vowels)

#tuple ('i', 'u')
tup = ('i', 'u')

#adding tuple
vowels.add(tup)
print('Vowels are:', vowels)

#adding same tuple again
vowels.add(tup)
print('Vowels are:', vowels)

#copy numbers to new_numbers
numbers = {1,2,3,4}
new_numbers = numbers.copy()

#add 5
new_numbers.add(5)

print('Numbers: ', numbers)
print('new_numbers: ', new_numbers)

#initialize A, B
A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

#Equivalent to A-B
print(A.difference(A))

#Equivalnet to B-A
print(B.difference(A))

