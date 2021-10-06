### Exercise 38 - Curso em Video
## Develop a program that reads an integer number and asks to user choose the base conversion.
# 1 for binary
# 2 for octal
# 3 for hexadecimal
from time import sleep
number = int(input('Write a number: '))
print('='*20)
print('Menu')
print('You want to convert number {0} to: '.format(number))
print('1 - Binary')
print('2 - Octal')
print('3 - Hexadecimal')
print('='*20)
option = int(input())

if(option == 1):
    print('Converting...')
    sleep(5)
    print('Your number is: {0} converted to Binary is: {1}'.format(number,bin(number)))
elif(option == 2):
    print('Converting...')
    sleep(5)
    print('Your number is: {0} converted to Binary is: {1}'.format(number,oct(number)))
elif(option == 3):
    print('Converting...')
    sleep(5)
    print('Your number is: {0} converted to Binary is: {1}'.format(number, hex(number)))
else:
    print("This is isn't a valid option")




