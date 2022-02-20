#8.	Review the below script and determine the area 
#of the script that consists of class or instance attributes. 

class car(): 
      
    # init method or constructor 
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 
          
    def show(self): 
        print("Model is", self.model ) 
        print("color is", self.color ) 
          
# both objects have different self which  
# contain their attributes 
audi = car("audi a4", "blue") 
ferrari = car("ferrari 488", "green") 
  
audi.show()     # same output as car.show(audi) 
ferrari.show()  # same output as car.show(ferrari)

### The answer is below: #####
### -> the class attribute could be audi.show() or ferrari.show(),
#     while instance attributes are self, model and color. 