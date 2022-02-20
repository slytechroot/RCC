#message.py
class message: #define a class called message
    def __init__(self, text): #define the initialization function that takes 
                                #arguments from the class instance.
        self.text = text #converts the text argument into a variable that is an element
                        #of the instance of the class
    def print(self): #a function that prints self.text
        print(self.text)

instance = message("This is my message.")

print(instance.text)
instance.print()

