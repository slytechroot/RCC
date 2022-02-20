#Lab3Ex12
 
import customerinfo

print("Please answer the following questions!")

name = input('Enter your name: ')
age = input('Enter your age: ')
phone = input('Enter your phone number: ')
marital = input('Enter your marital status: ')

customerinfo.check_name(name)
customerinfo.check_age(age)
customerinfo.check_phone(phone)
customerinfo.check_marital(marital)

customerinfo.store_info(name, age, phone, marital)

customerinfo.r_info(name, age, phone, marital)

print('Thank you!')

