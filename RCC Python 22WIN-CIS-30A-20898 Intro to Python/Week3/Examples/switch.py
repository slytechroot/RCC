#using switch in Python
from email.policy import default


user_choice = int(input('Enter 1 for Monday, 2 for Tuesday... 7 for Sunday: '))

def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day."

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
}

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default) ()

print(switch(user_choice))


