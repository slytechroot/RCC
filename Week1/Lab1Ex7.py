# A cloud company charges clients $100/month to store 750 GB of data.
# Each additional GB will cost the clients $5.
# Create a program that prompts the user to input the amount of data to be stored in cloud, then
# calculate the total cost of cloud storage based on the input.

monthly_cost = 100.00
customer_storage = int(input("Enter the new storage total needed in GB: "))

additional_storage = customer_storage - 750
print("That's an extra of: ", additional_storage, "GB")

additional_fee = additional_storage * 5.00

# Total costs
total_cost = additional_fee + monthly_cost
print("Monthly cost and additional storage cost is ", total_cost)