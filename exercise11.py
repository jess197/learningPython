### Exercise 11 - Curso em Video
## Develop a program to convert real to dolar

dolar = 5.30

real = float(input('How much R$ do you want to convert in U$? '))
conversion = real/dolar
print('The amount you have in R${0:.2f} is equivalent to U${1:.2f}'.format(real, conversion))