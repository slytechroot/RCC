print("Exercise 1.")
num = -4
if num > 0:
    print(num, "is a positive number.")
else: 
    print(num, "is a negative number.")
#############
print("Exercise 2.")
age = 37
if age > 21:
    print(age, "is above legal age limit")
elif age == 0:
    print(age, "is a newborn age")
else:
    print(age, "is under legal age limit")

#############
print("Exercise 3.")
numbers = [16, 15, 19, 18, 14]
total = 0
for i in numbers:
    total = total+i
print(total)
############
print("Exercise 4.")
val = range(10, 16)
for i in val:
  print(i)

################
print("Exercise 5.")
n = 20
i = 1
val = 0

while i <= n:
    val -= i
    i = i+1    

print(val)

#######
print("Exercise 6.")
my_list = [3, 8, 6, 1, 7, 2]

print(my_list[0])

print(my_list[3])

print(my_list[5])
#########
print("Exercise 7.")
newlist = [[44, 33, 22, 11],[2, 0, 1, 5]]

print(newlist[0][2])

print(newlist[1][2])

########
print("Exercise 8.")
my_list = [3, 7, 9, 4, 1, 2, 6]

print(my_list[1:5])

print(my_list[:-4])

print(my_list[2:])
#########
print("Exercise 10.")
nums = [1,2,5,8,9]

nums.insert(4,3)
print(nums)

nums[2:2] = [6,3]
print(nums)

##################
print("Exercise 11.")
my_list = [6, 2, 3, 9, 11, 4]
my_list.remove(2)
my_list.pop(2)
my_list.pop()
print(my_list)

#############
print("Exercise 13.")
A = frozenset([20, 21, 22, 23])
B = frozenset([23, 24, 25, 26])
C = frozenset([27, 28])

print(A.isdisjoint(C)) 
print(C.issubset(B)) 
print(B.issuperset(C))  

#########
print("Exercise 16.")
nums = [5, 7, 10]

def mult(num):
    print((num*2))

mult(sum(nums))
