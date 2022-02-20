#Calculate Lisa's coffee purchase total amount

customer_purchase = 23
cost_perPound = 10.00
customer_purchase *= cost_perPound

discount = 0.10 * (customer_purchase)
print('Discount amount: $ {:.2f}' .format(discount))

total_amount = customer_purchase - discount
print('Discount amount: $ {:.2f}' .format(total_amount))