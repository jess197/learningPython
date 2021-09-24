### Exercise 19 - Curso em Video
## Develop a program that reads any angle and shows sin,cos and tan

import math as m
ang = int(input('Type any angle: '))
rad = m.radians(ang)
sin = m.sin(rad)
cos = m.cos(rad)
tan = m.tan(rad)

print('Angle: {0:.0f} degrees \n Sin of this angle is: {1:.2f} \n Cos of this angle is: {2:.2f} \n Tan of this angle is: {3:.2f}'.format(ang,sin,cos,tan))