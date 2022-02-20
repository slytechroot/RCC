'''
1.	In an English class, Carolina earns the following quiz grades: 92, 87, 93, 88. 
In the same class, Raquel earns the following quiz grades: 88, 92, 81, 97. 
Use Python sets and methods to perform the following tasks:
A.	Display the different quiz scores from Carolina’s and Raquel’s grades. 
# determine difference
B.	Display the same grades that are earned by the students.
C.	Remove the lowest quiz score for each student and display the quiz scores.
a.	Declare 2 sets, mutable sets, each contains scores of each student. 
a.	Use method to print the difference in scores.
b.	Use method to print the common grades, intersection.
c.	Use method to remove lowest quiz score, min() and remove(). 
Print the sets.
'''
c_scores = {92,87,93,88}
print('Carolina scores: ', c_scores)
r_scores = {88,92,81,97}
print("Raquel's score: ", r_scores)

#display difference
print(c_scores.difference(r_scores))
print(r_scores.difference(c_scores))
print(c_scores.symmetric_difference(r_scores))
print(r_scores.symmetric_difference(c_scores))

#display same grades earned
print('\n')
print(c_scores.intersection(r_scores))
print('\n')

#remove the lowest score
c_scores.remove(min(c_scores))
print(c_scores)
r_scores.remove(min(r_scores))
print(r_scores)













