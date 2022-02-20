#Different types of tuplets
#container to store group of elements

#empty tuple
my_tuple = ()
print(my_tuple)

#tuple having integers
my_tuple = (1,2,3)
print(my_tuple)

#tuple with mixed datatypes
my_tuple = (1, "Hello",3,4)
print(my_tuple)

#nested tuples
my_tuple = ("mouse", [8,4,6], (3,4))
print(my_tuple)

#accessing (and printing out) tuple elements using indexing
my_tuple = ('P','e','r','m','i','t')
print(my_tuple[0]) # 'p'
print(my_tuple[5]) # 't'

#nested tuple
n_tuple = ("mouse", [8,4,6], (1,2,3))

#nested index
print(n_tuple[0][3]) # 's'
print(n_tuple[1][1]) # 4