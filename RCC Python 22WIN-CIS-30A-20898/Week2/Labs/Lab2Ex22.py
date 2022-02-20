"""
1.Write a Python program to fulfill the following criteria:
A.Create a dictionary with the below key and values:
•name: John Doe
•ID: 999999
•Course: CIS30A
Print the dictionary
B.Add an item: Semester: Fall 2020. Print the updated dictionary.
C.Change Course value to ‘Python’. Print the updated dictionary.
D.Remove ID from the dictionary. Print the updated dictionary.
E.Use popitem() to remove the last item in the dictionary. Print dictionary.
F.Clear all items in dictionary. Print dictionary.

"""
#A
dictionary = {'Name':'John Doe', 'ID': 999999, 'Course':'CIS30A'}
print(dictionary)

#B
dictionary['Semester'] ='Fall 2020'
print(dictionary)

#C
dictionary['Course'] = 'Python'
print(dictionary)

#D
dictionary.pop('ID')
print(dictionary)

#E
dictionary.popitem()
print(dictionary)

#F
dictionary.clear()
print(dictionary)

