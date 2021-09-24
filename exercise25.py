### Exercise 25 - Curso em Video
## Develop a program to read a name of a city and say if starts or not with NEW

city = input('Type a name of a city: ')
citysplit = city.upper().split()
citynew = citysplit[0] == 'NEW'

print('City starts with NEW: {0}'.format(citynew))


