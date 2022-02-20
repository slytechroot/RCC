"""
1.Given a string “America, land of the free.”. Write a Python program that uses
slice() constructor to do the following:
A.Use index sequencing in object to display “America”
B.Use reverse index sequencing (negative) in an object to display “free”
C.Use index sequencing in an object to display the second,
fourth and every other following characters of the string. Hint: use start, stop and step.

"""
astr = "America, land of the free."
s1 = slice(7)
print(astr[s1])

#using negative indexes to display 'free'
s2 = slice(-5,-1)
print(astr[s2])

#same as above, but using positives index to display 'free'
s2 = slice(21,25)
print(astr[s2])

s3 = slice(1, 25, 2)
print(astr[s3])

















