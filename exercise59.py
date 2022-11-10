### Exercise 59 - Curso em Video
## Guessing game 2.0
from random import randrange
from time import sleep
print('-=-'*20)
print('Guessing game v2.0')
print('-=-'*20)
cont = 0
number = 0 
guess = int(input('Guess a number between 0 and 10: '))
print('PROCESSING...')
sleep(3)
while guess != number: 
    number = randrange(0,10)
    if True:
        guess = int(input('Try again. Guess a number between 0 and 10: '))
        cont += 1
print("Correct guess. You tried {} times until WIN!!!".format(cont))

