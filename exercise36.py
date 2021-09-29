### Exercise 36 - Curso em Video
## Develop a program that reads the lenght of 3 sides and if the three sides make up a triangle

a = int(input('First side of the triangle: '))
b = int(input('Second side of the triangle: '))
c = int(input('Third side of the triangle: '))

if(a+b>c and a+c>b and b+c>a):
    print('This is a triangle!')
else:
    print("This isn't a triangle!")

