# Exercise 61 - Factorial with for

num = int(input('Type a number to get the factorial: '))

factorial = 1 

for num in reversed(range(1,num+1)):
    factorial *= num
    num -= 1
print(factorial)