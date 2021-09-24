### Exercise 16 - Curso em Video
## Develop an algorithm to calculate a rent of a car
### PS: It costs $60 daily + 0,15 per km

km = float(input('How many km did you drive? '))
days = int(input('How many days did you rent this car? '))

rent = (60*days)+(km*0.15)

print('The price of this car rent will be {0:.2f}'.format(rent))