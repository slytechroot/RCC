x = "hello"
food = ["tacos", "cookies", "kimchi"]

print (food[1])

print (len(food[1]))

#new variable f
for f in food:
  print(f)

food.append("chips")

print(food)

#remove food[] index 2 (by array) string from list

food.pop(1)
print(food)

#remove food[] index 3 string from list

food.remove("kimchi")
print(food)

print ("Item removed from list is:" + (f))
print (len(f))

print(food)

# trying something new with For loop statement
print ("\n Trying this...\n")
#print ("\n")

for r in food:
  print (r)
  if f != ("milk"):
    print("I don't like eating cookies!")
