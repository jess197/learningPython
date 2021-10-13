### Exercise 51 - Curso em Video
# Develop a program that reads six integer numbers and sum just the even of them.

s = 0
for n in range(0,7):
    num = int(input('Type a number: '))
    if(num%2 == 0):
        s += num
print('The sum of these even numbers is: {0} '.format(s))