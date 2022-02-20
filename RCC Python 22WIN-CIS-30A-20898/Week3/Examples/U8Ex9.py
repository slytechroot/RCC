#More file handling
file = open('myfile.txt', 'r')

#readlines() - read individual lines of the file
print(len(file.readlines()))

'''Note
when python reads all the lines, the cursor is now at the end.
so we have to bring it back to the 1st line to read the 1st character.
'''

file.seek(0)

words = 0
for line in file:
    words += len(line.split())

print(words)
file.close()
