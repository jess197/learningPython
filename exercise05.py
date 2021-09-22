### Exercise 05 - Curso em Video
## Develop a program to read an input and shows primitive types.

some = input('Type something: ')
isnum = some.isnumeric()
isalfa = some.isalpha()
isalfanum = some.isalnum()
isupper = some.isupper()
islower = some.islower()

print('You typed: ', some)
print('Type: ', type(some))
print('Is numeric? ', isnum)
print('Is alpha? ', isalfa)
print('Is alphanumeric? ', isalfanum)
print('Is uppercase? ', isupper)
print('Is lowercase? ', islower)