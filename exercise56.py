### Exercise 56 - Curso em Video
# Develop a program that reads the weight of 5 people and shows what was the heavier and lighter weight

for n in range(1,6):
    weight = float(input('What is the weight of person {0}: '.format(n)))
    if(n == 1):
        lighter = weight
        heavier = weight
    if(weight <= lighter):
        lighter = weight
    elif(weight >= lighter):
        heavier = weight
print('The heavier weight is: {0} and lighter weight is {1}'.format(heavier,lighter))