"""
1.	Write a Python script that contains a variable that holds your first name
and add statements to fulfill the following tasks:
A.	Display the first and last letter of your first name using index.
B.	Display the number of characters in your first name.
C.	Display the first to third letter of your first name using index.
D.	Display the second to last letter of your first name using index.
E.	Display the second to last letter of your first name using len().

"""
my_name = "Attila"

#display first and last letter
print("The first letter in my first name is: ", my_name[0])
print("The last letter in my first name is: ", my_name[-1])

#Display the number of characters
print("Number of characters in my first name is: ", len(my_name[:]))
#or
print("Number of characters in my first name is: ", len(my_name))

#display 1st to 3rd letter
sub_name = my_name[0:3]
print("The first to third letter of my first name is: ", sub_name)
#same as
sub_name = my_name[:3]
print("Same as: ", sub_name)

#display the second to the last letter
sub_name2 = my_name[1:]
print("The first to third letter of my first name is: ", sub_name2)
#same as
sub_name3 = my_name[1:len(my_name)]
print("Same as: ", sub_name3)

