#Question 1 - what is the output below?
age = 16

if age > 21:
    print(age, "is above legal age limit")
elif age == 0:
    print(age, "is a newborn age")
else:
    print(age, "is under legal age limit")

#Question 2 - what is the output below?
numbers = [6, 5, 9, 8, 4]

val = 0
for i in numbers:
            val = val+i
print(val)

#Question 3 - Which of the following option is the LAST output after the 
#               below program has ran?
val = range(1, 6)
for i in val:
  print(i)

#Question 4 - Determine the output of the following program:
n = 10
i = 1
val = 0

while i <= n:
    val -= i
    i = i+1
print(val)

#Question 5 - Given my_list below - Which of the following statements will print the 
# third element value in my_list?
my_list = [3, 8, 6, 1, 7, 2]

print(my_list[-4])
print(my_list[-3]) #this is also the 3rd index of the list, but from a negative index
print(my_list[3]) 
print(my_list[4]) #this is the 3rd positive index in the list


#Question 6 - Given newlist - Which of the following statement will print the next to 
#               last element of the second sub-list, value 5?
newlist = [[44, 33, 22, 11],[2, 0, 1, 5]]

print(newlist[0][2])
print(newlist[1][3])
#print(newlist[5])
#print(newlist[3])

#Question 7 - given my_list - Which of the following statement will print values [7, 8, 4, 2]?
my_list = [1, 3, 7, 8, 4, 2, 5]

print(my_list[3:6])
print(my_list[2:])
print(my_list[:-5])
print(my_list[2:6])

#Question 8 - Determine the output of the following program:
my_list = [6, 2, 3, 9, 11, 4]

my_list.remove(2)
my_list.pop(4)
my_list.pop() #pops out the last item in the list/index
print(my_list)

#Question 9 - Given A, B, C - Which of the following statement would print True?

A = frozenset([10, 11, 12, 13])
B = frozenset([14, 15, 16, 17])
C = frozenset([16, 17, 18])

print(A.isdisjoint(B))
print(C.issuperset(B))
print(C.issubset(A))
print(B.issuperset(A))

#Question 10 - answer the question. 








