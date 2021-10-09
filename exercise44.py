### Exercise 43 - Curso em Video
## Develop a program that reads the weight and height of a person and calculate his or her BMI.
# Underweight = < 18.5
# Normal weight = 18.5 to 24.9
# Overweight = 25 to 29.9
# Obesity BMI of 30 or greater

print('Enter your weight and height using metric measures')
weight = float(input('What is your weight? '))
height = float(input('What is your height? '))

bmi = weight/pow(height,2)
print('')
print('Your BMI is: {:0.2f} '.format(bmi))
if(bmi <= 18.5):
    print('Your are underweight')
elif(18.5 <= bmi <= 24.9):
    print('You have a normal weight')
elif(25.0 <= bmi <= 29.9):
    print('You are overweight')
else:
    print('You are with obesity!')