#MultiLevel Inheritance
class A():
    def __init__(self):
        self.varA = 1
        print('A')

#this inherits from A
class B(A):
    varB = 2
    def __init__(self):
        super().__init__()
        print('B')

#this inherits from B
class C(B):
    varC = 3
    def __init__(self):
        super().__init__()
        print('C')

ob = C()
