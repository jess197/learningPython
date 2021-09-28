### Exercise 29 - Curso em Video
## Develop a program that reads the speed of a car and if it ultrapass 80km/h, show a message saying that the conductor got a traffic ticket.
# PS: The traffic ticket will cost $7 each km exceeded.

vel = float(input('Speed of the car: '))
limitvel = 80

if(vel < limitvel):
    print('Congrats!')
else:
    exceedvel = vel-limitvel
    tticket = exceedvel*7
    print('You will receive a traffic ticket! You will need to pay ${0}'.format(tticket))