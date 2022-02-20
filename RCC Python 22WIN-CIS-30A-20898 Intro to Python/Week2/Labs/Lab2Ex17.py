"""
1.Write a Python program that does the following
A.Generate numbers 0 – 20. Use break statement to stop the loop at the 11th number.

Generate numbers from 0 – 25. Use continue statement skip number 20 in the iteration. 

"""
num = range(0,20,1)
for i in num:
    i = i + 1
    if i == 11:
        break
    print(i)
print('\n')

#using continue
num = range(0,25,1)
for i in num:
    i = i + 1
    if i == 20:
        continue
    print(i)















