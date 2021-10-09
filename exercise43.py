### Exercise 43 - Curso em Video
## Develop a program that reads the lenght of 3 sides and if the three sides make up a triangle and if it is:
# Equilateral triangle
# Isosceles triangle
# Scalene triangle

a = int(input('First side of the triangle: '))
b = int(input('Second side of the triangle: '))
c = int(input('Third side of the triangle: '))

if(a+b>c and a+c>b and b+c>a):
    if(a == b == c):
        print('This is an Equilateral triangle! ')
    elif(a == b or b == c or a == c):
        print('This is an Isoceles triangle!')
    else:
        print('This is an Scalene triangle!')
else:
    print("This isn't a triangle!")