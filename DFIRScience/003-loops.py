x = 0

while x <= 10:
  print(x)
  x += 1 # increment
else:
  print("Finished the x<=10!")

#range(20, 30)

for y in range(20, 30):
  if y == 25:
    continue
  print(y)
  if y == 28:
    print("y is 28!")
    break

print("Outside the loop. Terminating...")

