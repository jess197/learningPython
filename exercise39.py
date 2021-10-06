### Exercise 39 - Curso em Video
## Develop a program that receive two integer inputs and compare the numbers
# First value is bigger
# Second value is bigger
# Both are equal

num1 = int(input('Type a number: '))
num2 = int(input('Type another number: '))

if(num1 > num2):
    print('{0} is bigger than {1}'.format(num1,num2))
elif(num2 > num1):
    print('{0} is bigger than {1}'.format(num2,num1))
else:
    print('Neither are bigger or smaller. {0} is equal to {1}'.format(num1,num2))