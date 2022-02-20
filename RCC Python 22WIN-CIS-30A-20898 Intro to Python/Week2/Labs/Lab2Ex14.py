"""
14.In a diet plan, a client loses 10 pounds the first month, 12 pounds the second month,
8 pounds the third month and 5 pounds the fourth month.
Write a Python program that uses a FOR loop to find the total weight that the client loses over 4 months.

"""
weight_loss = [10,12,8,5]

#initializing total weight loss
total_l = 0

for i in weight_loss:
    total_l += i
print('Total weight loss in 4 months:', total_l)

#using range
for j in range(len(weight_loss)):
    print('Weight loss month ', (j+1), ":" , weight_loss[j])

print('Total weight loss using range:', sum(weight_loss))
























