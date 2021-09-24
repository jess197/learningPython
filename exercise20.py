### Exercise 20 - Curso em Video
## A teacher wants to sort one of his students to do a presentation.
# Develop a program to help him reading his students names and writing their names

import random as r

student1 = input('Name of first student: ')
student2 = input('Name of second student: ')
student3 = input('Name of third student: ')
student4 = input('Name of fourth student: ')

rand = r.choice([student1,student2,student3,student4])

print('I choose {0} to be starting to present '.format(rand))

