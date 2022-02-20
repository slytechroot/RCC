"""
1.Maria is saving for her vacation. During the first year, she saves the following:
$200, $320, $180, $210, $175, $305. 
In the second year, Maria is able to save $550, $285, $195, $410. 
Use Python lists, without using sum(), write a program to determine which year Maria saved the most.

"""
year1 = [200, 320, 180, 210, 175, 305]
year2 = [550, 285, 195, 410]
print (year1)
print (year2)

'''Option 1 - without using the sum() method'''
sum_year_1 = 0
sum_year_2 = 0

for i in year1: sum_year_1 += 1
for i in year2: sum_year_2 += i

if sum_year_1 > sum_year_2:
    print('Maria saved more in the 1st year.')
else:
    print('Maria saved more in the 2nd year.')
    
'''Option 2 - using the sum() method'''
if sum(year1) > sum(year2):
    print ('She saved more in the 1st year.')
else:
    print ('She saved more in the 2nd year.')