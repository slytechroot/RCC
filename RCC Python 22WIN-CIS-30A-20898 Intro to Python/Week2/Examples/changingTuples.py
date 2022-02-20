#changing tuples
#the only way to change tuples is to re-assign the container
#itself

my_tuple = (4, 2, 3, [6,5])

#typeError: 'tuple' object does not support item assignment
#my_tuple[1] = 9 #Output: (4,2,3,[9,5])

#however, item of mutable element can be changed
my_tuple[3][0] = 9
print(my_tuple)

#tuples can be re-assigned
my_tuple = ('p','r','o','g','r','a','m')

#Output: ('p','r','o','g','r','a','m')
print(my_tuple)

