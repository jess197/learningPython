### Exercise 52 - Curso em Video
# Develop a program that reads the first term and the commom difference of an arithmetic progression.
# In the end show the first 10 terms of this AP.

firstTerm = int(input('Type the first term of an AP: '))
commonDiff = int(input('Type the commom difference: '))

for n in range(0,10):
    if(n < 9):
        ap = firstTerm+n*commonDiff
        print('{},'.format(ap),end='')
    else:
        ap = firstTerm + n * commonDiff
        print('{}'.format(ap), end='')

