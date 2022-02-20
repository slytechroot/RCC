'''
1.	Append the following lines to the file you created in Exercise #9.
“ I enjoy programming because it makes me think “
Then, print all the contents of that file you created in Exercise #8. 
'''
#Print all the content of the file
file = open('myfile.txt', 'a+')
file.write("I enjoy programming because it makes me think.")

file.seek(0)
print(file.read())

file.close()
