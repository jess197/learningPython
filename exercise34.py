### Exercise 34 - Curso em Video
## Develop a program to read 3 numbers and say which is bigger or smaller.

num1 = int(input('Type a number: '))
num2 = int(input('Type another number: '))
num3 = int(input('Type a third number: '))

if(num1 > num2 > num3):
    print('{0} is bigger and {1} is the smaller'.format(num1,num3))
else:
    if(num1 > num3 > num2):
        print('{0} is bigger and {1} is the smaller'.format(num1,num2))
    else:
        if(num2 > num1 > num3):
            print('{0} is bigger and {1} is the smaller'.format(num2, num3))
        else:
            if(num2 > num3 > num1):
                print('{0} is bigger and {1} is the smaller'.format(num2, num1))
            else:
                if(num3 > num1 > num2):
                    print('{0} is bigger and {1} is the smaller'.format(num3, num2))
                else:
                    print('{0} is bigger and {1} is the smaller'.format(num3, num1))







