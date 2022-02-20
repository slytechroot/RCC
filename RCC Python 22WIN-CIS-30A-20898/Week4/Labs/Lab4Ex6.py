'''Define a class, Vehicle. Include Class_Suite (members, functions, statements) 
that displays the description of two types of vehicles. 
Members are make, model, color, year, price. '''

class Car:
    def __init__(self, make, model, color, year, price):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def show(self):
        print("Make is", self.make)
        print("Model is", self.model)
        print("Color is", self.color)
        print("Year is", self.year)
        print("Price is", self.price)
        print('\r')

car1 = Car('BMW','X5','blue', 2022, 50000)
car2 = Car('Audi','Quatro','silver', 2022, 40000)

car1.show()
car2.show()