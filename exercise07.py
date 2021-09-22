### Exercise 07 - Curso em Video
## Develop an algorithm who read a number and show double, triple and square.

number = int(input('Type a number: '))
double = number*2
triple = number*3
square = number** (1/2)

print('The number is: {0}\n Double is: {1} \n Triple is {2} \n Square is: {3:.2f}'.format(number, double, triple, square))
