'''
1.	Given 
st_A = { 'c', 'o', 'm', 'p', 'u', 't', 'e', 'r'}, 
st_B = {'m', 'u', 't', 'e'}. 
Use Python set methods to perform the following tasks:
A.	Display which set is a subset. 
B.	Display which set is a superset.
    a.	Declare the given sets, st_A and st_B
    i.	Use method to print st_B is a subset.
    b.	Use method to print st_A is superset
'''
st_A = {'c', 'o', 'm', 'p', 'u', 't', 'e', 'r'}
print(st_A)
st_B = {'m', 'u', 't', 'e'}
print(st_B)

#display subset
print('Is B a subset of A? (True/False) ',st_B.issubset(st_A))

#display superset
print('Is A a superset of B? (True/False) ', st_A.issuperset(st_B))








