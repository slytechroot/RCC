'''
13.	Create a module to do the following:
•	Calculate sales tax from subtotal, 7.75 percent of subtotal. 
    Display sales tax amount.
•	Calculate shipping cost at 5% of the subtotal cost. Display shipping cost. 
•	Calculate grand total with tax. Display the grand total.
•	Open and write product choice, discount, subtotal, tax and grand total 
    to “receipt.txt”. 
•	Close file.
•	Display “Thank you for shopping with us!”
'''
from re import sub
fout = open('receipt.txt', 'w')
#declare tax
tax = 0.0775
#function to determine the total from tax and shipping
def total(customer_list):
    #initialize subtotal at 0
    subtotal = 0

    for i in customer_list:
        subtotal += (i[1])

    print(customer_list)
    #format for 2 decimal points
    print('Subtotal: $ {:.2f}' . format(subtotal))

    shipping = subtotal * 0.05
    print('Shipping: $ {:.2f}' .format(shipping))

    t_amount = tax * subtotal
    print('Tax: \t $ {:.2f}' .format(subtotal))

    total = subtotal + t_amount + shipping
    print('Total: \t $ {:.2f}' . format(total))

    receipt(customer_list, subtotal, total, shipping)

def receipt(customer_list, subtotal, total, shipping):
    fout.write('**** RECEIPT ****\n')
    fout.write('Item        Price\n')
    fout.write('****         ****\n')

    for i in customer_list:
        fout.write('{}   $ {}\n'.format(i[0],i[1]))

    fout.write('''
--------------------------
Subtotal: $ {}
Shipping: $ {:.2f}
Tax:      % {}
Total:    $ {:.2f}
--------------------------
Thank you for shopping with us...
'''.format(subtotal, shipping, tax*100, total))

    fout.close()
    print('\n Your receipt has been printed in the receipt.txt file!')


