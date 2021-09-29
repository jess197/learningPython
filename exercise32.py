### Exercise 32 - Curso em Video
## Develop a program that asks a trip distance in kilometers. Calculate the price of the bus passage.
# For trips up to 200 km each kilometer is $0,50
# For trips more than 200 km each km is $0,45

tripDistance = float(input('What is the distance of this trip? '))

if(tripDistance < 200):
    busPassage = tripDistance*0.50
    print('The distance is less than 200km... So the bus passage is ${0:.2f}'.format(busPassage))
else:
    busPassage = tripDistance*0.45
    print('The bus passage is ${0:.2f}, because the distance is more than 200km.'.format(busPassage))