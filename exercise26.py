### Exercise 26 - Curso em Video
## Develop a program to read a name of a person and say if he or she has SILVA in the name

name = input('Type your fullname: ')
namefind = name.upper().find('SILVA')

validname = bool(namefind != -1)

print('Hey! This name contains SILVA? {0} '.format(validname))
