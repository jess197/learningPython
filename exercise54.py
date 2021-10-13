### Exercise 54 - Curso em Video
# Develop a program that reads a phrase and print if is a PALINDROME

phrase = input('Type a phrase: ')
count = 0
wphrase = phrase.replace(' ','').lower()
for n in range(0,len(wphrase)):
    if(list(wphrase[n]) == list(wphrase[::-1][n])):
        count += 1

if count == len(wphrase):
    print('It is a PALINDROME')
else:
    print('It is not a PALINDROME')




