# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

#changing and adding Dictionary elements
#update value
my_dict['age'] = 27
#output: {'name': 'Jack', 'age': 26}
print (my_dict)

#add item
my_dict['address'] = 'Downtown'
#output: {'address': 'Downtown', 'name': 'Jack', 'age': 26}
print(my_dict)

#Pop to remove specified 'address'
my_dict.pop('address')
print(my_dict)

#PopItem to remove the last item in dictionary, 'age':27
my_dict.popitem()
print(my_dict)

#clear dictionary
my_dict.clear()
print(my_dict)
