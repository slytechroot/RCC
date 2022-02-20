#Example 3 - class
class Car():

    #init method or constructor with arguments
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def show(self):
        print("Model is", self.model)
        print("Model is", self.color)

#both objects have different self which
#contain their attributes
audi = Car("Audi A4", "blue")
ferrari = Car("Ferrary 488", "green")

audi.show() #same output as car.show(audi)
ferrari.show() #same output as car.show(ferrari)