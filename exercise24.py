### Exercise 24 - Curso em Video
## Develop a program to read a number from 0 to 9999 and shows separated digits
# Example: Type a number: 1834 - Four digit number
# Ones: 4
## Tens: 3
### Hundreds: 8
#### Thousands: 1

number = input('Type any number from 0 to 9999: ')
sizestring = 4
numberfour = number.zfill(sizestring)
reversenum = numberfour[::-1]
print('Ones: {0} \nTens: {1} \nHundreds: {2} \nThousands: {3}'.format(reversenum[0],reversenum[1],reversenum[2],reversenum[3]))
#
# Math way
