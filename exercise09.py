### Exercise 09 - Curso em Video
## Develop a program that reads a value in meters and convert to centimeters and millimeters.

measure = float(input('Type a measure in meters: '))

cm = measure*100
mm = measure*1000

print('Measure in: \n Meters: {0} m \n Centimeters: {1} cm \n Millimeters: {2} mm'.format(measure, cm, mm))

