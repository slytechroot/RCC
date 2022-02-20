#Class Attribute Example
class sampleclass:
    count = 0 #class attribute

    def increase(self):
        sampleclass.count += 1

#calling increase() on an object
s1 = sampleclass()
s1.increase()
print(s1.count)

#calling increase on one more
#object
s2 = sampleclass()
s2.increase()
print(s2.count)

print(sampleclass.count)
