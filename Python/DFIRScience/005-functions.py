print("Good morning...")
print("Hello Attila")

#Define function sayHello()
def sayHello():
  print("\nHello...")

#you MUST call the function
sayHello()

#define sayHelloName function
def sayHelloName(name):
   print("\n\nGood morning " + name)
sayHelloName("Jarvis")

#while loop
x = 0
while x < 3:
    sayHello()
    x += 1


# 
print ("\n...do simple math")
def addOne(x):
  return x + 1

y = addOne(3)
print(y)
