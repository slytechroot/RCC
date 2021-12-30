x = 19

if x == 10:
  print ("10")
elif x == 19:
  print ("19")
elif x == 20:
  print ("20")
else:
  print ("None found")

#< > == <= >= !=

if x != 20:
  print ("not eq 20")

if x != 20 and x >= 19:
  print ("And is true")

if x == 20 or x < 20:
  print ("or is true")

if 10 <= x <= 20:
  print ("The value of x is ") + str(x)
else:
  print ("Not within range")

