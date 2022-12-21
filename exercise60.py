# Exercise 60 - Calculator

value1 = int(input('Type a number: '))
value2 = int(input('Type another number: '))
option = ''


while option == '': 
    print('1 - Sum')
    print('2 - Multiply')
    print('3 - Which one is bigger')
    print('4 - New numbers')
    print('5 - exit')
    option = int(input('Type your option based on menu above: '))

    if(option == 1): 
        result = value1+value2
    elif(option == 2): 
        result = value1*value2
    elif(option == 3):
        if value1 > value2: 
            result = value1
        elif value2 > value1:
            result = value2
        else:
            result = value1
    elif option == 4: 
        value1 = int(input('Type a number: '))
        value2 = int(input('Type another number: '))
        option = ''
        print(option)
    elif option == 5: 
        break
    else:
       option = ''

if option in (1,2,3):
    print('You have chosen the option {0}, so your result is: {1}'.format(option,result))





