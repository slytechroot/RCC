# how to delete elements from our list
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

#Output ['r','o','b','l','e','m']
print(my_list)

#Output: 'o'
print(my_list.pop(1))

#Output ['r','b','l','e','m']
print(my_list)

#Output: 'm'
print(my_list.pop(4))

#Output ['r','b','l','e']
print(my_list)

my_list.clear()

#output: []
print(my_list)

