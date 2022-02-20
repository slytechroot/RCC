'''
1.	A car travels 50 miles on the first day, 70 miles on the second day, 
and 100 miles on the third day. 
Write a function that converts the total miles into kilometers. 1 mile = 1.6 km
a.	Define function
a.	List contains miles each day
b.	sum() to find total miles
c.	Operate calculation to convert km
b.	Function call
'''
miles = [50,70,100]

def miles_to_km(num):
    print('Total km: {}'.format(num*1.6))

miles_to_km(sum(miles))


