def getInteger(prompt):
    result = int(input(prompt))
    return result

def Main():
    print('Started...')
    output = getInteger('Please enter an integer: ')
    output2 = getInteger('Please enter another integer: ')
    print(output)
    print(output2)

if __name__ == "__main__":
    Main()

