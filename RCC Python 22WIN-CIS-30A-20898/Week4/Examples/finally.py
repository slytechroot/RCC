#Exceptions - catch errors, avoid hard crashes, good for user experience, commonly occur when dealing
#with user input or file IO.
#this happens when a user inputs the wrong data into our variable or open files that do NOT exist
# this is an OPTIONAL keyword
### Using 'Finally' ###
def Main():
    try:
        f = open('myfiles.txt', 'r')
        for line in f:
            print(line.strip('\n\r'))
        f.close()
    #if try: fails do this
    except:
        print("The file was either not found or unable to be read.")
    
    finally:
        print('Exiting...')

if __name__ == "__main__":
    Main()



