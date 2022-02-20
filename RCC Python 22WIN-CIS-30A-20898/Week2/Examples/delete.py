# how to delete elements from our list
my_list = ['P','r','o','b','l','e','m']
print (my_list)

#delete one item
del my_list[2]
print (my_list)

#delete multiple items
del my_list[1:5]
print(my_list)

#delete entire list
del my_list

#Error: List not defined. The my_list was deleted
#from the system, so it cannot be printed
print(my_list)


#another method to remove from list/index
#is pop or remove method. 