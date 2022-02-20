#string slicing using index
str3 = 'Python'

#print using index, p as index 0, first char
print(str3[0])

#print using negative index, n at index 1, last char of string
print(str3[-1])

#print first to third
print(str3[:3])

#print third to the end
print(str3[2:])

#print from fourth character to the end
sub_str4 = str3[3:len(str3)]
print(sub_str4)
#print(str3[3:])

#print first to end, every other character
#[start:end:step]
print(str3[0:5:2])

#print entire string 5 times
print(str3 * 5)

#print from the beginning to the end, skipping every 5 character
print(str3[::5])

