### Exercise 08 - Curso em Video
## Develop an algorithm to read two grades from a student and shows the average.

grade1 = float(input('Grade 1: '))
grade2 = float(input('Grade 2: '))

sumgrades = grade1+grade2
avg = sumgrades/2

print('Average grade from this student is: {0:.2f} '.format(avg))
