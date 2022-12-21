# Exercise 61 - Factorial with while

num = int(input('Type a number to get the factorial: '))

factorial = 1

while num > 1:
    factorial *= num 
    num -= 1

print(factorial)