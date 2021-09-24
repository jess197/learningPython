### Exercise 27 - Curso em Video
## Develop a program that reads a phrase and shows:
#1) How many times letter A appears
#2) First time apeard position
#3) Last time apeard position

phrase = input('Type a phrase: ')
phrase = phrase.lower()
count = phrase.count('a')
first = phrase.find('a')
last = phrase.rfind('a')

print('Phrase is: {0} \nQuantity of A: {1} \nFirst time A appeard: {2} \nLast time A appeard: {3}'.format(phrase,count,first,last))