### Exercise 17 - Curso em Video
## Develop an algorithm to read any Real number and shows the integer part of this number

import math as m

number = float(input('Type any real number: '))
integer = m.trunc(number)

print('The integer part of the {0} number is {1}'.format(number, integer))