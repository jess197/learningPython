### Exercise 23 - Curso em Video
## Develop a program to read a person's fullname and shows:
# 1 - Name with all letters in UPPPERCASE
# 2 - Name with all letters in lowercase
# 3 - How many letters in total (without spaces)
# 4 - How many letters have first name

import re

fullname = input('What is your fullname? ').strip()
#1
nameupper = fullname.upper()
#2
namelower = fullname.lower()
#3
totaletters = len(re.sub(r'\s+', '',fullname)) #Regular expression with re lib
#or
space = fullname.count(' ')
wtnospace = len(fullname)-space
#or
tot = len(fullname.replace(' ',''))
#4
firstname = fullname.split()

print('Fullname: {0} \nName with UPPERCASE: {1}\nName with lowercase: {2}\nHow many letters in total: {3}\nHow many letters have first name: {4}'.format(fullname,nameupper,namelower,totaletters,firstname[0]))
