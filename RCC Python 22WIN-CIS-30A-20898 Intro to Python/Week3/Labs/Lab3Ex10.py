'''
1.	Open the file you created in Exercise #9 and do the following:
A.	Print all the content of the file.
B.	Print the total number of lines.
C.	Print the total number of words.
'''
#Print all the content of the file
file = open('myfile.txt')
file_contents = file.readlines()
print(file_contents)

#Print the total number of lines. We add file.seek(0) because the cursor
#need to return from the end of file to beginning. 
file.seek(0)
print(len(file.readlines()))


#print the total number of words
file.seek(0)
words = 0
for line in file:
    words += len(line.split())
print(words)


#Close the file
file.close()