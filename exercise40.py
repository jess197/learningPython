### Exercise 40 - Curso em Video
## Develop a program that receive the birth date of a male brazillian to inform:
# 1 - if he need to present to local army
# 2 - if he need to present to local army now
# 3 - if it passed the time to present to local army and he is late
import time
print('='*20)
print('Please inform your gender: ')
print('1 - Female')
print('2 - Male')
print('3 - Prefer not inform')
gender = int(input())

if(gender == 2):
    birth = str(input('What is your birth date ? '))
    splitbirth = birth.split('/')
    today = time.localtime()
    year = today.tm_year
    month = today.tm_mon
    day = today.tm_mday

    yo = year - int(splitbirth[2])
    mo = month - int(splitbirth[1])
    dy = day - int(splitbirth[0])

    if(mo < int(splitbirth[1]) and mo !=0):
        yo = yo - 1
        mo = 12 - abs(mo)
    elif(mo == 0):
        yo = yo
    elif(yo < 0 or mo < 0):
        print('This is an invalid input. Try again')
    elif(dy < 0):
        mo = mo - 1

    if(yo == 18):
        print('You need to present yourself to local army!')
    elif(yo < 18):
        time = 18-yo
        print('You need to present yourself to local army in {0} years and {1} months'.format(time,mo))
    else:
        time = yo - 18
        print('You are late in {0} years and {1} months, you need to present to local army as soon as possible!'.format(time,mo))
else:
    print("Congratulations, you don't need to present yourself to local army")





