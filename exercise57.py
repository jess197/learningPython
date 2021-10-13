### Exercise 57 - Curso em Video
## Develop a program that reads name, age and gender of 4 people and in the end shows:
# the average age of this group
# what is the name of the oldest man
# how many women has less than 21 yo
total = 0
count = 0
older = 0
olderguy: str = ""
for n in range(1,5):
    name = str(input('What is your name? '))
    age = int(input('What is your age? '))
    print(''' Select a option for your gender:
    1 - Man
    2 - Woman''')
    gender = input()
    total += age
    avg = total/n
    gender = int(gender)
    if gender == 1:
        if(older < age):
            older = age
            olderguy = name
    elif gender == 2:
        if(age < 21):
            count += 1
print('')
print('=-'*50)
print('This group is composed by {} women under 21 yo, {} is the oldest guy and the average age is {} '.format(count,olderguy,avg))
print('=-'*50)

