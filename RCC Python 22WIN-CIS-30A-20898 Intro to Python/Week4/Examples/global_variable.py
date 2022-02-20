#global variable
#non-local variable
def a():
    #city = 'Corona'
    def b():
        global city
        city = 'Moreno Valley'
    print("Before calling b: " + city)
    print('Calling b now: ')
    b()
    print("After calling b: " + city)

city = 'Perris'
a()
print("'City' in main: " + city)