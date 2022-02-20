'''
Write a Python program that includes the following tasks:
A.	Display the intersection of A_set and B_set. #300
B.	Display the difference of A_set and B_set. #100, 200
C.	Verify that A_set is disjointed from C_set. #True
D.	Display the union of A_set with B_set. #100, 200, 300, 400, 500
E.	Display the symmetric difference of B_set and C_set. #400, 600, 700
'''
A_set = frozenset([100, 200, 300])
B_set = frozenset([300, 400, 500])
C_set = frozenset([500, 600, 700])

#A - intersection between A and B
print(A_set.intersection(B_set))

#B - difference between A and B
print(A_set.difference(B_set))

#C - validate if disjoin A from C
print(A_set.isdisjoint(C_set))

#D - union between A and B
print(A_set.union(B_set))

#E - symmetric difference between B and C
print(C_set.symmetric_difference(B_set))

