#global, local and non-local

#nest global variable in method
def displayT():
    global message1
    print(message1) #use variable in method
    message1 = "I love Python!"

#update variable
message1 = "Programming is fun! "

#call method, 'I Love Python' is displayed
displayT()

#print newly assigned string, 'Programming is fun'
print(message1)

displayT()

