### Exercise 21 - Curso em Video
## A teacher wants to sort one of his students to do a presentation.
# Develop a program to order the list of the choosen students

import random as r

s1 = input('Student 1: ')
s2 = input('Student 2: ')
s3 = input('Student 3: ')
s4 = input('Student 4: ')

list = [s1,s2,s3,s4]
r.shuffle(list)

print('The order will be {0}'.format(list))