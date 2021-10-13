### Exercise 55 - Curso em Video
# Develop a program that reads the birthdate of 7 people and shows how many are under 21 yet.

import time as t
under18 = 0
more18 = 0
for n in range(1,8):
    birth = input('Type a birthdate of the person {0}: '.format(n))
    birthyear = birth.split('/')
    mayority = t.localtime().tm_year - int(birthyear[2])

    if(mayority < 21):
        under18 += 1
    else:
        more18 += 1
print('')
print('There are {} people under of 21 yo and {} who has more than 21 yo'.format(under18,more18))


