#start getting user information
def check_name(name):
    if name.isalpha():
        print(name)
    else:
        input("Enter a valid name: ")

def check_home_number(home_number):
    if home_number.isdigit():
        print(home_number)
    else:
        input("Enter a valid house number: ")

def check_street_name(street_name):
    if street_name.isalpha():
        print(street_name)
    else:
        input('Enter a valid street name: ')

def check_city_name(city_name):
    if city_name.isalpha():
        print(city_name)
    else:
        input('Enter a valid city name: ')

def check_phone(phone):
    if phone.isdigit():
        print(phone)
    else:
        input('Enter a valid phone number: ')

def store_info(name, home_number, street_name, city_name, phone):
    file = open('customerinfo.txt', 'a+')
    file.write('\nName: ' + name + '\n')
    file.write('Home number: ' + home_number + '\n')
    file.write('Street name: ' + street_name + '\n')
    file.write('City name: ' + city_name + '\n')
    file.write('Phone no.: ' + phone + '\n')
    file.close()
    print('\nThe above information has been stored in text file... ')
