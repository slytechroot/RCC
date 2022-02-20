"""
13.Marcella receives the following grades on her math assignments: 82, 91, 79, 63, 97.
Write a Python program that determines Marcella’s average assignment grade, given the following scale:
•Grade A: 90 to 100
•Grade B: 80 to 89
•Grade C: 70 – 79
•Grade D: 60 – 69
•Grade F: below 60
Program should contain IF-ELIF-ELSE statements

"""

grades = [82, 91, 79, 63, 97]
total = sum(grades)
avg_grade = total/5
print('Average grades: ', avg_grade)

if avg_grade <= 100 and avg_grade >= 90:
    print('Average grade is A')
if avg_grade <= 90 and avg_grade >= 80:
    print('Average grade is B')
if avg_grade <= 80 and avg_grade >= 70:
    print('Average grade is C')
if avg_grade <= 70 and avg_grade >= 60:
    print('Average grade is D')
else:
    print('Average grade is F')