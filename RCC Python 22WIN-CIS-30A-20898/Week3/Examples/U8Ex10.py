#more file handling

file = open('myfile.txt', 'a+')

file.write("I enjoy programming because it makes me think.\n")
file.write("Python is fun")


file.seek(0)

print(file.read())

file.close()

