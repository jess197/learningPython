### Exercise 18 - Curso em Video
## Develop an algorithm to calculate hypotenuse of a right triangle

import math as m
print('Pythagorean Theorem')
a = int(input('What is the value of A side? '))
b = int(input('What is the value of B side? '))

x = m.hypot(a,b)

print('The hypotenuse will be: {0}'.format(x))