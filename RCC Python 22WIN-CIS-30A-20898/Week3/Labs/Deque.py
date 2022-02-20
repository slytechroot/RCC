#Frozensets
#initialize A and B
A = frozenset([1,2,3,4])
B = frozenset([3,4,5,6])
C = frozenset([5,6])

#isdisjoint() method
#print(SetToEvaluate.method(evaluatedAgainst)
print(A.isdisjoint(C)) #Output: true

#issubset() method
#is C a subset of B?
print(C.issubset(B)) #Output: true

#issuperset() method
#is B a superset of C
print(B.issuperset(C)) #Output: true
#copy a frozenset

#C is a copy of A. Printout C. 
C = A.copy() #Output: frozenset({1,2,3,4})
print(C)

#union. Join (combine) two sets together. 
print(A.union(B)) #Output: frozenset({1,2,3,4,5,6})

#intersection. Printout the sets that are similar in both sets. 
print(A.intersection(B)) #Output: frozenset({3,4})

#difference. Difference value between sets A and B. 
print(A.difference(B)) #Output: frozenset({3,4})

#symmetric difference
print(A.symmetric_difference(B)) #Output: frozenset({1,2,5,6})





