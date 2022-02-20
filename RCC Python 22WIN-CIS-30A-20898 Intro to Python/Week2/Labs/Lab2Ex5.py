"""
5. Write a Python program that uses join() to display a
list of your family member names,
each name should be separated by “#”. 
"""

my_family = ['Attila Kun', 'Francisc', 'Florica', 'Marius']
print(my_family)
print("\r")
symbol = "#"

#print all characters in small letters
print(symbol.join(my_family))

#same as above
print("#".join(my_family))

