#interations
#in python we can iterate over lists.
#using function range(number) will create a list of ranged numbers.

def Main():
    for step in range(5):
        print(step)

    #create a list. we use [] brackets.
    words = ['cat','bat','hat','rat','sat']
    for word in words:
        print(word)
    
    #while loop is to repeat the code until the result is False.
    num = 0
    while num <= 0:
        num = int(input('Please enter a positive integer: '))

    #make a while infinite loop
    while True:
        print('Please enter a positive integer: ')
    
if __name__ == "__main__":
    Main()



