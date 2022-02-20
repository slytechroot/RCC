"""
20.Given the below list, which contains student names and correlated ages:
•students = [[‘Jack’, ‘Lisa’, ‘Tomas’, ‘Daniel’],[22, 27, 30, 19]]
Write a Python program that fulfills the following criteria:
A.access the list using a FOR loop to display the names and age of the students. 
B.Display second name and age: Lisa, 27.
"""
#multi-dimensional lists - 2D lists
students = [['Jack', 'Lisa', 'Tomas', 'Daniel'],[22, 27, 30, 19]]
print(students)
print(' ')
#A.access the list using a FOR loop to display the names and age of the students.
for i in range(len(students)):
    for j in range(len(students[i])):
        print(students[i][j], end = ' ')
    print()

#B.Display second name and age: Lisa, 27.
print([i[1] for i in students])

#print 'Lisa'
print(students[0][1])

#print 27
print(students[1][1])
