# r read
# w write
# a append
###############
# Create a file handle first!!!
# F is a file handle or FH for file handle

# Open file and write to it. This will create a new file. 
F = open("007-test.txt", "w")
#print the file to screen. 
print(F)

#Write to file
F.write("I'm writing to a file.\n")
F.write("This is a second line.\n")
F.write("This is a third line.\n")

#Script closing the file
print("\nClosing the opened file...\n")
F.close()

print("Reading from file below this line. \n")

# \n
#Read contents of file. 
F = open("007-test.txt", "r")

# Read from file
# TROUBLESHOOT THIS LINE!!!!!!!
#print(F.read())

#Read the first 10 characters
#print(F.read(10))

#Read lines
#print(F.readline())
#print(F.readline())
#print(F.readline())

#Read ALL lines. This will enclose the output in square brackets [].
#print(F.readlines())

for line in F:
  #print(line)
  print(len(line))
  if len(line) == 21:
    print("Cool guy!")
  else:
    print ("Not a cool guy!")

F.close()
