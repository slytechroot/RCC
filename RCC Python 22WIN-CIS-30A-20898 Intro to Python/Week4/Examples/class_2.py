#Another example for - class
class Dog:

    #a simple class
    #attribute
    attr1 = 'mamal'
    attr2 = 'dog'

    #a sample method
    def fun(self):
        print("I'm a ", self.attr1)
        print("I'm a", self.attr2)

#driver code
#object instantiation
Rodger = Dog()

#accessing class attributes
#and method through objects
print(Rodger.attr1)
Rodger.fun()
