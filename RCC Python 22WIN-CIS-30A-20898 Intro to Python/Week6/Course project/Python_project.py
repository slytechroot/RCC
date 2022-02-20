#Computer services business calendar
import calendar, customerinfo
from datetime import date

#program greeting the user
print('\n\t\t\t\t### Welcome to business booking calendar program. ### \n')
print('1. Please fill out all necessary information for the technician to better contact you for support.')

#Collect user's choice of service 1 through 4.
print('\n2. Which type of service are you interested in? - ')
service_choice = int(input('Enter 1 for Computer Repairs, 2 for Networking, 3 for Data backup, \
4 for general support: '))

#locally defined functions for user options
def repairs():
    return "Repairs"
def networking():
    return "Networking"
def backup():
    return "Backup"
def support():
    return "General Support"
def default():
    return "Incorrect service."

#choice helper
switcher = {
    1: repairs,
    2: networking,
    3: backup,
    4: support
}

#locally defined function
def switch(service):
    return switcher.get(service, default) ()
#output to user their choice of service
print("\nYou've chosen -> ",switch(service_choice))

#append the above information entered by user to user's appointment file
file = open('customerinfo.txt', 'w')
file.write("\nYou've chosen " + switch(service_choice) + ' as service.')
file.close()
print('\nThe above information you entered has been appended to your file... ')
    
#start collecting user information for appointment. This information will be added to the user's appointment file. 
print("\n3. Please answer the following questions for your appointment!")
name = input('Enter your name: ')
home_number = input('Enter your home number: ')
street_name = input('Enter your street name: ')
city_name = input('Enter your city name: ')
phone = input('Enter your phone number: ')
#refers to custom customerinfo.py file
customerinfo.check_name(name)
customerinfo.check_home_number(home_number)
customerinfo.check_street_name(street_name)
customerinfo.check_city_name(city_name)
customerinfo.check_phone(phone)
customerinfo.store_info(name, home_number, street_name, city_name, phone)
print('Thank you!')

#output today's date for the user
today = date.today()
print("\nToday's date is: ", today)

#collect more user information such as month, day of month and time for appointment
#Collect user's choice of month for appointment:
calendar.month_name = input('\nWhich month are you available? - ')
print(calendar.month_name)
#calendar.day_name = input('\nWhich day are you available? - ')
#print(calendar.day_name)
calendar.monthdayscalendar = input('\nWhich date works for you? - ')
print(calendar.monthdayscalendar)
calendar.timegm = input('\nWhich time are you available? -  ')
print(calendar.timegm)
print('Here is the month/day/time you booked: - ', calendar.month_name, calendar.monthdayscalendar, calendar.timegm)

#append the above information entered by user to user's appointment file
file = open('customerinfo.txt', 'a+')
file.write('\nThis is the date of the appointment: ')
file.write(calendar.month_name + '-' + calendar.monthdayscalendar + '- ' + calendar.timegm + '.')
file.close()
print('\nThe above information you entered has been appended to your file... ')

