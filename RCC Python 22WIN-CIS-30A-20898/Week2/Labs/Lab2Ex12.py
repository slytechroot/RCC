"""
12.Store A sells a 50” LCD TV for $400 and charges for shipping.
Store B sells the same LCD TV for $530 and provides free shipping.
The television weights 65 lbs. and shipping company charges $1.25 per pound to ship the TV.
Write a Python program that determines which store charges less for the TV.
Program should contain IF-ELSE statement. 
"""
storeA_TV = 400.00 #dollars
storeB_TV = 530.00 #dollars
TV_weight = 65     #pounds
shipping_charge = 1.25 #dollars

#calculate total shipping per pound
shipping = TV_weight * shipping_charge
print("Shipping costs per pound - $", shipping)

#calculate total cost for TV cost + shipping for storeA
total_A = storeA_TV + shipping
#print it out to terminal
print("\nStore A TV + shipping: $", total_A)
print("Store B TV: $", storeB_TV)

#compare the 2 stores
if total_A > storeB_TV:
    print('\nStore A charges more for TV')
else:
    print('\nStore B charges more for TV')










