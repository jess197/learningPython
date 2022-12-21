# Exercise 61 - Factorial with recursive function


num = int(input('Type a number to get the factorial: '))

def factorial(num):
    if(num == 1): 
        return 1
    else: 
        return num * factorial(num-1)

print('The factorial from {0} is {1}'.format(num,factorial(num)))