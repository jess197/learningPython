### Exercise 41 - Curso em Video
## Develop a program that reads two grades of one student and calculate the average. Showing if:
# He/She PASSED
# He/She REPROVED
# He/She needs a RETAKE TEST

grade1 = float(input('What is your first grade? '))
grade2 = float(input('What is your second grade? '))

avg = (grade1+grade2)/2

if(avg > 7.0):
    print('Congratulations! Your average grade is {:0.2f}. You PASSED!!'.format(avg))
elif(6.9 > avg > 5.0):
    print('Your average grade is {:0.2f} and is under 7.0 . You will need to do a retake test!'.format(avg))
else:
    print('Your average grade is {:0.2f} is under 5.0. You reproved :( '.format(avg))

