### Exercise 49 - Curso em Video
# Develop a program that calculate the sum between odd numbers multiples of three in range of 0 to 500
s = 0
for num in range(0,500):
    if(num%3 == 0 and num%2 == 1):
       s += num
print('Sum of odd numbers multiples of three in range of 0 to 500 is: {} '.format(s))