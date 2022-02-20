"""
16.At a restaurant, Katie orders the following items:

•a burger, $9.99
•milkshake, $5.25
•fries, $2.75
•2 tacos, $2.99 
•nachos, $5.25
•lemonade, $3.75
Write a Python program that determines the subtotal of Katie’s order. Program must use WHILE loop. 

"""
foods = [9.99,5.25, 2.75,2.99,5.25,3.75]
sub_total = 0
j = 0 # j as the indexer to access each index items

while (j < len(foods)):
    sub_total = sub_total + foods[j]
    j = j + 1

#to print raw results from subtotal after addition of all items
print(sub_total)

#to print with 2 decimal using the round method
print("Subtotal amount: $", round(sub_total,2))

















