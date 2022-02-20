'''
14.	BestElectronics sells the following items: 
1.	Laptop: $299.99
2.	Gaming desktop PC: $1029.99
3.	TV: $249.99
4.	X-box One: $219.99
5.	Nintendo Switch: $279.99
Write a Python program that does the following:
1.	 Prompts customer to enter a choice of product. Then, store the choice and add price to subtotal. 
2.	Ask if user wants to select another product. 
a.	If customer selects another product, then add to subtotal. 
b.	If customer does not select product, proceed to the next step.
3.	Use the functionality in the module that you created in Exercise #13 to display customer order and output receipt file. 
Provide screen capture of script and output.
'''
import Lab3Ex13

db = {1:('Laptop', 299.99), 2:('Gaming PC', 1029.99), 3:('TV', 249.99), 
    4:('X-box One', 219.99), 5:('Nintendo Switch', 279.99)}

print('Here is a list of products: ')

for k, v in db.items():
    print('{}) {}: $ {}'.format(k, v[0], v[1]))

customer_list = []

keep_choosing = "Y"
while keep_choosing == 'Y':
    choice = int(input('\n What is your choice: '))

    if choice in db.keys():
        customer_list.append((db[choice][0], db[choice][1]))
    else:
        print('Invalid Choice.')

    keep_choosing = input('Keep choosing (Y for yes, N for no): ').upper()

Lab3Ex13.total(customer_list)

