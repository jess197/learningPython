### Exercise 41 - Curso em Video
## Develop a program that reads the birthdate of an athlete and show his category:
# up to 9 years - KIDS
# up to 14 years - JUNIOR
# up to 19 years - MID LEVEL
# up to 20 years - SENIOR
# more than 20 years - MASTER

import time as t

birthdate = input('Please input your birthdate: ')
bd = birthdate.split('/')

birth_year = bd[2]

year = t.localtime().tm_year

y = year - int(birth_year)


if(y <= 9):
    print('You have {0} years. Your category is for KIDS'.format(y))
elif(y <= 14):
    print('You have {0} years. Your category is for JUNIORS'.format(y))
elif(y <= 19):
    print('You have {0} years. Your category is for MID LEVELS'.format(y))
elif(y <= 20):
    print('You have {0} years. Your category is for SENIORS'.format(y))
else:
    print('You have {0} years. Your category is for MASTERS'.format(y))