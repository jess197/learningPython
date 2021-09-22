### Exercise 12 - Curso em Video
## Develop a program to calculate the area and ink needed to paint a wall.
# It's important to know that for each liter of ink paints a 2m² area

width = float(input("What is the wall's width? "))
height = float(input("What is the wall's height? "))

area = width*height

liter = 2

neededliters = area/liter



print('It will be necessary {0} liters of paint for an area of {1} m²'.format(neededliters, area))
