### Exercise 29 - Curso em Video
## Guessing game
from random import randrange
print('Guessing game')
num = int(input('Guess random number between 0 and 5: '))

rand = randrange(0, 5)

if(num == rand):
    print('YOU WIN!!')
else:
    print('NOT THIS TIME, TRY AGAIN')
