### Exercise 28 - Curso em Video
## Develop a program who reads a person's fullname and shows first and last names

fullname = input('What is your fullname? ')
split = fullname.split()
first = split[0]
last = split[len(split)-1]
print('First Name is: {0} \nLast Name is: {1}'.format(first,last))
