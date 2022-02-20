#try and finally
f = open("test.txt", 'r')

try:
    #raise NameError("Hi there!")
    print("Checking errors!")

finally:
    f.readlines()
    f.close()
print("No file exists!")



