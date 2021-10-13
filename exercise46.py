### Exercise 46 - Curso em Video
## Develop a program to play jokenpo with you

from random import choice
from time import sleep
print('=-'*20)
print('JOKENPO GAME')
print('Choose one option: ')
print('1 - Rock')
print('2 - Scissor')
print('3 - Paper')
print('=-'*20)
playerChoice = int(input())

if(playerChoice == 1):
    playerChoice = 'Rock'
elif(playerChoice == 2):
    playerChoice = 'Scissor'
elif(playerChoice == 3):
    playerChoice = 'Paper'
else:
    print('Invalid option')

computerOption = ['Rock','Scissor','Paper']

computerChoice = choice(computerOption)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if(computerChoice == 'Paper'):
  if(playerChoice == 'Rock'):
      print('I WON, YOU LOST! I choose {} and you choose {}'.format(computerChoice, playerChoice))
  elif(playerChoice == 'Scissor'):
      print('CONGRATULATIONS YOU WON, I LOST! I choose {} and you choose {}'.format(computerChoice, playerChoice))
  elif(playerChoice == 'Paper'):
      print("It's a DRAW. We need to play again. I choose {} and you choose {} as well".format(computerChoice, playerChoice))
elif(computerChoice == 'Rock'):
    if (playerChoice == 'Rock'):
        print("It's a DRAW. We need to play again. I choose {} and you choose {} as well".format(computerChoice, playerChoice))
    elif (playerChoice == 'Scissor'):
        print('I WON, YOU LOST! I choose {} and you choose {}'.format(computerChoice, playerChoice))
    elif (playerChoice == 'Paper'):
        print('CONGRATULATIONS YOU WON, I LOST! I choose {} and you choose {}'.format(computerChoice, playerChoice))
elif(computerChoice == 'Scissor'):
    if (playerChoice == 'Rock'):
        print('CONGRATULATIONS YOU WON, I LOST! I choose {} and you choose {}'.format(computerChoice, playerChoice))
    elif (playerChoice == 'Scissor'):
        print("It's a DRAW. We need to play again. I choose {} and you choose {} as well".format(computerChoice, playerChoice))
    elif (playerChoice == 'Paper'):
        print('I WON, YOU LOST! I choose {} and you choose {}'.format(computerChoice, playerChoice))









