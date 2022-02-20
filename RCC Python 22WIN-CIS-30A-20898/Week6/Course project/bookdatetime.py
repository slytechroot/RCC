#choose day, time for appointment
#start getting user information
def check_month(month):
    if month.isalpha():
        print(month)
    else:
        input("Enter a valid month: ")

def check_day(day):
    if day.isalpha():
        print(day)
    else:
        input("Enter a valid day of the week: ")

def check_time(time):
    if time.isdigits():
        print(time)
    else:
        input('Enter a valid day time: ')

def booking_info(month, day, time):
    file = open('customerinfo.txt', 'a+')
    file.write(month + '\n')
    file.write(day + '\n')
    file.write(time + '\n')
    file.close()
    print('\nThe above information has been appended to your file... ')

