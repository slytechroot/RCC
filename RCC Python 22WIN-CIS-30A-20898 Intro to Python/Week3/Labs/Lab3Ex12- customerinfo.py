'''
1.	Complete the following tasks:
A.	Create a module with the following functionality:
•	Verify customer input is digit or alphabet. 
•	Store the input into a text file, “customer_info.txt”. 
•	Read and display the stored data from the file.
B.	Write a program that prompts the customer enter name, 
age, phone number, marital status. 
C.	Then use the module to check input, store, read 
and display customer information. 
'''
def check_name(name):
    if name.isalpha():
        print(name)
    else:
        input("Enter a valid name: ")

def check_age(age):
    if age.isdigit():
        print(age)
    else:
        input('Enter a valid age: ')

def check_phone(phone):
    if phone.isdigit():
        print(phone)
    else:
        input('Enter a valid phone number: ')

def check_marital(marital):
    if marital.isalpha():
        print(marital)
    else:
    input('Enter valid marital status: ')

def store_info(name, age, phone, marital):
    file = open('customerinfo.txt', 'w')
    file.write(name + '\n')
    file.write(age + '\n')
    file.write(phone + '\n')
    file.write(marital + '\n')
    file.close()
    print('Information stored. ')

def r_info(name, age, phone, marital):
    file = open('customerinfo.txt', 'r')
    print(file.read())
    file.close()


