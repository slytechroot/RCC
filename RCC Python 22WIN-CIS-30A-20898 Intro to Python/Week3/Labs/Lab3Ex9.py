'''
1.	Create a file called myfile.txt and complete the following tasks:
A.	Write the following sentences into the file:
“I am a student”
“I am learning Python”
B.	Close the file.'''

file = open('myfile.txt', 'w')

file.write('I am a student\n')
file.write('I am learning Python\n')
file.close()