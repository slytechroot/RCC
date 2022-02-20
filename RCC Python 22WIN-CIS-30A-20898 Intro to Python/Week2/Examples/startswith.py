#str.startswith(str, beg = 0,end = len(string));
#!/usr/bin/python3

str = "this is string example....wow!!!"
print (str.startswith( 'this' ))
print (str.startswith( 'string', 8 ))
print (str.startswith( 'this', 2, 4 ))

#starts with "P"
my_strng = "Peter Pan"
print(my_strng.startswith("P"))

#starts with "Bel" at position 7 and ends at position 24
strng1 = "Tinker Bell and Peter Pan"
print(strng1.startswith("Bel", 7, 24))

