#Exercise 58 
# Develop a script who reads a person gender and only accepts 'W', 'M', and 'N'. If receives the wrong value ask again until receives
# the correct value  

gender = str(input('What is your gender? ')).upper()
while gender != 'M' and gender != 'W' and gender != 'N': 
    gender = str(input('Type again: '))
print('Correct answer!')


