### Exercise 29 - Curso em Video
## Guessing game
from random import randrange
from time import sleep
print('-=-'*20)
print('Guessing game')
print('-=-'*20)
num = int(input('Guess random number between 0 and 5: '))

rand = randrange(0, 5)
print('PROCESSING...')
sleep(3)
if(num == rand):
    print('YOU WIN!!')
else:
    print('NOT THIS TIME, TRY AGAIN')
