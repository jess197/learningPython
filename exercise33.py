### Exercise 33 - Curso em Video
## Develop a program that reads a year input and says if its leap year

year = int(input('Type a year: '))

if(year%4 == 0 and year%400 == 0):
    print("{0} it's a leap year!!".format(year))
else:
    print("{0} isn't a leap year".format(year))